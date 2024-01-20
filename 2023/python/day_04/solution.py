class Solution: 
  def __init__(self, path): 
    self.board = self.prepare_board(path)

  def prepare_board(self,path):
    doc = ""
    with open(path) as fh: 
      doc = fh.read()
    games = []
    for line in doc.split("\n"): 
      str_answers, str_card = line.split("|")
      int_answers = list(map(int, str_answers.split(":")[1].strip().split()))
      int_card = sorted(list(map(int,str_card.strip().split())))
      games.append((int_answers, int_card))
    return games
  
  def check_board(self):
    board_score = 0
    for game in self.board:
      board_score += self.check_game(game)
    return board_score
      
  def check_game(self, game): 
    winners = game[0]
    card = game[1]
    game_score = 0 
    for num in winners: 
      if self.search(card, num):
        game_score = 1 if game_score == 0 else game_score * 2
    return game_score
  
  def search(self, arr, target):
    hi = len(arr) - 1 
    lo = 0
    while (lo <= hi):
      mid = lo + (hi - lo) // 2
      if arr[mid] == target: 
        return True 
      elif arr[mid] > target: 
        hi = mid - 1
      else: 
        lo = mid + 1
    return False

s = Solution("puzzle.txt")
assert s.check_board() == 23750