## This calculator helps you plan out an essay


word = input("Pick a word")
if len(word) % 2 == 0:
    print("Your word has an even amount of letters")
else:
    print("Your word has an odd amount of letters (" + str(len(word)) + ")")

# This part will count if a piece of text meets a word count

word_count = int(input("What is your character count? "))
phrase = input("Type your text here for character count: ")
if len(word) > word_count:
    print("Your text meets the character count")
else:
    print("Your text is below the character count. ")
    actual_word_count = (len(phrase))
    remainder = abs(word_count - actual_word_count)
    print("You have " + str(remainder) + " characters left.")

#We tell them how many they have left to meet

#This part helps plan out the time needed

if len(word) < word_count:
    time_spent = int(input('How many minutes have you spent on it so far? '))
    rate = time_spent/actual_word_count
    time_needed = rate * remainder
    print("You need about " + str(time_needed) + " minutes left to complete it at this rate.")

days_left = int(input("How many days left do you have to finish it? "))
if days_left < 1:
    print("lol")
else:
    time_perday = time_needed/days_left
    print("You will need to spend at least " + str(time_perday) + " minutes every day to meet the deadline.")
    
