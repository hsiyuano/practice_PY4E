hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter rates:")
r = float(rate)
if h <= 40: # if...else condition
    pay = h*r
else: 
    pay = 40*r + (h-40)*(1.5*r)
print(pay)