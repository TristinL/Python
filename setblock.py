from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
mc.setBlock(pos.x-1, pos.y, pos.z, 10)
mc.setBlock(pos.x+1, pos.y, pos.z, 10)
mc.setBlock(pos.x, pos.y, pos.z-1, 10)
mc.setBlock(pos.x, pos.y, pos.z+1, 10)


mc.setBlock(pos.x+10, pos.y, pos.z, 8)
mc.player.setTilePos(pos.x+10, pos.y+35, pos.z)

