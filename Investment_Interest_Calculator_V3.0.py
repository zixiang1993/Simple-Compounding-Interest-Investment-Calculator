def greetings():
  print("This is a simple compounding interest calculator.")
  print("")
  print("Made by Ng Zi Xiang (Zack).")
  print("V3.0 : Last updated 8/10/2021")
  print("")
  input("Press any key to continue to use: ")

greetings()

a = int(input("State your initial deposit amount (no comma), say 10000: "))
R = float(input("Give an interest rate in decimal, say 0.10, which is 10% per annum: "))
n1 = int(input("Give the no. of years for investment, say 10 for 10 years: "))
print("")
print("")

def my_formula(a,R,n1):
  n2 = 1
  total_interest = []
  while n2 != n1+1:
    i = int(a*R)
    x = f'{int(i):,d}'
    a = a + i
    print(f"Year {str(n2)} - Interest earned is RM {x}.")
    total_interest.append(i)
    cumulative_interest = f'{sum(total_interest):,d}'
    print(f"Year {str(n2)} - Cumulative value stands at RM {cumulative_interest}.")
    print("")
    n2 += 1
    i = (a+i)*R
  z = f'{int(sum(total_interest)):,d}'

  # Cumulative interest is {z}.
  # z = f'{int(sum(cumulative_interest)):,d}'
 
  print(f"Your total interest is RM {str(z)} after {str(n1)} years .")
  print("")
  print("Below is the respective interest earned per year :")
  print("")
  for interest in enumerate(total_interest):
    print(interest)
  print("")

my_formula(a,R,n1)
print("Thank you for using and hope you found it useful!")
exit = input("Press any key to exit: ")