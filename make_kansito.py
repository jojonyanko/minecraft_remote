from mcje.minecraft import Minecraft
import param_MCJE as param

def make_kannsito(mc, x=1, z=1, y=76, sityuublock=param.GLOWSTONE, kahenblock=param.GLOWSTONE, zyouhenblock=param.GLOWSTONE ):

    blocktipe_sityu = sityuublock
    blocktipe_kahen = kahenblock
    blocktipe_zyouhen = zyouhenblock
    kudow = param.AIR

    mc.setBlocks(x * 28,1, z * 28,x * 16,y-1,z * 16, blocktipe_sityu)
    mc.setBlocks(x * 29,y,z * 29,x * 15,y,z * 15, blocktipe_kahen)
    mc.setBlocks(x * 28,y,z * 28,x * 16,y,z * 16, kudow)
    mc.setBlocks(x * 30,y+1,z * 30,x * 14,y+1,z * 14, blocktipe_kahen)
    mc.setBlocks(x * 29,y+1,z * 29,x * 15,y+1,z * 15, kudow)
    mc.setBlocks(x * 30,y+4,z * 30,x * 14,y+4,z * 14, blocktipe_zyouhen)
    mc.setBlocks(x * 29,y+4,z * 29,x * 15,y+4,z * 15, kudow)
    mc.setBlocks(x * 29,y+5,z * 29,x * 15,y+5,z * 15, blocktipe_zyouhen)
    mc.setBlocks(x * 28,y+5,z * 28,x * 16,y+5,z * 16, kudow)
    mc.setBlocks(x * 28,y+6,z * 28,x * 16,y+6,z * 16, blocktipe_zyouhen)