from mcpi import minecraft
from mcpi import block
from time import sleep
import pi2go 
import time

# Reading single character by forcing stdin to raw mode
import sys
import tty
import termios

list_range = range(15)


mc = minecraft.Minecraft.create()

while True:
	
	mc.setBlocks(0,-1,0, 15,-1,15,block.WOOD.id)
	
	mc.setBlocks(0, 0, -0, 15, 15, 15, block.Block(0))
	
	exit()
