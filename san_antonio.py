# -*- coding utf-8 -*-
import random

quotes = [
  "Ecoutez-moi monsieur Shakespear, vous avez beau être ou ne pas être, nous sommes !",
  "On doit pouvoir choisir entre s'écouter parler et se faire entendre"]

characters = [
  "Alvin et les Chipmunks",
  "Babar",
  "betty boop",
  "calimero",
  "casper",
  "le chat potté",
  "Kirikou"]

def get_random_item(object_list):
  rand_num = random.randint(0, len(object_list) - 1)
  item = object_list[rand_num] #Get a quote from a list
  return item #Return the item

def capitalize(words):
  for word in words:
    word.capitalize()

def message(character, quote):
  capitalize(character)
  capitalize(quote)
  return "{} à dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

# Show random quote

while user_answer != "B":
  print(message(get_random_item(characters), get_random_item(quotes)))
  user_answer = input("Tapez entrée pour connaitre une autre citaion ou B pour quitter le programme.")
