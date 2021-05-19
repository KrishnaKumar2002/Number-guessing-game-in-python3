import math
import random
lower=int(input("enter the lower bound))
upper=int(input("enter the upper bound"))
a=random.randint(lower,upper)
print("you have only ",round(math.log(upper-lower=1,2),"chances")
count=0
while count<math.log(upper-lower+1,2):
   count+=1
   guess=int(input("guess the number"))
   if x==guess:
    print("congrats! you got it in",count,"try")
    break
   elif x>guess:
    print("you have guessed too high")
   else:
    print("you have guessed too small)
 if count>=math.log(upper-lower=1,2):
   print("the number is %d",count)
   print("\n better luck next time!")
    
