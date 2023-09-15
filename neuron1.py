import sys
neu1i = sys.argv[1]
## Neuron 1 input
if float(neu1i) > -65.0:
	neu1o = 5.0
	print("5")
else:
	neu1o = 0.0
	print("0")
#print("neuron 1 output: ", neu1o)
## Neuron 1 output