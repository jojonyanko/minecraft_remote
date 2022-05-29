# jo

from mcje.minecraft import Minecraft
import param_MCJE as param

import axis_flat

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo3")

mc.postToChat("こんにちは！")

axis_flat.reset_minecraft_world(mc, width=100)
axis_flat.clear_XYZ_axis(mc, wait=0)
axis_flat.draw_XYZ_axis(mc, wait=1)