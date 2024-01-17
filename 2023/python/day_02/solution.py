s = "Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green; 2 red, 13 blue, 8 green; 18 blue, 7 green, 5 red"

def get_txt_as_arr(path): 
  doc = ""
  with open(path) as fh: 
    doc = fh.read()
  return doc.split("\n")
  
def get_results(str):
  result = str.split(":")
  idx = int(result[0].split()[1])
  return result[1].strip()

def get_games(str):
  games = str.split(";")
  results = []
  for game in games:
    results.append(get_hands(game))
  return results

def get_hands(str):
  hands = {}
  for hand in str.split(","): 
    number, color = hand.strip().split(" ")
    hands[color] = int(number)
  return hands

def entire_game(input):
  game = []
  for item in input:
    results = get_results(item)
    game.append(get_games(results))
  return game

def check_game(game, limits):
  for k in game: 
    if game[k] > limits[k]:
      return False 
  return True

def check_games(games, limits): 
  for game in games: 
    if not check_game(game, limits):
      return False
  return True

def find_max(games):
  maxes = {"green": 0, "red": 0, "blue": 0}
  for game in games: 
    for k in game: 
      if game[k] > maxes[k]: 
        maxes[k] = game[k]
  return maxes

def get_powers(board): 
  total = 0
  for games in board: 
    maxes = find_max(games)
    max_total = 1
    for max in maxes.values():
      max_total *= max
    total += max_total
  return total
    

def check_board(board, limits):
  total = 0
  for idx, games in enumerate(board): 
    if check_games(games, limits):
      total += idx + 1
  return total

def main(path):
  arr = get_txt_as_arr(path)
  board = entire_game(arr)
  # print(check_board(board, {"red" : 12, "green" : 13, "blue" : 14}))
  print(get_powers(board))

if __name__ == "__main__": 
  PATH = "puzzle.txt"
  main(PATH)

