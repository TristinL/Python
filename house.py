from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
from mcpi import block


mc.player.setPos(55, 60, 55)

mc.setBlocks(50, 59, 50, 60, 59, 60, 35)

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

time.sleep(5)

#for reference to blocktypes look up "help(mcpi.block)"
mc.setBlocks(x-6, y-1, z+6, x-6, y+5, z-6, block.BRICK_BLOCK)
mc.setBlocks(x+6, y-1, z-6, x+6, y+5, z+6, block.BRICK_BLOCK)
mc.setBlocks(x-6, y-1, z-6, x+6, y+5, z-6, block.BRICK_BLOCK)
mc.setBlocks(x+6, y-1, z+6, x-6, y+5, z+6, block.BRICK_BLOCK)

mc.setBlocks(x-6, y, z, x-6, y+1 ,z, block.DOOR_WOOD)
