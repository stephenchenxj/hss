import RPi.GPIO as GPIO
import time

#import datetime
#myDateTime = datetime.datetime.now()
#print (myDateTime)





import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
COMMASPACE =', '

from picamera import PiCamera
camera = PiCamera()
camera.resolution = (640,480)
    
    


def send_email(dateTimeStr):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("hs.diy.sf@gmail.com", "specialforce")
    
    msg_full = MIMEMultipart()
    msg_full['Subject'] = 'Door Open'
    msg_full['From'] = 'hs.diy.sf@gmail.com'
    msg_full['To'] = 'chentju@hotmail.com'
     
    image_name = dateTimeStr+'.jpg'
    with open(image_name, 'rb') as fp:
        img = MIMEImage(fp.read())
        msg_full.attach(img)
    
    #msg = "YOUR MESSAGE!"    
    #server.sendmail("hs.diy.sf@gmail.com ", "chentju@hotmail.com", msg)
    server.send_message(msg_full)
    server.quit()


def save_video(dateTimeStr):
    file_name = dateTimeStr + '.h264'
    
    camera.start_recording( file_name )
    time.sleep(35)
    camera.stop_recording()
    
def capture_image(dateTimeStr):
    file_name = dateTimeStr + '.jpg'
    camera.capture(file_name)
    


input_pin_no = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_pin_no, GPIO.IN)


while(1):
    if GPIO.input(input_pin_no)== 1:
        print ('Door is opened!')
        dateTimeStr = time.strftime("%Y-%m-%d-%H:%M:%S")
        #print (dateTimeStr)
        capture_image(dateTimeStr)
        
        #need to add error handling here: what if no network, program will hang here
        #send_email(dateTimeStr)
        
        save_video(dateTimeStr)
        
        
        time.sleep(1)
    elif GPIO.input(input_pin_no) == 0:
        print ('Door is closed!')
        time.sleep(1)
        