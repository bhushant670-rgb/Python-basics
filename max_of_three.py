 # Program to find maximum of three numbers without using max()
def find_max_num(a,b,c):
  if a>=b and a>=c :
    print(f"{a} is maximum")
  elif b>=c and b>=a :
    print(f"{b} is maximum")
  else :
    print(f"{c} is maximum")
def main():
  a=int(input("Enter first number: ")
  b=int(input("Enter second number: ")
  c=int(input("Enter third number: ")
  find_max_num(a,b,c)
main()
