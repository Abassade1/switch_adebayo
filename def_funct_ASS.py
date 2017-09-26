print ("====VALUE OF AN AREA====")
print ()

def room_size():
    lenght = int(input("Room lenght = " ))
    breath = int (input ("Room Breath = "))
    room_size = lenght * breath 
    if room_size >= 500:
        print ("The Room size is ", room_size , "This is for master bedroom!")
    elif room_size == 400:
        print ("The Room size is ", room_size, "This is for madam bedroom")
    else:
        print ("The Room Size is ", room_size, "This is size for lady's room")


room_size()
