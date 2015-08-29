# A temperature class for gxconv
# License: GPL2.0
# Author: Flaymond Darius
# NOTE: Please refer to the LICENSE file for further informations about the,
#		license.


class Temperature_Class():
	
	def celToFah(self):
		print("\nCelsius to Fahrenheit")
		# this will loop the prompt again and again
		while True:
			# save the input in user_input as float type
			# NOTE: hit ctrl+c to quit the program
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			# calculate the user_input with the formula, and save it in total variable
			total = user_input * 9.0/5.0 + 32.0 
		
			# print and output the answer in total variable with only 4 decimal point maximum
			print("The answer is: %.4f" % (total))	
		
		
		
	# celsius to kelvin
	def celToKel(self):
		print("\nCelsius to Kelvin")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input + 273.15
		
			print("The answer is: %.4f" % (total))

	# celsius to rankine
	def celToRan(self):
		print("\nCelsius to Rankine")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = (user_input + 273.15) * 9.0/5.0
		
			print("The answer is: %.4f" % (total))
		
	# fahrenheit to celsius
	def fahToCel(self):
		print("\nFahrenheit to Celsius")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = (user_input - 32.0) * 5.0/9.0
		
			print("The answer is: %.4f" % (total))
		
	# fahrenheit to kelvin
	def fahToKel(self):
		print("\nFahrenheit to Kelvin")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = (user_input + 459.67) * 5.0/9.0
		
			print("The answer is: %.4f" % (total))
		
	# fahrenheit to rankine
	def fahToRan(self):
		print("\nFahrenheit to Rankine")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input + 459.67
		
			print("The answer is: %.4f" % (total))
		
	# kelvin to celsius
	def kelToCel(self):
		print("\nKelvin to Celsius")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input - 273.15
		
			print("The answer is: %.4f" % (total))
	
	# kelvin to fahrenheit
	def kelToFah(self):
		print("\nKelvin to Fahrenheit")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input * 9.0/5.0 - 459.67
		
			print("The answer is: %.4f" % (total))
	
				
	# kelvin to rankine
	def kelToRan(self):
		print("\nKelvin to Rankine")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input * 9.0/5.0
		
			print("The answer is: %.4f" % (total))
	
		
	# rankine to celsius
	def ranToCel(self):
		print("\nRankine to Celsius")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = (user_input - 491.67) * 5.0/9.0
		
			print("The answer is: %.4f" % (total))
	
		
	# rankine to fahrenheit
	def ranToFah(self):
		print("\nRankine to Fahrenheit")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input - 459.67
		
			print("The answer is: %.4f" % (total))
		
	# rankine to kelvin
	def ranToKel(self):
		print("\nRankine to Celsius")
		while True:
			user_input = float(input("Please enter your input(ctrl+c to quit): "))
		
			total = user_input * 5.0/9.0
		
			print("The answer is: %.4f" % (total))
			
			
# Temperature greeter menu
def TempGreeter():
	# print the list of available formulas
	
	print("\nTemperature conversions\n")
	print("Available formulas: ")
	print("\n1.Celsius->Fahrenheit")
	print("2.Celsius->Kelvin")
	print("3.Celsius->Rankine")
	print("\n4.Fahrenheit->Celsius")
	print("5.Fahrenheit->Kelvin")
	print("6.Fahrenheit->Rankine")
	print("\n7.Kelvin->Celsius")
	print("8.Kelvin->Fahrenheit")
	print("9.Kelvin->Rankine")
	print("\n10.Rankine->Celsius")
	print("11.Rankine->Fahrenheit")
	print("12.Rankine->Kelvin\n")
	choice = int(input("Please enter your choice in integers(ctrl+c to quit): "))
		
	# decide based on user choice in integer (1-12)
		
	t1 = Temperature_Class()
	
	if choice == 1:
		t1.celToFah()
		
	elif choice == 2:
		t1.celToKel()
		
	elif choice == 3:
		t1.celToRan
		
	elif choice == 4:
		t1.fahToCel()
		
	elif choice == 5:
		t1.fahToKel()
		
	elif choice == 6:
		t1.fahToRan()
		
	elif choice == 7:
		t1.kelToCel()
		
	elif choice == 8:
		t1.kelToFah()
		
	elif choice == 9:
		t1.kelToRan()
		
	elif choice == 10:
		t1.ranToCel()
		
	elif choice == 11:
		t1.ranToFah()
		
	elif choice == 12:
		t1.ranToKel()
		
	# else than the provided numbers, just print these	
	else:
		print("Error occured")
