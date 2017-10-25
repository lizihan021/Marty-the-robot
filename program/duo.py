# -*- coding: UTF-8 -*-
# Written by Zihan Li
# this is the main driven program of marty.
# it defines an object called duo which include following functions:
		# .dance(times, speed) to dance "times" times at "speed" speed
		# .walk(times, speed)  to walk "times" times at "speed" speed
		# .turn(angle, speed)  to turn "angle" at "speed" speed
		# .zhuanyan(times, range, speed) to rotate eyes
		# .dongshou(times, jizhun, tange, speed) to move hand

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

from PCA9685 import PCA9685 
import time

#assign the pin of servo 
zuod1 = 4
zuod2 = 5
zuod3 = 6
youd1 = 8
youd2 = 9
youd3 = 10

yan = 12
yous = 13
zuos = 14

class duo: 
	def __init__(self):
		self._pwm = PCA9685(0x40)
		self._pwm.setsq(50)
		self._pwm.setallpwm(0,4000)
		self._pwm.allinit()

	def reset(self):
		zuojiao = -4
		youjiao = 5
		zuo2 = 0
		you2 = 0
		yo = 0
		zu = 0
		self._pwm.setangle(youd3,90+youjiao)
		self._pwm.setangle(zuod3,90+zuojiao)
		self._pwm.setangle(youd2,90+you2)
		self._pwm.setangle(zuod2,90+zuo2)
		self._pwm.setangle(youd1,90+yo)
		self._pwm.setangle(zuod1,90+zu)
		self._pwm.setangle(yous,90)
		self._pwm.setangle(zuos,90)
		self._pwm.setangle(yan,90)
		self.jz1 = 90 #use to record the current angle of servo.
		self.jz2 = 90
		self.jz3 = 90
		self.jy1 = 90
		self.jy2 = 90
		self.jy3 = 90

	#must be called before calling the following functions 
	def init(self):
		self._pwm.allinit()
		self.reset()

	def dance(self, times = 3, speed = 5):
		if speed>10: speed = 10
		if speed<1: speed = 1
		zuojiao = -4
		youjiao = 2
		fuduu = 25
		self._pwm.setangle(youd3,90+youjiao)
		self._pwm.setangle(zuod3,90+zuojiao)
		for j in range(0,times):
			for i in range(0, fuduu+1):
				self._pwm.setangle(youd3,90-i+youjiao)
				self._pwm.setangle(zuod3,90-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*fuduu+1):
				self._pwm.setangle(youd3,90-fuduu+i+youjiao)
				self._pwm.setangle(zuod3,90-fuduu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, fuduu+1):
				self._pwm.setangle(youd3,90+fuduu-i+youjiao)
				self._pwm.setangle(zuod3,90+fuduu-i+zuojiao)
				time.sleep(0.004*(11-speed))
		
	def walk(self, times = 1, speed = 5):
		if speed>10: speed = 10
		if speed<1: speed = 1
		zuojiao = -4
		youjiao = 5
		zuo = 0
		you = 0
		fudu = 22
		taijiao = 17
		qian = 10
		self._pwm.setangle(youd3,90+youjiao)
		self._pwm.setangle(zuod3,90+zuojiao)
		self._pwm.setangle(youd1,90+you)
		self._pwm.setangle(zuod1,90+zuo)
		for i in range(0, fudu+1):
			self._pwm.setangle(youd3,90-i+youjiao)
			self._pwm.setangle(zuod3,90-i+zuojiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, taijiao+1):
			self._pwm.setangle(youd3,90-fudu-i+youjiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, qian+1):
			self._pwm.setangle(youd1,90+i+you)
			self._pwm.setangle(zuod1,90-i+zuo)
			time.sleep(0.004*(11-speed))

		for j in range(0,times):
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-taijiao+i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*fudu+1):
				self._pwm.setangle(youd3,90-fudu+i+youjiao)
				self._pwm.setangle(zuod3,90-fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*qian+1):
				self._pwm.setangle(youd1,90+qian-i+you)
				self._pwm.setangle(zuod1,90-qian+i+zuo)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+taijiao-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*fudu+1):
				self._pwm.setangle(youd3,90+fudu-i+youjiao)
				self._pwm.setangle(zuod3,90+fudu-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*qian+1):
				self._pwm.setangle(youd1,90-qian+i+you)
				self._pwm.setangle(zuod1,90+qian-i+zuo)
				time.sleep(0.004*(11-speed))

		for i in range(0, taijiao+1):
			self._pwm.setangle(youd3,90-fudu-taijiao+i+youjiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, 2*fudu+1):
			self._pwm.setangle(youd3,90-fudu+i+youjiao)
			self._pwm.setangle(zuod3,90-fudu+i+zuojiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, taijiao+1):
			self._pwm.setangle(zuod3,90+fudu+i+zuojiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, qian+1):
			self._pwm.setangle(youd1,90+qian-i+you)
			self._pwm.setangle(zuod1,90-qian+i+zuo)
			time.sleep(0.004*(11-speed))
		for i in range(0, taijiao+1):
			self._pwm.setangle(zuod3,90+fudu+taijiao-i+zuojiao)
			time.sleep(0.004*(11-speed))
		for i in range(0, fudu+1):
			self._pwm.setangle(youd3,90+fudu-i+youjiao)
			self._pwm.setangle(zuod3,90+fudu-i+zuojiao)
			time.sleep(0.004*(11-speed))

#angle < 0 means turn right
	def turn(self, angle = 0, speed = 5):
		if speed>10: speed = 10
		if speed<1: speed = 1
		if angle > 35: angle = 35
		if angle < -35: angle = -35
		zuojiao = -4
		youjiao = 5
		zuo2 = 0
		you2 = 0
		fudu = 22
		taijiao = 17
		self._pwm.setangle(youd3,90+youjiao)
		self._pwm.setangle(zuod3,90+zuojiao)
		self._pwm.setangle(youd2,90+you2)
		self._pwm.setangle(zuod2,90+zuo2)
		#means turn left
		if angle<0:
			for i in range(0, fudu+1):
				self._pwm.setangle(youd3,90-i+youjiao)
				self._pwm.setangle(zuod3,90-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, -angle+1):
				self._pwm.setangle(zuod2,90-i+zuo2)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-taijiao+i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*fudu+1):
				self._pwm.setangle(youd3,90-fudu+i+youjiao)
				self._pwm.setangle(zuod3,90-fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, -angle+1):
				self._pwm.setangle(zuod2,90+angle+i+zuo2)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+taijiao-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, fudu+1):
				self._pwm.setangle(youd3,90+fudu-i+youjiao)
				self._pwm.setangle(zuod3,90+fudu-i+zuojiao)
				time.sleep(0.004*(11-speed))
		else:
			for i in range(0, fudu+1):
				self._pwm.setangle(youd3,90+i+youjiao)
				self._pwm.setangle(zuod3,90+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, angle+1):
				self._pwm.setangle(youd2,90+i+you2)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(zuod3,90+fudu+taijiao-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, 2*fudu+1):
				self._pwm.setangle(youd3,90+fudu-i+youjiao)
				self._pwm.setangle(zuod3,90+fudu-i+zuojiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, angle+1):
				self._pwm.setangle(youd2,90+angle-i+you2)
				time.sleep(0.004*(11-speed))
			for i in range(0, taijiao+1):
				self._pwm.setangle(youd3,90-fudu-taijiao+i+youjiao)
				time.sleep(0.004*(11-speed))
			for i in range(0, fudu+1):
				self._pwm.setangle(youd3,90-fudu+i+youjiao)
				self._pwm.setangle(zuod3,90-fudu+i+zuojiao)
				time.sleep(0.004*(11-speed))

	def zhuanyan(self,times = 4, yanrange = 20,speed = 5):
		if speed>10: speed = 10
		if speed<1: speed = 1
		for j in range(0,times):
			for i in range(0,yanrange+1):
				self._pwm.setangle(yan,90-i)
				time.sleep(0.004*(11-speed))
			for i in range(0,2*yanrange+1):
				self._pwm.setangle(yan,90-yanrange+i)
				time.sleep(0.004*(11-speed))
			for i in range(0,yanrange+1):
				self._pwm.setangle(yan,90+yanrange-i)
				time.sleep(0.004*(11-speed))

	#move hand at 'jizhun' +- 'srange' with speed of 5
	def dongshou(self, times = 4, jizhun = 40, srange = 20,speed = 5):
		if speed>10: speed = 10
		if speed<1: speed = 1
		for j in range(0,times):
			for i in range(0,srange+1):
				self._pwm.setangle(yous,jizhun-i)
				self._pwm.setangle(zuos,180-jizhun-i)
				time.sleep(0.004*(11-speed))
			for i in range(0,2*srange+1):
				self._pwm.setangle(yous,jizhun-srange+i)
				self._pwm.setangle(zuos,180-jizhun-srange+i)
				time.sleep(0.004*(11-speed))
			for i in range(0,srange+1):
				self._pwm.setangle(yous,jizhun+srange-i)
				self._pwm.setangle(zuos,180-jizhun+srange-i)
				time.sleep(0.004*(11-speed))
		self._pwm.setangle(yous,90)
		self._pwm.setangle(zuos,90)