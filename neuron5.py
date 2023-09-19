def main():
	neu5i = input("Initial membrane potential:")
	wei5 = input("Weight parameter (0-1):")
	## Neuron 5 and weight input
	if float(neu5i) > -65.0:
		neu5o = float(neu5i)+5.0*float(wei5)
		print("Spike!")
	else:
		neu5o = neu5i
		print("No spike")
	print("neuron 5 output: ", neu5o)
	## Neuron 5 output

if __name__ == "__main__":
	main()