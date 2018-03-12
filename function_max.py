def maximum(a,b):
	if a==b:
		print("equal")
	elif a>b:
		print("The maximum is a = {}".format(a))
	else:
		print("The maximum is b = {}".format(b))

a=int(input("a="))
b=int(input("b="))

maximum(a,b)	