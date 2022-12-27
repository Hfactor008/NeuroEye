import time
import numpy as np
import turtle
import csv
import pdb
from datetime import datetime
import winsound
from playsound import playsound
#winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 100 ms




system_time = []
coord = []



def HOtest(coord,system_time): 
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("BANDIT Examination Simulator - Dot Test!")

    

    
    wn.setup(width = 0.98,height = 0.98)
    winsound.PlaySound('Ins_Dot.wav',winsound.SND_ALIAS)
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(4,4)
    ball.penup()
    
    ball.goto(0,0)
    #turtle.tracer(0,0)

    tspeed = 2
    tspeed_t = 0.3
    # Int data 
    x = 0
    y = 0

    sx = 960
    sy = 540



    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)



    ball.hideturtle()
    ball.goto(-860,440)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 2


    ball.hideturtle()
    ball.goto(400,180)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 3


    ball.hideturtle()
    ball.goto( -400,-180)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 4


    ball.hideturtle()
    ball.goto( 850,-400)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 5
 
    ball.hideturtle()
    ball.goto( 850,400)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 6


    ball.hideturtle()
    ball.goto( -400,180)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 7
 

    ball.hideturtle()
    ball.goto( -860,-400)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)

    # dot 8


    ball.hideturtle()
    ball.goto( 400, -180)
    ball.showturtle()
    Coordinate = np.array(ball.pos())    
    ScreenCoordinate = np.abs(Coordinate+(sx,sy))
    coord.append(ScreenCoordinate)
    system_time.append(str(datetime.now()))
    time.sleep(tspeed)
    system_time.append(str(datetime.now()))



 

    np.savetxt('Dot-screentimestamp.csv',system_time, delimiter='\t', fmt='%s')
    np.savetxt('Dot-screencoordimates.csv',coord, delimiter='\t', fmt='%s')

    wn.bye()   

HOtest(coord,system_time)