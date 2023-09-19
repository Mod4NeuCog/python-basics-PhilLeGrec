def main():
	import sys
	neu3i = sys.argv[1]
	## Neuron 3 input
	if float(neu3i) > -65.0:
		neu3o = float(neu3i)+5.0
		print("5")
	else:
		neu3o = neu3i
		print("0")
	print("neuron 3 output: ", neu3o)
	## Neuron 3 output

if __name__ == "__main__":
	main()