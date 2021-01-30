total_floor = int(input("Enter the no.floor : "))
lift_position = 1
start_floor = 1
y = 'True'

while True:
    def floor_selections(total_floor):
        floor_selection = int(input("Enter the destination floor: "))
        try:
            if floor_selection < total_floor:
                final_floor = floor_selection
                return current_floors(total_floor,final_floor)
            elif floor_selection > total_floor:
                print("Enter the proper floor")
                return floor_selections(total_floor)
            else:
                print("Its the top floor. ")
                proceed = input("Do you want to proceed ?(Y / N)")
                select = proceed.upper()
                if select == 'Y':
                    final_floor = floor_selection
                    return current_floors(total_floor, final_floor)
                elif select == 'N':
                    return floor_selections(total_floor)
                else:
                    raise ValueError
        except:
            print("Invalid selection")

    def current_floors(total_floor, final_floor):
        current_floor = int(input("enter the current floor"))
        try:
            if current_floor > total_floor:
                print("enter the proper no.")
                return current_floors(total_floor, final_floor)
            elif current_floor == final_floor:
                print("You are in the same floor")
            else:
                start_floor = current_floor
                return start_lift(start_floor, final_floor)
        except:
            print("Invalid selection")


    def start_lift(start_floor, final_floor):
        if start_floor == 0:
            call_lift = input("press 'u' to go up: ")
        else:
            call_lift = input("Press U or D for Up or Down: ")

        lift_in = call_lift.upper()
        try:
            if lift_in == 'D':
                print("lift is coming Down")
                return up(start_floor, final_floor)
            elif lift_in == 'U':
                print("lift is coming Up")
                return up(start_floor, final_floor)
            else:
                print("invalid selection")
                return start_lift(start_floor)
        except:
            print("Error occoured")
            return start_lift(start_floor)

    def up(start_floor, final_floor):
        if final_floor > start_floor :
            print("lift is going up")
            diff = final_floor - start_floor
            for i in range(start_floor + 1, final_floor + 1):
                print(i)
            x = final_floor

            return exit(x)


        elif final_floor < start_floor:
            print(" lift is going Down")
            diff = abs(final_floor - start_floor)

            for i in range(start_floor - 1, final_floor - 1, -1):
                print(i)

            x = final_floor
            exit(x)

    def exit(x):
        print("You Reached {} floor. Have a nice day".format(x))



    floor_selections(total_floor)
