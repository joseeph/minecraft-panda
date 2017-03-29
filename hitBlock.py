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

def moveForward():
	speed = 50

	pi2go.init()

	t_end=time.time() +0.5

	while time.time() < t_end:
		pi2go.forward(speed)
		print 'Forward', speed
	pi2go.stop()
	return
	
def creatBlock():
	
	pos = mc.player.getTilePos()
	
	b = mc.setBlock(pos.x+1, pos.y,pos.z,block.DIAMOND_BLOCK.id)
	return pos
	
def blockHit():
	blockEvents = mc.events.pollBlockHits()
	for blockEvent in blockEvents:
		
		return blockEvent
	
def detectHit(block,hitBlock):
	if block.x+1 == hitBlock.pos.x or block.y == hitBlock.pos.y or block.z ==hitblock.pos.z:
		return True
		
while True:
	if detectHit(creatBlock(),blockHit()):
		moveForward()
	
	
