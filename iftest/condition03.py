#!/usr/bin/env python3


#user input for hostname
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string

# If statement comparing 2 strings
if hostname.lower() == " mtg":
 print("The hostname was found to be mtg")
 print("hostname matches expected config")

#exit message
print("Exiting the script")
