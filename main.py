def lowerletter_function():
    f=open("believer.txt", "r")
    data = f.read()
    cnt=0
    for ch in data:
        if ch.islower(): #islower() checks the letter if it is small letter
            cnt+=1
    f.close()
    print("No. of lower case letter in file", cnt)

lowerletter_function()
