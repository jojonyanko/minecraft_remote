# jo

from mcje.minecraft import Minecraft
import param_MCJE as param

import axis_flat
import make_kansito

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo3")

mc.postToChat("こんにちは！")

# axis_flat.reset_minecraft_world(mc, width=50)
# mc.setBlocks(-50,1,-50,50,111,50,param.GLASS)



mc.setBlocks(-49,0,-49,49,200,49,param.AIR)


# mc.setBlocks(-10,1,-10,10,100,10,param.GLASS)
# mc.setBlocks(-9,1,-9,9,99,9,param.GOLD_BLOCK)


# x = 49
# z = 4

# y = 1
# for i in range(6):
    
#     mc.setBlocks(x, y ,-z,-x,y + 7,z,param.GLASS)
#     mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

#     mc.setBlocks(-z, y ,x,z,y + 7,-x,param.GLASS)
#     mc.setBlocks(-(z - 2), y + 1 ,x,z - 2,y + 6,-x,param.AIR)
#     mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

#     y += 20

# y = 1
# for j in range(5):
#     x = 48
#     z = -5
#     for i in range(10):
#         mc.setBlocks(-x,y,z,-(x - 4),y + 1,z - 3,param.GLASS)
#         y += 1
#         z -= 4

#     for i in range(10):
#         mc.setBlocks(-x,y,z,-(x - 4),y + 1,z - 3,param.GLASS)
#         y += 1
#         x -= 5

# mc.setBlocks(-3,2,-3,3,100,3,param.AIR)
# mc.setBlocks(-2,100,-2,2,101,2,param.AIR)

# x = -3
# y = 1
# z = -3

# for j in range(4):
#     for i in range(6):
#         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#         x += 1
#         y += 1

#     for i in range(6):
#         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#         z += 1
#         y += 1

#     for i in range(6):
#         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#         x -= 1
#         y += 1

#     for i in range(6):
#         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#         z -= 1
#         y += 1

# z += 1
# x += 1

# for i in range(5):
#     mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#     x += 1
#     y += 1

make_kansito.make_kannsito(mc, x= -1, z= -1)
make_kansito.make_kannsito(mc, x=1, z=1, y=5)
mc.postToChat("無駄無駄無駄無駄ぁあ！！無駄なんだよジョジョォォォ！！！")
make_kansito.make_kannsito(mc, x= -1, Z=1)
make_kansito.make_kannsito(mc, x=1, Z= -1)