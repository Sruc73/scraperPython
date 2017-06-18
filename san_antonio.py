# -*- coding utf-8 -*-
import random
import json

# Give a Json file and return a list
def read_values_from_json(path, key):
  values = []
  with open(path) as f:
    data = json.load(f)
    for entry in data:
      values.append(entry[key])
      return values

# Give a json and return a list
def clean_strings(sentences):
  cleaned = []
  # Store quotes on a list. Create an empty list and add each sentence one by one.
  for sentence in sentences:
    # Clean quote from whitespace and so on
    cleaned_sentence = sentence.strip()
    # Don't use extend as it adds letter one by one!
    cleaned.append(cleaned_sentence)
  return cleaned

def random_character():
  all_values = read_values_from_json()
  return random_intem_in(all_values)

print(random_quote())

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
