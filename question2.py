# function that takes a number and checks if it is an even number and returns true or false
def is_even(number):
   return True if number % 2 == 0 else False

while True:
   number = int(input("Enter a number: "))
   if number == 0:
       break
   else:
       if is_even(number):
           print("Even")
       else:
           print("Odd")
