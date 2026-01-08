 # Find Area of circle
import math
def find_Area_circle(r):
  Area = (math.pi)*(r)**2
  return Area
def main():
  r=int(input("Enter radius of circle: "))
  p=find_Area_circle(r)
  print(f"Area of circle of radius {r} is {p:.3f}")
main()

#Find Simple intrest
def find_Simple_intrest(amt,r,t):
  si=(amt*r*t)/100
  return si
def main():
  amt=int(input("Enter amount: "))
  r=int(input("Enter intrest rate per year: "))
  t=int(input("Enter time in years: "))
  p=find_Simple_intrest(amt,r,t)
  print(f"Simple intrest is {p}")
main()

# Temperature conversion
def find_temp(cel):
 fahr=(9/5)*cel+32
 return fahr
def main():
 cel=int(input("Enter temperature in celsius: ")
 temp=find_temp(cel)
 if temp>100:
  print(f" Outside Temperature is {temp} degree fahrenheit")
  print("Too hot outside")
 elif temp<50:
  print(f"Outside Temperature is {temp} degree farhenheit")
  print("Pleasant Outside")
main()
 
 
  
