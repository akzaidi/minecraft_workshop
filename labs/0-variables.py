from mcpi import minecraft

## Modify the following to the address provided by the instructor and your username
server_address = "40.112.53.114"
username = "azaidi"

mc = minecraft.Minecraft.create(address=server_address, name=username)
pos = mc.player.getPos()
print pos

## Teleport
## We'll create three variables with positions stored to where we want to move to

x = 10 
y = 110 
z = 12

mc.player.setTilePos(x, y, z)