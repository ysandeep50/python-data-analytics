from turtle import *
speed('slowest')
pencolor('yellow')
bgcolor('black')
s = 8
d = 100
for i in range(s):
    fd(100)
    lt(360/s)
    write(i, font=('Arial', 12, 'normal'))
    dot(360/s)

mainloop()