def computepay():# I used computerpay(h,r), but the error message is h,r is not defined
    hrs = input("Enter hours: ")
    rate = input("Enter rate: ")

    h = float(hrs) #create function (函数) of computerpay
    r = float(rate)

    if h <= 40:
        return h * r

    return 40 * r + (h - 40) * r * 1.5


p = computepay()# also does not use computerpay(h, r), leave it empty
print("Pay:", p)