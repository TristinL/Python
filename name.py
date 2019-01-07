from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#start character at (0, 50, 0)

mc.player.setPos(0, 50, 0)

#delay time 10 seconds

import time
time.sleep(10)

#Get player tile pos. and assign to variables

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

#set block type

blocktype = 37

#produce letter "T" x+10, z-12 spaces infront of player

mc.setBlock(x+14, y, z-12, blocktype)
mc.setBlock(x+14, y, z-11, blocktype)
mc.setBlock(x+13, y, z-11, blocktype)
mc.setBlock(x+12, y, z-11, blocktype)
mc.setBlock(x+11, y, z-11, blocktype)
mc.setBlock(x+10, y, z-11, blocktype)
mc.setBlock(x+14, y, z-10, blocktype)

#Produce letter "r" x+10, z-9 spaces infront of player

mc.setBlock(x+13, y, z-9, blocktype)
mc.setBlock(x+12, y, z-9, blocktype)
mc.setBlock(x+11, y, z-9, blocktype)
mc.setBlock(x+10, y, z-9, blocktype)
mc.setBlock(x+13, y, z-8, blocktype)
mc.setBlock(x+13, y, z-7, blocktype)
mc.setBlock(x+12, y, z-7, blocktype)

#Produce letter "i" x+10, z-5 spaces infront of player

mc.setBlock(x+14, y, z-5, blocktype)
mc.setBlock(x+12, y, z-5, blocktype)
mc.setBlock(x+11, y, z-5, blocktype)
mc.setBlock(x+10, y, z-5, blocktype)

#Produce letter "s" x+10, z-3 spaces infront of player

mc.setBlock(x+14, y, z-3, blocktype)
mc.setBlock(x+13, y, z-3, blocktype)
mc.setBlock(x+12, y, z-3, blocktype)
mc.setBlock(x+10, y, z-3, blocktype)
mc.setBlock(x+14, y, z-2, blocktype)
mc.setBlock(x+12, y, z-2, blocktype)
mc.setBlock(x+10, y, z-2, blocktype)
mc.setBlock(x+14, y, z-1, blocktype)
mc.setBlock(x+12, y, z-1, blocktype)
mc.setBlock(x+11, y, z-1, blocktype)
mc.setBlock(x+10, y, z-1, blocktype)

#Produce letter "t" x+10, z+1 spaces infront of player

mc.setBlock(x+13, y, z, blocktype)
mc.setBlock(x+14, y, z+1, blocktype)
mc.setBlock(x+13, y, z+1, blocktype)
mc.setBlock(x+12, y, z+1, blocktype)
mc.setBlock(x+11, y, z+1, blocktype)
mc.setBlock(x+10, y, z+1, blocktype)
mc.setBlock(x+13, y, z+2, blocktype)

#Produce letter "i" x+10, z+4 spaces infront of player

mc.setBlock(x+14, y, z+4, blocktype)
mc.setBlock(x+12, y, z+4, blocktype)
mc.setBlock(x+11, y, z+4, blocktype)
mc.setBlock(x+10, y, z+4, blocktype)

#Produces letter "n" x+10, z+7 spaces infront of player

mc.setBlock(x+12, y, z+6, blocktype)
mc.setBlock(x+11, y, z+6, blocktype)
mc.setBlock(x+10, y, z+6, blocktype)
mc.setBlock(x+12, y, z+7, blocktype)
mc.setBlock(x+12, y, z+8, blocktype)
mc.setBlock(x+11, y, z+8, blocktype)
mc.setBlock(x+10, y, z+8, blocktype)
