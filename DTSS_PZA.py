#Defining the simulator
import random
def SimNeurons():
    n_i = -74
    #Initial membrane potential is -74 mV
    syn = random.uniform(0,1)
    #A random impulse (normalized from 0 to 1, later changed to a mV value)
    n = n_i + 30*syn
    if n > -55:
        out = 1
        #Spike!
    else:
        out = 0
        #No spike
    return syn,n, out
#Printing the table
print("Time | Inputs | Membrane Potential | Output")
for i in range(6):
    syn,n,out = SimNeurons()
    print(i, "|", syn, "|", n, "|", out)