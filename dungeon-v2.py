dungeon = [['Rm 101', 'Rm 102', 'Rm 103', 'Rm 104', 'Elevator'],
           ['Rm 201', 'Rm 202 (my room)', 'Rm 203', 'Rm 204', 'Elevator'],
           ['Rm 301', 'secret stairs', 'Rm 303', 'Rm 304', 'Elevator'],
           ['Rm 401', 'secret stairs', 'maintenance closet', 'Rm 404', 'dead end']]

#tell me what room I should move to
def move_left_from(room_number):
    print("You want to move left! OK. I don't know how to do that yet.")

def move_right_from(room_number):
    print("You want to move right! OK. I don't know how to do that yet.")

def move_up_from(floor_number):
    print("You want to move up! OK. I don't know how to do that yet.")

def move_down_from(floor_number):
    print("You want to move down! OK. I don't know how to do that yet.")

#FOR THURSDAY, 7/27:
#Here is a "game loop" that asks for user input and calls the correct
#functions. The key is the while(True) loop, and also that
#exit() gets called on some input. See if you can adapt this for your
#social network back-end!
def main():
    print("Welcome to the dungeon! Muahahaha.")
    floor_number = 1
    room_number = 1
    print("You start at" + dungeon[floor_number][room_number])

    #this is equivalent to "forever": since True is true forever!
    while True:

        #ask for what the user wants to do
        user_action = input("What do you want to do?\n \
        You can move up (u), down (d), left (l), or right(r),\n \
        or you can quit (q). ")

        if user_action == 'q':
            print("Sorry to see you go!")
            exit()

        #elif = else if. So, if the user action was NOT q, now check if it's u
        elif user_action == 'u':
            move_up_from(floor_number)

        elif user_action == 'd':
            move_down_from(floor_number)

        elif user_action == 'r':
            move_right_from(room_number)

        elif user_action == 'l':
            move_left_from(room_number)

        #else here means, if the user action was ANYTHING else
        #besides q, u, d, r, or l.
        else:
            print("Um, I don't know what that means. Please ask again.")

        #at the end of the if/else statements, print a line of stars
        #to help the user separate the previous action from the next action
        print("**********************\n")

    #end of the main method

#call the main method, so our program runs
main()
