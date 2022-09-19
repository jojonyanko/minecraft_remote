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

def make_honto(mc,x= 10,y=100,z= 10,tyusinblock=param.GOLD_BLOCK):
    blocktipe_tyuusin = tyusinblock

    mc.setBlocks(x,1,z,-x,y,-z,param.GLASS)
    mc.setBlocks(x-1,1,z-1,-(x-1),y-1,-(z-1),blocktipe_tyuusin)

def make_kaidow(mc,x=49,y=1,z=4,y_plas=20,kaidowblock=param.GLASS):
    blocktipe_kaidow=kaidowblock
    for i in range(6):
        
        mc.setBlocks(x, y ,-z,-x,y + 7,z,blocktipe_kaidow)
        mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

        mc.setBlocks(-z, y ,x,z,y + 7,-x,blocktipe_kaidow)
        mc.setBlocks(-(z - 2), y + 1 ,x,z - 2,y + 6,-x,param.AIR)
        mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

        y += y_plas

def make_outkaidan(mc,x=48,y=1,z=-5,outkaidanblock=param.GLASS):
    blocktipe_outkaidan=outkaidanblock
    use_y=y
    for j in range(5):
        use_x=x
        use_z=z
        for i in range(10):
            mc.setBlocks(-use_x,use_y,use_z,-(use_x - 4),use_y + 1,use_z - 3,blocktipe_outkaidan)
            use_y += 1
            use_z -= 4

        for i in range(10):
            mc.setBlocks(-use_x,use_y,use_z,-(use_x - 4),use_y + 1,use_z - 3,blocktipe_outkaidan)
            use_y += 1
            use_x -= 5

def make_insidekaidan_seihoukei_zyouhen(mc,x= -3,y=1,z= -3,dansu=6,insideblock_seihoukei_zyouhen=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_zyouhen = insideblock_seihoukei_zyouhen
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_zyouhen)
            use_x += 1
            use_y += 1

def make_insidekaidan_seihoukei_migi(mc,x=3,y=7,z= -3,dansu=6,insideblock_seihoukei_migi=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_migi = insideblock_seihoukei_migi
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_migi)
            use_z += 1
            use_y += 1

def make_insidekaidan_seihoukei_kahen(mc,x=3,y=13,z=3,dansu=6,insideblock_seihoukei_kahen=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_kahen = insideblock_seihoukei_kahen
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_kahen)
            use_x -= 1
            use_y += 1

def make_insidekaidan_seihoukei_hidari(mc,x=-3,y=1,z=3,dansu=6,insideblock_seihoukei_hidari=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_kahen = insideblock_seihoukei_hidari
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_kahen)
            use_z -= 1
            use_y += 1

def make_insidekaidan(mc,x=-3,y=1,z=-3,dansu=6,insideblock=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock=insideblock
    use_x = x
    use_y = y
    use_z = z
    for j in range(4):

        make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_zyouhen=insideblock)

        use_x += dansu
        use_y += dansu

        make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_migi=insideblock)

        use_z += dansu
        use_y += dansu

        make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_kahen=insideblock)

        use_x -= dansu
        use_y += dansu

        make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_hidari=insideblock)

        use_z -= dansu
        use_y += dansu
    
    use_z += 1
    use_x += 1

    make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu - 1,insideblock_seihoukei_zyouhen=insideblock)