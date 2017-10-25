# -*- coding: UTF-8 -*-
#from PCA9685 import PCA9685 #导入驱动
#import time
#pwm=PCA9685(0x40)
#pwm.setsq(50)#设置频率
#pwm.init()#初始化pca9685
#pwm.allinit()#把16个通道初始化
#pwm.setallpwm(0,4000)#设置所有通道。两个参数，前面一个是低电平转高电平的时间，后面一个是高电平转低电平的时间，这两个数值都应该小于4096
#pwm.setpwm(0,0,4000)#第一个参数为通道。两个参数，前面一个是低电平转高电平的时间，后面一个是高电平转低电平的时间，这两个数值都应该小于4096
#pwm.setallangle(180)#所有通道的舵机都设置为180度并且频率设为50
#pwm.setangle(0,180)#设置0通道为180度
#pwm.getsq()#读取频率

from duo import duo
import time
marty = duo()
marty.init()
marty.dance(3,6)
