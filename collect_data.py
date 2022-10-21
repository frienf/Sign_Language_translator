import cv2
import os

def makedir(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)
    return None
  else:
      pass


cap = cv2.VideoCapture(0)
i = 0
image_count = 0
while i<108:
  ret,frame = cap.read()
  frame = cv2.flip(frame,1)
  roi = frame[100:400,320:620]
  cv2.imshow('roi',roi)
  gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray,(5,5),2)
  th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  ret, test_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  test_image = cv2.resize(test_image,(64,64))
  cv2.imshow('roi scaled and gray',test_image)
  copy = frame.copy()
  cv2.rectangle(copy,(320,100),(620,400),(255,0,0),5)
  if i == 0:
    image_count=0
    cv2.putText(copy,'Hit Enter to record when ready to record A gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
  if i == 1:
    image_count+=1
    cv2.putText(copy,'Record A gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/A/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 2:
    image_count+=1
    cv2.putText(copy,'Record B gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/A/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 3:
    cv2.putText(copy,'Hit Enter to record when ready to Record B gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
  if i == 4:
    image_count+=1
    cv2.putText(copy,'Record B gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/B/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 5:
    image_count+=1
    cv2.putText(copy,'Record B gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/B/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 6:
    cv2.putText(copy,'Hit Enter to record when ready to Record C gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)  
  if i == 7:
    image_count+=1
    cv2.putText(copy,'Record C gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/C/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 8:
    image_count+=1
    cv2.putText(copy,'Record C gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/C/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 9:
    cv2.putText(copy,'Hit Enter to record when ready to Record D gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 10:
    image_count+=1
    cv2.putText(copy,'Record D gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/D/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 11:
    image_count+=1
    cv2.putText(copy,'Record D gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/D/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 12:
    cv2.putText(copy,'Hit Enter to record when ready to Record E gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 13:
    image_count+=1
    cv2.putText(copy,'Record E gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/E/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 14:
    image_count+=1
    cv2.putText(copy,'Record E gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/E/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 15:
    cv2.putText(copy,'Hit Enter to record when ready to Record F gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 16:
    image_count+=1
    cv2.putText(copy,'Record F gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/F/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 17:
    image_count+=1
    cv2.putText(copy,'Record F gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/F/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 18:
    cv2.putText(copy,'Hit Enter to record when ready to Record G gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 19:
    image_count+=1
    cv2.putText(copy,'Record G gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/G/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 20:
    image_count+=1
    cv2.putText(copy,'Record G gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/G/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 21:
    cv2.putText(copy,'Hit Enter to record when ready to Record H gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 22:
    image_count+=1
    cv2.putText(copy,'Record H gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/H/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 23:
    image_count+=1
    cv2.putText(copy,'Record H gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/H/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 24:
    cv2.putText(copy,'Hit Enter to record when ready to Record I gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 25:
    image_count+=1
    cv2.putText(copy,'Record I gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/I/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 26:
    image_count+=1
    cv2.putText(copy,'Record I gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/I/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 27:
    cv2.putText(copy,'Hit Enter to record when ready to Record J gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 28:
    image_count+=1
    cv2.putText(copy,'Record J gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/J/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 29:
    image_count+=1
    cv2.putText(copy,'Record J gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/j/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 30:
    cv2.putText(copy,'Hit Enter to record when ready to Record K gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 31:
    image_count+=1
    cv2.putText(copy,'Record K gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/K/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 32:
    image_count+=1
    cv2.putText(copy,'Record K gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/K/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 33:
    cv2.putText(copy,'Hit Enter to record when ready to Record L gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 34:
    image_count+=1
    cv2.putText(copy,'Record L gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/L/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 35:
    image_count+=1
    cv2.putText(copy,'Record L gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/L/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 36:
    cv2.putText(copy,'Hit Enter to record when ready to Record M gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 37:
    image_count+=1
    cv2.putText(copy,'Record M gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/M/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 38:
    image_count+=1
    cv2.putText(copy,'Record M gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/M/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 39:
    cv2.putText(copy,'Hit Enter to record when ready to Record N gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 40:
    image_count+=1
    cv2.putText(copy,'Record N gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/N/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 41:
    image_count+=1
    cv2.putText(copy,'Record N gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/N/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 42:
    cv2.putText(copy,'Hit Enter to record when ready to Record O gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 43:
    image_count+=1
    cv2.putText(copy,'Record O gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/O/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 44:
    image_count+=1
    cv2.putText(copy,'Record O gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/O/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 45:
    cv2.putText(copy,'Hit Enter to record when ready to Record P gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 46:
    image_count+=1
    cv2.putText(copy,'Record P gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/P/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 47:
    image_count+=1
    cv2.putText(copy,'Record P gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/P/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 48:
    cv2.putText(copy,'Hit Enter to record when ready to Record Q gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 49:
    image_count+=1
    cv2.putText(copy,'Record Q gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/Q/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 50:
    image_count+=1
    cv2.putText(copy,'Record Q gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/Q/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 51:
    cv2.putText(copy,'Hit Enter to record when ready to Record R gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 52:
    image_count+=1
    cv2.putText(copy,'Record R gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/R/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 53:
    image_count+=1
    cv2.putText(copy,'Record R gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/R/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 54:
    cv2.putText(copy,'Hit Enter to record when ready to Record S gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 55:
    image_count+=1
    cv2.putText(copy,'Record S gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/S/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 56:
    image_count+=1
    cv2.putText(copy,'Record S gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/S/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 57:
    cv2.putText(copy,'Hit Enter to record when ready to Record T gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 58:
    image_count+=1
    cv2.putText(copy,'Record T gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/T/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 59:
    image_count+=1
    cv2.putText(copy,'Record T gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/T/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 60:
    cv2.putText(copy,'Hit Enter to record when ready to Record U gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 61:
    image_count+=1
    cv2.putText(copy,'Record U gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/U/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 62:
    image_count+=1
    cv2.putText(copy,'Record U gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/U/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 63:
    cv2.putText(copy,'Hit Enter to record when ready to Record V gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 64:
    image_count+=1
    cv2.putText(copy,'Record V gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/V/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 65:
    image_count+=1
    cv2.putText(copy,'Record V gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/V/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 66:
    cv2.putText(copy,'Hit Enter to record when ready to Record W gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 67:
    image_count+=1
    cv2.putText(copy,'Record W gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/W/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 68:
    image_count+=1
    cv2.putText(copy,'Record W gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/W/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 69:
    cv2.putText(copy,'Hit Enter to record when ready to Record X gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 70:
    image_count+=1
    cv2.putText(copy,'Record X gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/X/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 71:
    image_count+=1
    cv2.putText(copy,'Record X gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/X/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 72:
    cv2.putText(copy,'Hit Enter to record when ready to Record Y gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 73:
    image_count+=1
    cv2.putText(copy,'Record Y gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/Y/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 74:
    image_count+=1
    cv2.putText(copy,'Record Y gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/Y/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 75:
    cv2.putText(copy,'Hit Enter to record when ready to Record Z gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 76:
    image_count+=1
    cv2.putText(copy,'Record Z gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/Z/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 77:
    image_count+=1
    cv2.putText(copy,'Record Z gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/Z/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 78:
    cv2.putText(copy,'Hit Enter to record when ready to Record 0 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 79:
    image_count+=1
    cv2.putText(copy,'Record 0 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/0/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 80:
    image_count+=1
    cv2.putText(copy,'Record 0 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/0/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 81:
    cv2.putText(copy,'Hit Enter to record when ready to Record 1 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 82:
    image_count+=1
    cv2.putText(copy,'Record 1 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/1/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 83:
    image_count+=1
    cv2.putText(copy,'Record 1 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/1/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 84:
    cv2.putText(copy,'Hit Enter to record when ready to Record 2 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 85:
    image_count+=1
    cv2.putText(copy,'Record 2 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/2/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 86:
    image_count+=1
    cv2.putText(copy,'Record 2 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/2/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 87:
    cv2.putText(copy,'Hit Enter to record when ready to Record 3 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 88:
    image_count+=1
    cv2.putText(copy,'Record 3 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/3/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 89:
    image_count+=1
    cv2.putText(copy,'Record 3 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/3/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 90:
    cv2.putText(copy,'Hit Enter to record when ready to Record 4 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 91:
    image_count+=1
    cv2.putText(copy,'Record 4 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/4/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 92:
    image_count+=1
    cv2.putText(copy,'Record 4 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/4/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 93:
    cv2.putText(copy,'Hit Enter to record when ready to Record 5 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 94:
    image_count+=1
    cv2.putText(copy,'Record 5 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/5/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 95:
    image_count+=1
    cv2.putText(copy,'Record 5 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/5/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 96:
    cv2.putText(copy,'Hit Enter to record when ready to Record 6 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 97:
    image_count+=1
    cv2.putText(copy,'Record 6 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/6/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 98:
    image_count+=1
    cv2.putText(copy,'Record 6 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/6/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 99:
    cv2.putText(copy,'Hit Enter to record when ready to Record 7 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 100:
    image_count+=1
    cv2.putText(copy,'Record 7 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/7/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 101:
    image_count+=1
    cv2.putText(copy,'Record 7 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/7/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 102:
    cv2.putText(copy,'Hit Enter to record when ready to Record 8 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 103:
    image_count+=1
    cv2.putText(copy,'Record 8 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/8/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 104:
    image_count+=1
    cv2.putText(copy,'Record 8 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/8/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)
  if i == 105:
    cv2.putText(copy,'Hit Enter to record when ready to Record 9 gesture',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)    
  if i == 106:
    image_count+=1
    cv2.putText(copy,'Record 9 gesture -Train',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/train/9/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)  
  if i == 107:
    image_count+=1
    cv2.putText(copy,'Record 9 gesture -Test',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    cv2.putText(copy,str(image_count),(400,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    gesture_one ='./handgesture/test/9/'
    makedir(gesture_one)
    cv2.imwrite(gesture_one+str(image_count)+".jpg",test_image)   
  if i == 108:
    cv2.putText(copy,"Hit Enter to Exit",(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
  cv2.imshow('frame',copy)

  if cv2.waitKey(1) == 13:
    image_count=0
    i+=1

cap.release()
cv2.destroyAllWindows()
