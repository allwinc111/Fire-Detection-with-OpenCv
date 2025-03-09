import cv2
import threading
import playsound
import smtplib

fire_cascade = cv2.CascadeClassifier('cascade.xml') 
vid = cv2.VideoCapture(0)
runOnce = False  

def play_alarm_sound_function():
    playsound.playsound('Fire_alarm.mp3', block=False)  
    print("Fire alarm end") 

def send_mail_function():  
    global runOnce
    recipient_mail = "allwinc111@gmail.com"  
    sender_mail = "allwinc111@gmail.com"
    sender_password = "Allwin@2905"  

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail, recipient_mail, "Warning: Fire detected!")  
        print(f"Alert mail sent successfully to {recipient_mail}")  
        server.quit()
        runOnce = True  # Ensure it's set after sending mail
        
    except Exception as e:
        print(f"Error sending mail: {e}")  

while True:
    ret, frame = vid.read()  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)  

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
        
        print("Fire alarm initiated")
        threading.Thread(target=play_alarm_sound_function).start()  

        if not runOnce:
            print("Mail send initiated")
            threading.Thread(target=send_mail_function).start()  

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
