while True:
	a = int(input("1st number: "))
	b = int(input("2nd number: "))
	if a == 0 & b == 0:
		break;
	print("a + b = ")
	print(a+b)
	print("a - b = ")
	print(a-b)
	print("a * b = ")
	print(a*b)
	if b != 0:
		print("a / b = ")
		print(a/b)
		print("a % b = ")
		print(a%b)
	print("a ** b = ")
	print(a**b)
