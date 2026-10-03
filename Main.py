import random
import string  # Imported but not used by the current numeric generator.


def get_otp(length):
    """Build a numeric OTP of the requested length and return it as a string.

    Digits are drawn one at a time from `num` with replacement, so repeats are allowed.
    The pool is 1-9 only (0 is not included) and 6 appears twice, which makes 6
    slightly more likely than the other digits.
    """
    # Digit pool used for each position of the OTP.
    num = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
    new = ''  # Accumulates the OTP as a string.

    # Keep picking a random digit until the requested length is filled.
    while length:
        new1 = random.choice(num)  # Pick one digit from the pool.
        new += str(new1)           # Append it to the OTP string.
        length -= 1                # One digit done.

    return new


try:
    # Ask the user how many digits the OTP should have.
    length = int(input("Enter the length of OTP you want: "))

    # Reject lengths outside the supported 6-10 range.
    if length < 6:
        print("Minimum OTP length is 6:")
    elif length > 10:
        print("Maximum OTP length is 10")
    else:
        print("Generating OTP:")
        print(f"Your OTP is: {get_otp(length)}")
except ValueError as e:
    # int() raises ValueError if the user enters something that is not a whole number.
    print(f"Value Error: {e}")
