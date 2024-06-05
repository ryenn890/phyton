# ------ FUNCTIONS ------

# Welcomes user and introduces the quiz
def intro():
    # Ask the user their name
    name = input("What's your name?")

    # great the user and introduce the quiz
    print("Welcome to this quiz,",name)
    print("This quiz is about the ten largest countries in the world can you name them")

# ------ MAIN CODE ------

intro()


def getlives():
    while true:
        Lives = input("how many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                 return Lives
            else:
                 print("please choose a positive number")
            except:
                print("that wasn't a number")


lives = getlives()