from turtle import *
speed('slowest')

for i in range(6):
    fd(100)
    lt(360/6)
    write(i, font=('Arial', 12, 'normal'))
    circle(60)

mainloop()