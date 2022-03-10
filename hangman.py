from random import randint
name = input("Enter your name : ")
print("Hello " + name + " Let's Play Hangman")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

categories = ["space",["Hungary","France","Brazil","Turkey","UnitedStates"],["LebronJames","CristianoRonaldo","ArdaTuran","LionelMessi","VolkanDemirel"],["Taco","TavukDoner","AdanaKebap","Sushi","AmericanSalad"]]
x = input("Choose a Category(1.Countries - 2.Sports - 3.Foods): ")
a = int(x)
b = randint(0,5)
my_word = categories[a][b] 

guess_string = ""

life = 6
count = 0
while life > 0:

	character_left = 0

	for character in my_word:
		if character in guess_string:
			print(character)
		else:
			print("-")
			character_left += 1
	
	if character_left == 0:
		print("You Won!! :)")
		break

	guess = input("Guess a letter: ")
	guess_string += guess

	if guess not in my_word:
		life -= 1
		count += 1
		print(HANGMANPICS[count])
		print(f"You have {life} guess left")

		if life == 0:
			print("You died :/ ")
