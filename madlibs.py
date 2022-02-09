# # string concatenation ( aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____"
# youtuber = "Zach King"  # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

# Obviously this can be extended to allow for multiple inputs for random madlibs
# Some things to add to enhance this project coud be:
#   Add additional madlibs
#   Produce a randome generator that selects the madlib when the computer is ran
#   Add word highlighting
#   Create a front end webpage to allow for user input
