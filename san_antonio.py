# -*- coding utf-8 -*-
import random

def read_values_from_json:
  values = []
  with open("characters.json") as f:
    data = json.load(f)
    for entry in data:
      values.append(entry[character])
      return values

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
