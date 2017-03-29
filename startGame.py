from mcpi import minecraft
from mcpi import block
from time import sleep
import pi2go 
import time

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

mc = minecraft.Minecraft.create()
pi2go.init()

blkOrigin = [-23, 48, 28]
blk1 = [blkOrigin[0]+4, blkOrigin[1], blkOrigin[2]]
blk2 = [blkOrigin[0]+2, blkOrigin[1], blkOrigin[2]]
blk4 = [blkOrigin[0]-2, blkOrigin[1], blkOrigin[2]]
blk5 = [blkOrigin[0]-4, blkOrigin[1], blkOrigin[2]]
blkList = [blk1, blk2, blkOrigin, blk4, blk5]
b_x = 0
b_y = 0
b_z = 0
robotSpeed = 50
spinTime = 0.5
runTime = 0.5


def pandaMoveForward():
	pi2go.init()
	mc.postToChat('Move Fordward!')
	t_end=time.time() + runTime
	while time.time() < t_end:
		pi2go.forward(robotSpeed)
	print 'Forward', robotSpeed
	pi2go.stop()
	return 
	
def pandaSpinLeft():
	pi2go.init()
	mc.postToChat('spin Left!')
	t_end=time.time() + spinTime
	while time.time() < t_end:
		pi2go.spinLeft(robotSpeed)
	print 'Left', robotSpeed
	pi2go.stop()
	return 
	
def pandaSpinRight():
	pi2go.init()
	mc.postToChat('Spin Right!')
	t_end=time.time() + spinTime
	while time.time() < t_end:
		pi2go.spinRight(robotSpeed)
	print 'Right', robotSpeed
	pi2go.stop()
	return 
	
def pandaMoveBackward():
	pi2go.init()
	mc.postToChat('Move Backward!')
	t_end=time.time() + runTime
	while time.time() < t_end:
		pi2go.reverse(robotSpeed)
	print 'backWard', robotSpeed
	pi2go.stop()

	return 
	
	
def setDiamond():
	for blk in blkList:
		mc.setBlock(blk[0],blk[1],blk[2],block.DIAMOND_BLOCK.id)
		print blk
	
		
def swingArm():	
	mc.postToChat('Bingo, got the bamboo!')
		# Define pins for Left/Right hand
	leftHand = 0
	RightHand = 1
	spinTime = 0.5
	runTime = 0.03
	lVal = 0 # 0 degrees is centre
	rVal = 0 # 0 degrees is centre
	i = 0
	while i <= 5:
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

def armMove():
	mc.postToChat('Stretch!')
	# Define pins for Left/Right hand
	leftHand = 0
	RightHand = 1
	spinTime = 0.5
	runTime = 0.03
	lVal = 0 # 0 degrees is centre
	rVal = 0 # 0 degrees is centre
	i = 0
	while i < 1:
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
l = 0
while True:
	
	if l <1:
		mc.postToChat('Game Started, try to hit the diamond block with right click and lead panda to bamboo!')
	l = l+1
	setDiamond()
	blockEvents = mc.events.pollBlockHits()
	for blockEvent in blockEvents:
		b_x = blockEvent.pos.x
		b_y = blockEvent.pos.y
		b_z = blockEvent.pos.z
		if (b_x == blkOrigin[0] and b_y == blkOrigin[1] and b_z == blkOrigin[2]):
			pandaSpinLeft()  
			break
		elif (b_x == blkList[0][0] and b_y == blkList[0][1] and b_z == blkList[0][2]):	
			pandaMoveForward()
			break
		elif (b_x == blkList[1][0] and b_y == blkList[1][1] and b_z == blkList[1][2]):	
			pandaMoveBackward()
			break
		elif (b_x == blkList[3][0] and b_y == blkList[3][1] and b_z == blkList[3][2]):		
			pandaSpinRight()
			break
		elif (b_x == blkList[4][0] and b_y == blkList[4][1] and b_z == blkList[4][2]):		
			armMove()
			break
	if findBamboo():
		swingArm()
		
			
			
	
	
