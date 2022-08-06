from mcje.minecraft import Minecraft
import param_MCJE as param

def make_kannsito(mc, x=1):
    mc.setBlocks(x * 28,1,x * 28,x * 16,75,x * 16, param.GLOWSTONE)
    mc.setBlocks(x * 29,76,x * 29,x * 15,76,x * 15, param.GLOWSTONE)
    mc.setBlocks(x * 28,76,x * 28,x * 16,76,x * 16, param.AIR)
    mc.setBlocks(x * 30,77,x * 30,x * 14,77,x * 14, param.GLOWSTONE)
    mc.setBlocks(x * 29,77,x * 29,x * 15,77,x * 15, param.AIR)
    mc.setBlocks(x * 30,80,x * 30,x * 14,80,x * 14, param.GLOWSTONE)
    mc.setBlocks(x * 29,80,x * 29,x * 15,80,x * 15, param.AIR)
    mc.setBlocks(x * 29,81,x * 29,x * 15,81,x * 15, param.GLOWSTONE)
    mc.setBlocks(x * 28,81,x * 28,x * 16,81,x * 16, param.AIR)
    mc.setBlocks(x * 28,82,x * 28,x * 16,82,x * 16, param.GLOWSTONE)