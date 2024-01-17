from solution import get_games, get_hands, get_results, check_game

GAME = "Game 1: 7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green"
RESULTS = "7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green"
HAND = "7 blue, 4 red, 11 green"
LIMITS = {
  "blue" : 20,
  "red" : 20,
  "green" : 20, 
}

assert get_results(GAME) == "7 blue, 4 red, 11 green; 2 red, 2 blue, 7 green"
assert get_hands(HAND) == {'blue': 7, 'red': 4, 'green': 11}
assert get_games(RESULTS) == [{'blue': 7, 'red': 4, 'green': 11}, {"red" : 2, "blue" : 2, "green" : 7}]

assert check_game({'blue': 7, 'red': 4, 'green': 11}, LIMITS) == True 
assert check_game({'blue': 21, 'red': 4, 'green': 11}, LIMITS) == False
