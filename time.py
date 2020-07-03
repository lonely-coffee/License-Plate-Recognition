import turtle,time

def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawLine(flag):
    drawgap()
    turtle.pendown() if flag else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.penup()
    turtle.left(180)
    turtle.fd(40)

def drawDate(date):
    for i in date:
        if i is '-':
            writeChar("年",g=1)
        elif i is '=':
            writeChar("月",b=1)
        elif i is '+':
            writeChar("日")
        else:
            drawDigit(eval(i))

def writeChar(char,r=0,g=0,b=0):
    turtle.write(char,font=("Arial",18,"normal"))
    turtle.pencolor(r,g,b)
    turtle.fd(40)

def main():
    turtle.setup(1200,350)
    turtle.speed(0)
    turtle.penup()
    turtle.fd(-450)
    turtle.pensize(5)
    t=time.gmtime()
    ft=time.strftime("%Y-%m=%d+",t)
    print(ft)
    turtle.pencolor(1,0,0)
    drawDate(ft)
    turtle.hideturtle()
    turtle.down()

main()
