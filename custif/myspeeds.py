#!/usr/bin/env python3

message = 'How is your network speed? '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 100:
    message = message + 'Supa Fast'
elif connection >= 50:
    message = message + 'Decent.'
elif connection >= 10:
    message = message + 'Get Better internet.'
else:
    message = message + 'Get Internet.'
print(message)

