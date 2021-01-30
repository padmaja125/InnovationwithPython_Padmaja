import time
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 125)

engine.say('Welcome, Enter the floor number to proceed')

engine.runAndWait()

Total_floors = 8
lift_l = 0

while True:
    def up(current_f, destination_f):

        if destination_f > current_f:
            time.sleep(1)
            print("going Up")
            engine.say("Going Up")
            engine.runAndWait()
            diff = destination_f - current_f
            for i in range(current_f + 1, destination_f + 1):
                print(i)
                time.sleep(1)

            time.sleep(1)
            print("You have reached on {} floor".format(destination_f))
            engine.say("You have reached on your destination floor")
            engine.runAndWait()
            time.sleep(1)
            print("Doors are opening")
            engine.runAndWait()
            time.sleep(2)
            lift_l = destination_f
            print("Lift current location is : {}".format(lift_l))

        elif destination_f < current_f:
            time.sleep(1)
            print("Going down")
            engine.say("going down")
            engine.runAndWait()
            diff = abs(destination_f - current_f)

            for i in range(current_f - 1, destination_f - 1, -1):
                print(i)
                time.sleep(1)

            time.sleep(1)
            print("you have reached on {} floor ".format(destination_f))
            engine.say("You reached your destination")
            engine.runAndWait()
            time.sleep(1)
            print("Doors are Opening")
            engine.say("Doors are opening")
            engine.runAndWait()
            time.sleep(2)
            lift_l = destination_f
            print("lift current location is: {}".format(lift_l))


    if lift_l == 0:
        call_lift = input("press 'u' to go up: ")
    else:
        call_lift = input("Press U or D for Up or Down: ")

    if call_lift == 'u' or call_lift == 'd':
        print("Welcome to the lift")
        engine.say("Welcome")
        engine.runAndWait()

        current_f = int(input("Enter the current floor"))

        if current_f > 8:
            print("sorry Enter the proper floor ")
            engine.say("sorry Enter the proper floor ")
            engine.runAndWait()
            continue

        if lift_l == current_f:
            print("Lift is coming Up")
            engine.say("Wait Please, While lift is coming Up")
            engine.runAndWait()
            time.sleep(2)
            print("Doors are opening")
            engine.say("Doors are opening")
            engine.runAndWait()
        elif lift_l > current_f:
            print("Lift is coming Up")
            engine.say("Wait Please, While lift is coming Up")
            engine.runAndwait()
            time.sleep(2)
            print("Doors are opening")
            engine.say("Doors are opening")
            engine.runAndWait()
        else:
            print("Lift is coming Up")
            engine.say("Wait Please, While lift is coming Up")
            engine.runAndWait()
            time.sleep(2)
            engine.say("Doors are opening")
            engine.runAndWait()

        time.sleep(2)
        print("Ring Ring")
        engine.say("Ring Ring")
        engine.runAndWait()

        time.sleep(2)
        destination_f = int(input("Enter the floor no: "))
        time.sleep(2)
        print("Ring Ring")
        engine.say("Ring Ring")
        engine.runAndWait()
    if destination_f > 8:
        print('Sorry Building have only 8 floors')
        engine.say('Sorry Building have only 8 floors')
        engine.runAndWait()
    elif destination_f == current_f:
        print("you are on the same floor")
        engine.say("you are on the same floor")
        engine.runAndWait()
    else:
        up(current_f, destination_f)
        lift_l = destination_f
