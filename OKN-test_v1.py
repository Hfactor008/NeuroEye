import time
import numpy as np
import turtle
import csv
import pdb
from datetime import datetime
import winsound
from playsound import playsound
import os


global path

path = "C:/Users/mm9rj/Desktop/Data"


system_time = []
coord1 = []
coord2 = []
coord3 = []
coord4 = []
coord5 = []





def HOtest(system_time): 
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("BANDIT Examination Simulator - OKN Test!")
    
    system_time = []
    coord1 = []
    coord2 = []
    coord3 = []
    coord4 = []
    coord5 = []

    
    sx = 960
    sy = 540
   
        

    wn.setup(width =0.98, height = 0.98, startx =1,starty =1)
    winsound.PlaySound('Ins_OKN.wav',winsound.SND_ALIAS)
    # wn.setup(width = 0.98,height = 0.98)

    s1 = turtle.Turtle()
    s1.hideturtle()
    s1.shape("square")
    s1.color("white")
    s1.hideturtle()
    s1.shapesize(20,5)
    s1.penup()
    s1.speed(0)
    s1.goto(-400,0)

    s2 = turtle.Turtle()
    s2.hideturtle()
    s2.shape("square")
    s2.color("white")
    s2.hideturtle()
    s2.shapesize(20,5)
    s2.penup()
    s2.speed(0)
    s2.goto(-600,0)

    s3 = turtle.Turtle()
    s3.hideturtle()
    s3.shape("square")
    s3.color("white")
    s3.hideturtle()
    s3.shapesize(20,5)
    s3.penup()
    s3.speed(0)
    s3.goto(-800,0)

    s4 = turtle.Turtle()
    s4.hideturtle()
    s4.shape("square")
    s4.color("white")
    s4.hideturtle()
    s4.shapesize(20,5)
    s4.penup()
    s4.speed(0)
    s4.goto(-1000,0)


    turtle.tracer(0,0)
    turtle.update()


    for i in range(4000):

        j = i - 400

        if j < 400:

            s1.showturtle()
            s1.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()

            

        elif j > 400 and j < 1200:

            k = j - 800

            s1.showturtle()
            s1.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 1200 and j < 2000:

            k = j - 1600

            s1.showturtle()
            s1.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2000 and j < 2800:

            k = j - 2400

            s1.showturtle()
            s1.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2800 and j < 3600:

            k = j - 3200

            s1.showturtle()
            s1.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        # Secound Bar
        j = i - 600

        if j < -400:
            
            s2.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()


        elif j > -400 and j < 400:

            s2.showturtle()
            s2.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 400 and j < 1200:

            k = j - 800

            s2.showturtle()
            s2.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 1200 and j < 2000:

            k = j - 1600

            s2.showturtle()
            s2.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2000 and j < 2800:

            k = j - 2400

            s2.showturtle()
            s2.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2800 and j < 3600:

            k = j - 3200

            s2.showturtle()
            s2.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        # Thrid Bar
        j = i - 800

        if j < -400:
            
            s3.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()


        elif j > -400 and j < 400:

            s3.showturtle()
            s3.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 400 and j < 1200:

            k = j - 800

            s3.showturtle()
            s3.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 1200 and j < 2000:

            k = j - 1600

            s3.showturtle()
            s3.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2000 and j < 2800:

            k = j - 2400

            s3.showturtle()
            s3.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2800 and j < 3600:

            k = j - 3200

            s3.showturtle()
            s3.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        # Fourth Bar
        j = i - 1000

        if j < -400:
            
            s4.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()


        elif j > -400 and j < 400:

            s4.showturtle()
            s4.goto(j,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 400 and j < 1200:

            k = j - 800

            s4.showturtle()
            s4.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 1200 and j < 2000:

            k = j - 1600

            s4.showturtle()
            s4.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2000 and j < 2800:

            k = j - 2400

            s4.showturtle()
            s4.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()

        elif j > 2800 and j < 3600:

            k = j - 3200

            s4.showturtle()
            s4.goto(k,0)
            turtle.tracer(0,0)
            turtle.update()
        
        system_time.append(datetime.timestamp(datetime.now()))

        Coordinate = np.array(s1.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord1.append(ScreenCoordinate)

        Coordinate = np.array(s2.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord2.append(ScreenCoordinate)

        Coordinate = np.array(s3.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord3.append(ScreenCoordinate)

        Coordinate = np.array(s4.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord4.append(ScreenCoordinate)

    turtle.tracer(0,0)
    turtle.update()



    


    s1.hideturtle()
    s2.hideturtle()
    s3.hideturtle()
    s4.hideturtle()

    winsound.Beep(1000, 2000)  # Beep at 1000 Hz for 100 ms
 
    
    
    turtle.tracer(0,0)





    for i in range(3800):

        j =  400 -i

        if j > -400:
            
            s1.showturtle()
            s1.goto(j,0)
            turtle.update()

        elif j < -400 and j > -1200:
    
            k = j + 800

            s1.showturtle()
            s1.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -1200 and j > -2000:
           
            k = j + 1600

            s1.showturtle()
            s1.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2000 and j > -2800:
            
            k = j + 2400

            s1.showturtle()
            s1.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2800 and j > -3600:
         
            k = j + 3200

            s1.showturtle()
            s1.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        # Secound Bar
        j =  600 -i

        if j > 400:

            s2.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()



        
        elif j < 400 and j > -400:
            
            s2.showturtle()
            s2.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()


        elif j < -400 and j > -1200:
    
            k = j + 800

            s2.showturtle()
            s2.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -1200 and j > -2000:
           
            k = j + 1600

            s2.showturtle()
            s2.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2000 and j > -2800:
            
            k = j + 2400

            s2.showturtle()
            s2.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2800 and j > -3600:
         
            k = j + 3200

            s2.showturtle()
            s2.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        # Thrid Bar
        j =  800 - i

        if j > 400:

            s3.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()



        
        elif j < 400 and j > -400:
            
            s3.showturtle()
            s3.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()


        elif j < -400 and j > -1200:
    
            k = j + 800

            s3.showturtle()
            s3.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -1200 and j > -2000:
           
            k = j + 1600

            s3.showturtle()
            s3.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2000 and j > -2800:
            
            k = j + 2400

            s3.showturtle()
            s3.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2800 and j > -3600:
         
            k = j + 3200

            s3.showturtle()
            s3.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        # Fourth Bar
        j =  1000 -i

        if j > 400:

            s4.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()



        
        elif j < 400 and j > -400:
            
            s4.showturtle()
            s4.goto(j,0)
            # turtle.tracer(0,0)
            turtle.update()


        elif j < -400 and j > -1200:
    
            k = j + 800

            s4.showturtle()
            s4.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -1200 and j > -2000:
           
            k = j + 1600

            s4.showturtle()
            s4.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2000 and j > -2800:
            
            k = j + 2400

            s4.showturtle()
            s4.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()

        elif j < -2800 and j > -3600:
         
            k = j + 3200

            s4.showturtle()
            s4.goto(k,0)
            # turtle.tracer(0,0)
            turtle.update()
        
        system_time.append(datetime.timestamp(datetime.now()))
        Coordinate = np.array(s1.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord1.append(ScreenCoordinate)

        Coordinate = np.array(s2.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord2.append(ScreenCoordinate)

        Coordinate = np.array(s3.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord3.append(ScreenCoordinate)

        Coordinate = np.array(s4.pos())
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord4.append(ScreenCoordinate)

    turtle.tracer(0,0)
    turtle.update()



    system_time = np.asarray(system_time)

    np.savetxt(os.path.join(path,'OKNTest_screentimestamp.csv'),system_time, delimiter='\t')
    np.savetxt(os.path.join(path,'OKNTest_screencoordimates1.csv'),coord1, delimiter='\t')
    np.savetxt(os.path.join(path,'OKNTest_screencoordimates2.csv'),coord2, delimiter='\t')
    np.savetxt(os.path.join(path,'OKNTest_screencoordimates3.csv'),coord3, delimiter='\t')
    np.savetxt(os.path.join(path,'OKNTest_screencoordimates4.csv'),coord4, delimiter='\t')

    print('OKN-Test Complete!!!')


    wn.bye()   

HOtest(system_time)