largest = None # create a variable but does not contain a value, no value is assigned
smallest = None
while True:
    num = input("Enter a number:")

    if num == "done": # == mean is equal to, = assign values to variable
        break

    try: # try to convert code to int, if cannot print
        num = int(num)
    except: # after except it has to have an indentation, it can add except:ValueError to specify
        print ("Invalid input")
        continue

    if largest is None or num > largest: # if largest does not have a number or the new number is bigger than the current largest number, save the new number as largest
        largest = num
    if smallest is None or num < smallest:
        smallest = num
    
    
print ("Maximum is", largest)
print ("Minimun is", smallest)


