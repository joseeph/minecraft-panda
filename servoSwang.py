#!/usr/bin/python
# servoTest.py

import pi2go
import time



#======================================================================
# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios


pi2go.init()
	
def swingArm():	
		# Define pins for Left/Right hand
	leftHand = 0
	RightHand = 1
	spinTime = 0.5
	runTime = 0.03
	lVal = 0 # 0 degrees is centre
	rVal = 0 # 0 degrees is centre
	i = 0
	while i <= 4:
		t_end=time.time() + runTime
		while time.time() < t_end:
			pi2go.setServo(leftHand,lVal)
			pi2go.setServo(RightHand,rVal)
		lVal = lVal + 5
		rVal = rVal - 5
		print lVal, rVal
		if lVal==90 or rVal==-90:
			i = i +1
			print 'start reverse!' , lVal, rVal
			k=0
			while k < 18:
				print 'in loop reverse1'
				t_end=time.time() + runTime
				while time.time() < t_end:
					pi2go.setServo(leftHand,lVal)
					pi2go.setServo(RightHand,rVal)
				lVal = lVal - 5
				rVal = rVal + 5
				k = k+1
				print 'in loop reverse2'
				
				
def findBamboo():
	 dist = pi2go.getDistance()
	 print dist
	 if dist<=3:
		 return True
		 
while True:
	if findBamboo():
		swingArm()
		
		
				

	
