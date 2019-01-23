def Fibonaaci(num1, num2, number1):
		while number1 >0:
			if(num2%2 == 0):
				print("Fibonaaci Number:", num2)
			next = num1 + num2;
			num1 = num2;
			num2 = next;
			number1 = number1-1
	

#Main starts from here
a = 1
b = 1
#num = input("Enter a number:=")
Fibonaaci(a,b,35)















