import random
import string
def get_otp(length):
    num=[1,2,3,4,5,6,6,7,8,9]
    new=''
    while length:
        new1=random.choice(num)
        new+=str(new1)
        length-=1
    return new
try:
    length=int(input("Enter the length of OTP you want: "))
    if length < 6:
        print("Minimum OTP length is 6:")
    elif length > 10:
        print("Maximum OTP length is 10")
    else:
        print("Generating OTP:")
        print(f"Your OTP is: {get_otp(length)}")
except ValueError as e:
    print(f"Value Error: {e}")