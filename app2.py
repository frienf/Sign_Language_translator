from keras.models import load_model,model_from_json
import cv2 as cv2
import numpy as np
import operator
import sys, os
directory='model_5_99/'
json_file = open(directory+"model-bw_17.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights(directory+"model-bw_17.h5")
json_file_k = open(directory+"model-bw_k.json" , "r")
model_json_k = json_file_k.read()
json_file_k.close()
loaded_model_k = model_from_json(model_json_k)
loaded_model_k.load_weights(directory+"model-bw_k.h5")
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
  result_k = loaded_model_k.predict(test_image.reshape(1 , 64 , 64 , 1))
  prediction={'A':result[0][0],
              'B':result[0][1],
              'D':result[0][2],
              'E':result[0][3],
              'F':result[0][4],
              'G':result[0][5],
              'H':result[0][6],
              'I':result[0][7],
              'K':result[0][8],
              'L':result[0][9],
              'N':result[0][10],
              'O':result[0][11],
              'P':result[0][12],
              'U':result[0][13],
              'V':result[0][14],
              'W':result[0][15],
              'Y':result[0][16]}          
  prediction=sorted(prediction.items(),key=operator.itemgetter(1),reverse=True)
  current_predict = prediction[0][0]
      #LAYER 2
  if(current_predict == 'B' or current_predict == 'F' or current_predict == 'K'or current_predict == 'V'or current_predict == 'W'):
      prediction = {}
      prediction['B'] = result_k[0][0]
      prediction['F'] = result_k[0][1]
      prediction['K'] = result_k[0][2]
      prediction['V'] = result_k[0][3]
      prediction['W'] = result_k[0][4]
      prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
      current_predict = prediction[0][0]
      
  cv2.putText(copy,current_predict,(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0,2))
  #cv2.putText(copy,saveLetter(result),(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0,2))
  cv2.imshow('frame',copy)

  if cv2.waitKey(1) == 13:
    break

cap.release()
cv2.destroyAllWindows()
