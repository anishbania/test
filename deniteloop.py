smallest=None
for num_small in [34,9,3,13,23,16]:
    if smallest is None :
        smallest=num_small
    elif num_small<smallest:
        smallest=num_small
print("Smallest",smallest)
print("Hello world")        
