## Normal way
name = "Chandru"

string = "Hi there, I am Chandru"

## f-strings


name = 'Sweety Omana'

string = f"Hi there, I am {name}"

print(string)


## String method

text = "Chandru Deivanayagan"

print(text.upper())

print(text.lower())

print(text.title())


## Finding and replacing

message = "I love Python Programming with Python"

print("Python" in message)

print(message.startswith("I"))

print(message.endswith("on"))


## Find Position

print(message.find("Python"))

print(message.count("Python"))

## replace


new_msg = message.replace("Python","TypeScript")

print(new_msg)