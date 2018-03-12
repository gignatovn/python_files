import string

def reverse(text):
    return text[::-1]

def palindrom(text):
    return text == reverse(text)

inp=input("Enter string: ")

""" removing punctuation """

s=inp.translate(str.maketrans('','',string.punctuation))

""" removing spaces """

s1=s.replace(" ","")

""" removing Upper case """

s2=s1.lower()


if(palindrom(s2)):
    print("It's palindrom")
else:
    print("Try again :)")
