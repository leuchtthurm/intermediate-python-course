import random

def main():
  roll = random.randint(1,6)

  if roll == 1:
    print(f'You rolled a {roll}! Back to the start!')
  elif roll == 6:
    print(f'You rolled a {roll}! Roll again!')
  else:
    print(f'You rolled a {roll}.')

if __name__== "__main__":
  main()