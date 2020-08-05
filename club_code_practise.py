def error_age():
    print("That isnt your age please enter your accual age")
    age_input_loop = True
def error_age_letter():
    print("That isnt a number please enter your accual age")
    age_input_loop = True    
def age_input():
    age_input_loop = True
    while age_input_loop:
        try:
            user_age = int(input("Hello, {} How old are you? " .format(user_name)))
        except ValueError:
            error_age_letter()
        else:
            if user_age == 18:
                print("You are old enough to enter the club")
                age_input_loop = False
            elif user_age > 18 and user_age < 100:
                print("You are old enough to enter the club")
                age_input_loop = False
            elif user_age < 18:
                print("You are not old enough to enter the club")
                age_input_loop = False
            elif user_age > 100:
                error_age()
            elif user_age != int:
                error_age()
            else:
                error_age()

user_name = str(input("What is your name? "))
age_input()




