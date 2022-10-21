from keras.models import load_model,model_from_json
import cv2 as cv2
import numpy as np
import operator
import sys, os
directory='model_5_99/'
json_file = open(directory+"model-bw_digit.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights(directory+"model-bw_digit.h5")
print("Loaded model from disk")
#categories = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE',6:'SIX',7:'SEVEN',8:'EIGHT',9:'NINE',A:'A',B:'B',C:'C',D:'D',E:'E',F:'F',G:'G',H:'H',I:'I',J:'J',K:'K',L:'L',M:'M',N:'N',O:'O',P:'P',Q:'Q',R:'R',S:'S',T:'T',U:'U',V:'V',W:'W',X:'X',Y:'Y',Z:'Z'}

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()
  frame = cv2.flip(frame,1)
  roi = frame[100:400,320:620]
  cv2.imshow('roi',roi)
  gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray,(5,5),2)
  th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
  ret, test_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
  test_image = cv2.resize(test_image,(64,64))
  cv2.imshow('roi scaled and grey',test_image)
  copy = frame.copy()
  cv2.rectangle(copy,(320,100),(620,400),(255,0,0),5)
  roi=roi/255
  result = loaded_model.predict(test_image.reshape(1,64,64,1))
  prediction={'1':result[0][0],
              '2':result[0][1],
              '3':result[0][2],
              '4':result[0][3],
              '5':result[0][4],
              '6':result[0][5],
              '7':result[0][6],
              '8':result[0][7],
              '9':result[0][8],}          
  prediction=sorted(prediction.items(),key=operator.itemgetter(1),reverse=True)
  current_predict = prediction[0][0]
  cv2.putText(copy,current_predict,(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0,2))  
  cv2.imshow('frame',copy)

  if cv2.waitKey(1) == 13:
    break

cap.release()
cv2.destroyAllWindows()
