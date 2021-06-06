from guizero import App, PushButton
from picamera import PiCamera
from time import sleep

pic_idx = 1
mov_idx = 1
camera = PiCamera()
turn_on = False
recording = False

def power_switch():
    global turn_on    
    if turn_on:        
        camera.stop_preview()
        turn_on = False
        power_switch_button.text = 'Turn On'        
    else:        
        camera.start_preview(alpha=200)
        turn_on = True
        power_switch_button.text = 'Turn Off'        
    
def take_a_picutre():
    global pic_idx    
    camera.capture('/home/pi/Desktop/pic%s.jpg' % pic_idx)
    pic_idx += 1    
    
def record_movie():
    global recording
    global mov_idx    
    if recording:        
        camera.stop_recording()
        recording = False
        record_movie_button.text = 'Start Recording'        
    else:        
        camera.start_recording('/home/pi/Desktop/mov%s.h264' % mov_idx)
        mov_idx += 1
        recording = True
        record_movie_button.text = 'Stop Recording'        

app = App(title="My Camera")

power_switch_button = PushButton(app, command=power_switch, text="Turn On")
take_picture_button = PushButton(app, command=take_a_picutre, text="Take a picture")
record_movie_button = PushButton(app, command=record_movie, text="Start Recording")

app.display()
