import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization
from keras.layers import GlobalAveragePooling1D
from keras.layers import Conv1D, MaxPooling1D, LSTM
from keras.layers import TimeDistributed
from sklearn.metrics import confusion_matrix
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
import numpy as np
import itertools
import glob
import os
import json
import sys
import time
import statistics

#dictionary mapping classes to asanas
asanas = {0:'bhujangasana', 1:'padamasana', 2:'shavasana', 3:'tadasana', 4:'trikonasana', 5:'vrikshasana', 6:'yo'}


# returns the keras model
def get_model():
    model = Sequential([
        TimeDistributed(Conv1D(16,3, activation='relu', padding = "same"),input_shape=[10,33,2]),
        TimeDistributed(BatchNormalization()),
        #TimeDistributed(MaxPooling1D()),
        TimeDistributed(Dropout(0.5)),
        #TimeDistributed(Conv1D(64,3, activation='relu',padding = "same")),
        BatchNormalization(),
        #TimeDistributed(Dropout(0.8)),
        TimeDistributed(Flatten()),
        #TimeDistributed(Dense(30,activation='softmax')),  
        LSTM(20,unit_forget_bias = 0.5, return_sequences = True),
        TimeDistributed(Dense(6,activation='softmax'))        
    ])
    adam = Adam(learning_rate=0.0001)
    model.compile(loss='categorical_crossentropy',
              optimizer= adam,
              metrics=['accuracy'])
    return model

def makePred(Xarr):
	Xtemp = [] 
	Xtemp.append(Xarr)
	Xin = np.asarray(Xtemp) # prepared input of 45 frames for model    
	#getting the predictions for the sequence     
	Yout = model.predict(Xin) #softmax output from the model
	Ycurr = Yout[0].tolist() # current sequence
	# applying thresholding and getting classes
	thr = 0.70 #threshold value
	pred = [] # to be populated with predictions
	for frame in Ycurr:
		Ymax = max(frame)
		if Ymax < thr:
			# confidence too low
			pred.append(6)
		else:
			pred.append(frame.index(Ymax))
	#do polling
	print (asanas.get(statistics.mode(pred)))
	return
        

def addToPred(Xch, Xarr, count):
    # print(Xch)
    Xarr[count] = Xch
    count = count + 1
    # get prediction if count is 45: all frames acquired
    if count == 10:
        makePred(Xarr)
        count = 0  # reset counter
        Xarr = np.empty((10, 33, 2))  # reset array        
    return Xarr, count


def readFile(filename, Xarr, count):
    with open(filename) as json_data:
        d = json.load(json_data)
        # print(d.shape())
        # X = np.asarray(d)
        for i in range(0, len(d)):
            A = []
            A = d[i]
            #A = [person['pose_keypoints_2d']]                
            X = np.asarray(A)
            X1 =  X[:,0]
            X2 = X[:,1]
            Xch = np.dstack((X1,X2))
            json_data.close
            Xarr, count = addToPred(Xch,Xarr,count)
                # add it to current set of frames           
    return Xarr, count

#load the model with weights
model = get_model()
model.load_weights("weights/val1-99-0.9944.hdf5")
#array to hold curent sequence and other  state variables
Xarr = np.empty((10,33,2))
lastRead = "none"
timeout = time.time() + 10
count = 0
# loop runs until no new file is generated for 3 seconds
while(True):
    #print(count)
    latest_file = max(glob.glob("output/*"), key=os.path.getctime)
    Xarr, count = readFile(latest_file,Xarr,count)       
    if time.time() > timeout:
        break
    
    # lastRead = latest_file