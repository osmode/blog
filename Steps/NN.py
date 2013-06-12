# NN.py  (C) Omar Metwally
# This is a simple script that initializes a neural network using
# the Pybrain library and uses it to predict the number of steps a person
# will take given the day of the week and the number of steps they took
# the previous day. 

from pybrain.structure import FeedForwardNetwork
from pybrain.structure import TanhLayer, SoftmaxLayer
from pybrain.structure import LinearLayer, SigmoidLayer, FullConnection

from pybrain.tools.shortcuts import buildNetwork
from pybrain.tools.neuralnets import NNregression
from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

from random import shuffle

# load raw, mean-normalized and feature-scaled data
# Feature scaling and mean normalization is critical here because
# of the wide range of feature values
f = open("output3")
data = f.read()
f.close()

# randomize the data before creating the train and CV sets
shuffle(data)

test_data = data[0:19]
CV_data = data[20:40]
data = data[41:]

features = []
test_features = []
targets= []
test_targets = []

# load csv data into lists 'data' and 'test_data'
# note that python's csv library was not used to make
# this demo code transparent to non-Python users and keep 
# the focus on pybrain
for row in data:
	row = row.split(',')

	if row[0]:
		temp = []
		temp.append(float(row[1]))

		temp2 = []
		temp2.append(float(row[0]))
		temp2.append(float(row[2]))

		features.append(temp2)
		targets.append(temp)

print "number of features: ",len(features[1])

for row in test_data:
	row = row.split(',')

	if row[0]:
		temp = []
		temp.append(float(row[1]))

		temp2 = []
		temp2.append(float(row[0]))
		temp2.append(float(row[2]))
		
		test_features.append(temp2)
		test_targets.append(temp)

		
num_input = len(data)
num_test = len(test_data)

# initialize a network with number of input units = 2 and 1 output unit
# (for regression). You can change the intervening parameters to specify
# the number of hidden layers and the number of hidden units in each
# hidden layer. For example, the line below initializes a NN with 2 hidden
# layers, one with 100 units and one with 50 units. 
net = buildNetwork(2,100,50,1)
print "number of inputs m: ",num_input

# initialize two classification data sets, one for training
# and cross-validation purposes, the other for the test data
# first argument is number of input units, second argument is # of output units
DS = SupervisedDataSet(2,1)
test_DS = SupervisedDataSet(2,1)

# populate the DS data set
i = 0
while i < len(features):
	DS.appendLinked(features[i], targets[i])
	i+=1
i = 0


# populate the test data set
while i < len(test_features):
	test_DS.appendLinked(test_features[i], test_targets[i])
	i+=1

# split up the regresion data set 'DS' into training
# and cross-validation sets
cvdata, trndata = DS.splitWithProportion(0.2)

trainer = BackpropTrainer(net, dataset=trndata,momentum=0.1,verbose=True, weightdecay=0.01)

# train the NN 10 separate times

i =0
while i < 10:
	# specify the number of epochs
	trainer.trainEpochs(5)

	i+=1

i = 0

print "Predicting on training data:\n"
print net.activateOnDataset(trndata)
print "Predicting on CV data:\n"
print net.activateOnDataset(cvdata)
print "Predicting on test data:\n"
print net.activateOnDataset(test_DS)

# Add code here to convert the output data into steps using the
# means and standard deviations (i.e. undo the mean normalization 
# and feature scaling, which was performed using normalizeScale.m
