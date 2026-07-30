## Functions - reusable blocks of code

## defining functions

def greet():
    print("Hello !! people present here.")

    print("Hello again!!!")

greet()

def calculator():
    pass

def send_email():
    pass

def validate_password():
    pass

def ai_engine():
    pass



def say_goodbye():
    print("Good Bye!!!")
    print("See you later")



say_goodbye()

say_goodbye()

say_goodbye()


## ---- hard coded ----

def check_weather():
    temperature = 30
    if temperature > 25:
        print("It's Hot")
    else:
        print("It's nice weather")


check_weather()


# parameters

def greet():
    print("hello people")

def greet_(name):
    print(f"Hello, {name}")


greet_("Sweety Omana")

greet_(name = "Devi Bala")


def greeting(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")

greeting("Sweety","Omana")

greeting(last_name = "bala",first_name = "devi")

## default parameters

def greetings(last,first="Hello"):
    print(first,last)

greetings(last = "chandru")

greetings("Chandru")


def greet(first,last="Every one"):
    print(first,last)

greet("Listen")


def greet(first="Listen",last="Every one"):
    print(first,last)

greet(last="Sweety")


###########################################################################

# functions

def add(a,b):
    return(a+b)

def greet():
    print("hello!!!")

greet()

add(100,100)

add(100,100,9)


def greeting(name):
    print(f"hello, welcome home {name}")

greeting("Kavitha")

def greetings(name,greet="Hello"):
    print(greet,name)

greetings("Brindha")

def greet(greet="Hello, welcome",name= "Friend"):
    print(greet,name)


greet(name="Sai Pallavi")