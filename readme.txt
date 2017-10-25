this is a project called Marty. 
made by Zihan Li 

FILES:
	*.prt files 		can be open by UG NX 10.0. They are used for 3D printing.
	_asm.prt 			is the assembly file that can give you a direct view of Marty.
	pi-shell.dwg 		is used to hold a fan to cool Raspi down. It is used for acrylic laser cut.
	eye-gear.txt 		is the parameters used to define the gear on Marty's eyes.
	pin-assignment.jpg 	is the GPIO pins on Raspi.

	programs are under /program and there is another Readme file to explain it.

HOW TO BUILD MARTY:
	Material List:
		8mm*M3 screws 
		a 3D printer with plenty of PLA
		SG90 Servo *9
		PCA9685 module
		Raspberry Pi 3 B+
		Pi Camera
		500 mAh, 11.1 V Li-battery
		voltage reduction module 12 V to 6 V

	You need to export *.prt files to *.stl files for 3D printing.
	You need to print:
		12 pieces of MMarty1.prt 	connecting bar
		8 pieces of marty4.prt 		supporting plate
		4 pieces of marty3.prt 		servo connecting bar
		2 pieces of marty2.prt 		third servo
		2 pieces of marty5.prt 		feet of marty
		2 pieces of marty6.prt 		second servo
		2 pieces of marty7.prt 		first servo
		2 pieces of shou.prt 		arms of marty
		2 pieces of yanjing.prt 	eyes of marty
		1 piece of body.prt 		body of marty


HOW TO USE MARTY:
	1. connect i2c ports on Raspi with PCA9685 module
		PIN03 GPIO02 -> SDA
		PIN05 GPIO03 -> SCL
		PIN04 VCC	 -> VCC (NOT "V+" !)
		PIN06 GROUND -> GND

	2. connect voltage reduction module with V+ and GND on the PCA9685 to support power.

	3. run "python set.py" on Raspi and THEN connect the battery to voltage reduction module.

	4. run other programs such as "dance.py" to test Marty. 


Eye gear:
模数 modulus 			0.22
齿数 teeth number 		24
宽度 thickness 			4
压力角 pressure angle 	36