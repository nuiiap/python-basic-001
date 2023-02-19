import turtle as tl

tao = tl.Pen()
tao.shape('turtle')
x=0;y=0;
color="red"
for i in range (5):
    if i==0:
        x=100
        y=100
    elif i==1:
        y-=200
        color="green"
    elif i==2:
        x-=200
        color="blue"
    elif i==3:
        y+=200
        color="black"
    else:
        y=0;x=0
        color="pink"
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    tao.pencolor(color)
    tao.right(75)
    tao.forward(100)
    for i in range (4):
        tao.right(144)
        tao.forward(100)
    tao.setheading(90)
    tao.right(90)

tao.getscreen()._root.mainloop()