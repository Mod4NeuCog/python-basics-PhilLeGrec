import random
def Simulate():
	neu6i = input("Initial membrane potential:")
	wei6 = random.uniform(0,1)
	if float(neu6i) > -65.0:
		print("Spike")
		neu6o = float(neu6i)+5.0*float(wei6)
	else:
		neu6o = neu6i
	print("New membrane potential: ", neu6o)
def Simulate2():
	neu6i = input("Initial membrane potential:")
	wei6 = random.uniform(0,1)
	if float(neu6i) > -65.0:
		print("Spike")
		neu6o = (1-1.05*float(wei6))*float(neu6i)
	else:
		neu6o = neu6i
	print("New membrane potential: ", neu6o)
Simulate()
Simulate2()
## The model for the first simulator is based on the equation x1 = x0 + s*w , where x is the membrane potential (function of discrete time), s is synaptic potential, w is synaptic weight parameter
## The model for the second simulation is based on the equation x1 = (1-1.05)*w*x0