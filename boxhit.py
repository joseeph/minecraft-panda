from mcpi import minecraft
from mcpi import block
from time import sleep

import time

mc = minecraft.Minecraft.create() 


	

while True:

	
	blockHits = mc.events.pollBlockHits()
	
	if blockHits:
		
		for blockHit in blockHits:
			print blockHit.pos.x
			print blockHit.pos.y
			print blockHit.pos.z
			print blockHit.face
			print blockHit.type
			print blockHit.entityId


