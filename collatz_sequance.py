#even n/2
#odd 3n+1

def collatz():
    try:
        n = int(input("Enter number? "))
        while n!=1:
            print(n)
            if n%2==0:
                n/=2
            else:
                n=3*n+1
    except ValueError:
        print("Try with number pls!!!")

collatz()
