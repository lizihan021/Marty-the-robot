# Written by Zihan Li
The program of Marty is written by Python.

The program is based on Raspbian OS on Raspberry Pi 3, with the PREREQUESTS: 
1. the OS has been configed with i2c communication
2. the i2c port is connected with PCA9685 module
3. openCV-3.0.0 is installed in the system

Main files: 
	duo.py  # this is the main driven program of marty.
		    # it defines an object called duo which include following functions:
		    # .dance(times, speed) to dance "times" times at "speed" speed
		    # .walk(times, speed)  to walk "times" times at "speed" speed
		    # .turn(angle, speed)  to turn "angle" at "speed" speed
		    # .zhuanyan(times, range, speed) to rotate eyes
		    # .dongshou(times, jizhun, tange, speed) to move hand

	face.py # this is the face detection file marty will take picture around every 
			# 0.5 seconds. Pictures is under /pic folder.
			# If there is face detected, Marty will turn to the direction 
			# of the face. If the face is far from Marty, it will walk toward the 
			# direction of the face.

	boom.py # this file serves as a example if you want to move Marty's hand, eyes
			# and legs simultaniously. DO NOT TRY TO WALK AND DANCE SIMUTANIOUSLY,
			# BECAUSE THAT MIGHT CAUSE ERRORS. 

	PCA9685.py video.py common.py and <files in /xmlf> come from 3rd party.

	other files are test files and serves as examples about how to control Marty.

File dependency:
	duo.py -> PCA9685.py
	face.py -> video.py
			-> common.py
			-> <files in /xmlf>
			-> </pic>
	boom.py -> yan.py
			-> shou.py
			-> dance.py
