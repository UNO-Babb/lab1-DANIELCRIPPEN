#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("enter a noun: ")
  #Print the story with the user supplied words.
print ("i like to ride a " + noun1)

name1 = input("enter a name: ")
print ("with my friend " + name1)

noun2 = input("enter a place: ")
print ("to " + noun2)

temp = input("describe the weather: ")
print ("it was " + temp)

adj = input("enter an adjective: ")
print ("so we " + adj)

time = input("enter a time of day: ")
print ("this was at " + time)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
