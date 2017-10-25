#!/usr/bin/env python

import numpy as np
import cv2
import os
import time
# local modules
from video import create_capture
from common import clock, draw_str
from duo import duo

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print help_message

    marty = duo()
    marty.init()

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    #define the xml files used to detect the face in the picture
    cascade_fn = args.get('--cascade', "xmlf/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "xmlf/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src, fallback='synth:bg=pic/test.jpg')

    while True:
        #take a picture
        os.system('raspistill -o pic/test.jpg -t 40 -w 500 -h 500 -q 50')
        time.sleep(0.01)
        cam = create_capture(video_src, fallback='synth:bg=pic/test.jpg')
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        if len(rects):
            for x1, y1, x2, y2 in rects:
                xmid = (x2 + x1)/2
                kuan = (x2 - x1)
                if (xmid>300 and xmid<495):
                    marty.turn((250-xmid)*40/250,5)
                if (xmid>5 and xmid<200):
                    marty.turn((250 -xmid)*40/250,5)
                if (kuan>5 and kuan<150):
                    marty.walk(2,7) 
                '''
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
                '''
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        #cv2.imshow('facedetect', vis)
        print rects

        if 0xFF & cv2.waitKey(5) == 27:
            break
        #if KeyboardInterrupt:
        #    break
            
    cv2.destroyAllWindows()
