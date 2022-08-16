"""Restaurant rating lister."""

import sys
dictionary_restaurant_rating = {}
tuple_ratings = None

def read_restaurant_rating(filename):
  file = open(filename)
  for line in file:
    restaurant_and_rating = line.rsplit()
    restaurant_and_rating = line.split(":")
    restaurant_name = restaurant_and_rating[0]
    restaurant_rating = restaurant_and_rating[1][0]
    dictionary_restaurant_rating[restaurant_name] = restaurant_rating
  return dictionary_restaurant_rating

def make_restaurant_tuple(filename):
  dictionary_restaurant_rating = read_restaurant_rating(filename)
  tuple_ratings = dictionary_restaurant_rating.items()
  tuple_ratings = sorted(tuple_ratings)
  for tuple in tuple_ratings:
    print(f'{tuple[0]} is rated at {tuple[1]}.')


def ask_restaurant_rating():
  requested_restaurant = input("What is the name of the restaurant? ")
  while True:
    restaurant_score = int(input("How would you rate this restaurant? "))
    if restaurant_score < 1 or restaurant_score > 5:
      print('Rating needs to be between 1 and 5!!!!!')
    else:
      break
  dictionary_restaurant_rating[requested_restaurant] = restaurant_score
  make_restaurant_tuple(sys.argv[1])


while True:
  print("Would you like to A) Check ratings B) Rate a new restaurant or C) Exit")
  choice = input("Choose an option ")
  if choice == 'A':
    make_restaurant_tuple(sys.argv[1])
  elif choice == 'B':
    ask_restaurant_rating()
  elif choice == 'C':
    print('GOODBYE!')
    break











