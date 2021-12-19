write=""
started = False

while 1==1:
    write=input("> ").lower()

    if write =="help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif write=="start":
        if started:
            print("Car already started")
#hallo
        else:
            print("Car started...ready to go!")
            started=True
    elif write=="stop":
        if not started==True:
            print("Car is already stopped")
        else:
            print("Car stopped")
            started = False
    elif write=="quit":

        break

    else:
        print("I don't understand")
