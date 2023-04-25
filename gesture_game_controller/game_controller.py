import pgzrun

WIDTH = 800
HEIGHT = 600

player = Actor("spiderman", center = (400, 300))

def update():
    if keyboard.left:
        player.x -= 5
        player.angle = 10
    elif keyboard.right:
        player.x += 5
        player.angle = -10
    elif keyboard.up:
        player.y -= 5
    elif keyboard.down:
        player.y += 5
    
    else:
        player.angle = 0

def draw():
    screen.fill("Grey")
    player.draw()

pgzrun.go()
