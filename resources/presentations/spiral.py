import turtle

colors = ['red', 'green', 'purple', 'green', 'yellow', 'orange']

t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[ x % len(colors) ])
	t.width(x/100+1)
	t.forward(x)
	t.left(59)

input()
