#import tobii_research as tr
#import pyrealsense2 as rs
import time
import numpy as np
import turtle
import csv
from datetime import datetime
import pdb
import msvcrt
import multiprocessing 







def Htest(): 
    coord = []
    system_time = []
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("H Test!")

    

    
    wn.setup(width = 0.98,height = 0.98)
    time.sleep(2)
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.shapesize(5,5)
    ball.penup()
    ball.speed(0)
    ball.goto(0,0)

    # Int data 
    x = 0
    y = 0
    # sx and sy should be measured based on screen dimension
    sx = 960
    sy = 540
    


    # Excuting H test
    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        x +=1
        
        system_time.append(str(datetime.now()))
       
        
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,sy))
        coord.append(ScreenCoordinate)
        #print(ScreenCoordinate)
        #BallPostition(i)=ball.position()


    #pdb.set_trace()
    #wn.tracer(8, 25)
    for i in range(400):
        
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        system_time.append(str(datetime.now()))
   
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        y -=1
        system_time.append(str(datetime.now()))
  
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)
        
    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    for i in range(1600):
        #ball.forward(i)
        ball.goto(x,y)
        x -=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        y -=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)
        
    for i in range(400):
        #ball.forward(i)
        ball.goto(x,y)
        y +=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,-sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    for i in range(800):
        #ball.forward(i)
        ball.goto(x,y)
        x +=1
        system_time.append(str(datetime.now()))
        Coordinate = np.array(ball.pos())
        
        ScreenCoordinate = np.abs(Coordinate+(sx,sy))
        coord.append(ScreenCoordinate)
        # print(ScreenCoordinate)

    coord = np.asarray(coord)
    np.savetxt('screentimestamp.csv',system_time, delimiter='\t', fmt='%s')
    np.savetxt('screencoordinates.csv',coord, delimiter='\t', fmt='%s')
    print('H-Test Complete!!!')

    wn.bye()


def eyetracker():
    found_eyetrackers = tr.find_all_eyetrackers()
    my_eyetracker = found_eyetrackers[0]

    L = []
    R = []
    Lp = []
    Rp = [] 
    system_time = []
    

    def gaze_data_callback(gaze_data):
 
        L.append(gaze_data['left_gaze_point_on_display_area'])
        R.append(gaze_data['right_gaze_point_on_display_area'])
        Lp.append(gaze_data['left_pupil_diameter'])
        Rp.append(gaze_data['right_pupil_diameter'])
       
        system_time.append(str(datetime.now()))
    

    my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA,  gaze_data_callback, as_dictionary=True)

    time.sleep(75)



    # input('Press Enter to Quit')
    my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA,  gaze_data_callback)

   
    

    L=np.asarray(L)
    R=np.asarray(R)
    #pdb.set_trace()
    GazeData = np.hstack([L,R])
    PupilData = np.vstack([Lp,Rp])
    np.savetxt('gazetimestamp.csv',system_time, delimiter='\t', fmt='%s')
    np.savetxt('gazedata.csv',GazeData, delimiter='\t')
    np.savetxt('pupildata.csv',PupilData.T, delimiter='\t')
    print('Gaze Tracking successful!')



def realsense():

    pipeline = rs.pipeline()
    #mf= rs.motion_frame
    config = rs.config()
    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.infrared, 1280, 720, rs.format.y8, 30)
    config.enable_stream(rs.stream.accel)
    config.enable_stream(rs.stream.gyro)
    config.enable_record_to_file('realsensedata.bag')
    # Start streaming
    pipeline.start(config)
    timeout = time.time() + 60*1.25   # 75 secounds


    while True:

            # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        infrared_frame = frames.get_infrared_frame()
       


        if time.time() > timeout:
            print('Real Sensing successful!')
            break
    
   



if __name__ == "__main__":

#    p1 = multiprocessing.Process(target=eyetracker) 
#    p2 = multiprocessing.Process(target=realsense) 
    p3 = multiprocessing.Process(target=Htest) 
#    p1.start()
#    p2.start()
    p3.start()
 

  
    # # wait until process 1 is finished 
#    p1.join() 
    # # wait until process 2 is finished 
#    p2.join() 
    p3.join() 



