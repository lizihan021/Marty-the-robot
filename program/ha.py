from PCA9685 import PCA9685

pwm = PCA9685(0x40)
pwm.setsq(50)
pwm.allinit()
pwm.setallpwm(0,4000)
pwm.setallangle(90)