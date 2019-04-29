
for i in range(1000):
    print("NAME" + str(i))
    if i > 99:
        continue
    print("NAME" + str(i).zfill(3))

    # can be inproved: write output direct into file 
