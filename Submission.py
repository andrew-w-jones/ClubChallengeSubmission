#!bin/python3

#Intermediate and advanced need to import this:
import datetime


#------BEGINNER------
#Start by getting the input and assigning it to a variable (I called it 'name')
#In the input we can specify the prompt we wish to be displayed.
name = input("Name: ")
#Then we print out the custom message
print("Hello "+name+", how are you?")



#------INTERMEDIATE------
#find out what greeting is proper for the time of day
now = datetime.datetime.now()
if now.hour <= 12:
    timeOfDay = "morning"
if now.hour <= 17 & now.hour > 12:
    timeOfDay = "afternoon"
if now.hour > 17:
    timeOfDay = "evening"

#Get the users name
name = input("Name: ")

#Print out custom message
print("Good "+timeOfDay+", "+name+".")


#------ADVANCED------

#same thing but with fstrings
#we can reuse the time getting from above, but we should get the name again
name = input("Name: ")
print(F"Good {timeOfDay}, {name}.")
