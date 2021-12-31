from Hector import *

def Driver():
    Hector = AIIPP("Hector")
    Hector.introduce_self()
    message = Hector.listen()
    # process message
    Hector.speak("I Like you")

    info = Hector.ask_question("Ava")
    if info == "* is a friend"
        Hector.friends.append(info)




if __name__ == "__main__":
    Driver()