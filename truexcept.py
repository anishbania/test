largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        anish=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or largest < anish:
        largest=anish
    elif smallest is None or smallest > anish:
        smallest=anish

print ("Maximum is", largest)
print ("Minimum is", smallest)
