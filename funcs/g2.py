import pgzrun

WIDTH = 800
HEIGHT = 500

square = Rect((400,250), (50,50))
square2 = Rect((500,300), (40,100))

b_vx = 4 # global variable

def draw():
    screen.clear()
    screen.draw.filled_rect(square, 'red')
    screen.draw.filled_rect(square2, 'yellow')

def update():
    global b_vx # this allows us to change the value of b_vx
    # loop around the screen
    square.x += 2
    if square.x > WIDTH:
        square.x = 0
    #bounce the box
    square2.x += b_vx
    if square2.right> WIDTH or square2.left < 0:
        b_vx = -b_vx # invert the direction of box

pgzrun.go()