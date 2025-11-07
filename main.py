import turtle 

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("lightyellow")
#s.tracer (0)


t.penup()
t.goto(-150, -100)
t.pendown()
t.pensize(4)
t.color('purple')
t.begin_fill()


for i in range(3):
    t.forward(300)
    t.left(90)
    t.forward(130)
    t.left(90)
t.begin_fill()


t.end_fill()
t.forward(300)
t.left(90)


#lingkaran
t.color('purple')
t.begin_fill()
t.circle(50, 180)
for i in range(2):
    t.left(180)
    t.circle(50, 180)
t.end_fill()


t.left(90)
t.forward(70)
t.right(90)


t.color('purple')
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(90)
    t.forward(160)
    t.left(90)
    
    
#Lingkaran
t.color('purple')
t.begin_fill()
for i in range(2):
    t.circle(40, 180)
    t.left(180)
t.end_fill()


t.right(90)
t.forward(160)
t.left(90)
t.forward(100)
t.right(90)
t.forward(70)


#Selamat ulang tahun yaa!!
t.color('purple')
t.penup()
t.goto(0, -175)
t.write('Selamat ulang tahun yaa!!', align='center', font="Times 35 normal")
turtle.done()