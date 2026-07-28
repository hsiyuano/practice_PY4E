def computepay(h,r):
    if h <= 40:
        return h * r
    return 40 * r + (h - 40) * r * 1.5
hrs = input("Enter hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print ("Pay:", p)