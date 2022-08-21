from mcje.minecraft import Minecraft
import param_MCJE as param

def make_kannsito(mc, x=1, z=1, sityuublock=param.GLOWSTONE, kahenblock=param.GLOWSTONE, zyouhenblock=param.GLOWSTONE ):

    blocktipe_sityu = sityuublock
    blocktipe_kahen = kahenblock
    blocktipe_zyouhen = zyouhenblock
    kudow = param.AIR

    mc.setBlocks(x * 28,1, z * 28,x * 16,75,z * 16, blocktipe_sityu)
    mc.setBlocks(x * 29,76,z * 29,x * 15,76,z * 15, blocktipe_kahen)
    mc.setBlocks(x * 28,76,z * 28,x * 16,76,z * 16, kudow)
    mc.setBlocks(x * 30,77,z * 30,x * 14,77,z * 14, blocktipe_kahen)
    mc.setBlocks(x * 29,77,z * 29,x * 15,77,z * 15, kudow)
    mc.setBlocks(x * 30,80,z * 30,x * 14,80,z * 14, blocktipe_zyouhen)
    mc.setBlocks(x * 29,80,z * 29,x * 15,80,z * 15, kudow)
    mc.setBlocks(x * 29,81,z * 29,x * 15,81,z * 15, blocktipe_zyouhen)
    mc.setBlocks(x * 28,81,z * 28,x * 16,81,z * 16, kudow)
    mc.setBlocks(x * 28,82,z * 28,x * 16,82,z * 16, blocktipe_zyouhen)