import mcpi.minecraft as minecraft

# Connect to minecraft server 127.0.0.1 as player 'steve'
server_address = "40.112.53.114"
username = "azaidi"
mc = minecraft.Minecraft.create(address=server_address, name=username)

block_id = 57

pos = mc.player.getPos()

pyramid_height = 10

for i in range(pyramid_height):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + (pyramid_height*2) - 2 - (i*2)
    y2 = y
    z2 = z + (pyramid_height*2) - 2 - (i*2)
    mc.setBlocks(x, y, z, x2, y2, z2, block_id)
