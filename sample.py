address = ["flat floor street", "18", "new york"]
pins = {"mike":1234, "joe":1111, "jack":2222}

print(address[0], address[1])

pin = int(input("Enter your pin: "))

def find_in_file(f):
	myfile = open ("sample.txt")
	fruits = myfile.read()
	fruits = fruits.splitlines()
	if f in fruits:
		return "That fruit is in the list."
	else:
		return "No such fruit found!"

if pin in pins.values():
	fruit = input("Enter fruit: ")
	print(find_in_file(fruit))
else:
	print("Incorrect pin!")
	print("This can only be accessed by: ")
	for key in pins.keys():
		print(key)
