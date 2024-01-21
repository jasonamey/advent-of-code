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
      game_data, answers_data = str_answers.split(":")
      int_game_num = int(game_data.split()[1])
      int_answers = list(map(int, answers_data.strip().split()))
      int_card = sorted(list(map(int,str_card.strip().split())))
      games.append((int_answers, int_card, int_game_num))
    return games
  
  def check_board_part_one(self):
    board_score = 0
    for game in self.board:
      board_score += self.check_game_part_one(game)
    return board_score
      
  def check_game_part_one(self, game): 
    winners = game[0]
    card = game[1]
    game_score = 0 
    for num in winners: 
      if self.search(card, num):
        game_score = 1 if game_score == 0 else game_score * 2
    return game_score

  def check_board_part_two(self):
    score = len(self.board)
    hand_results = {}
    #find all cards just playing first round
    for answers, hand, game_num in self.board: 
      arr = []
      count = 1
      for num in answers: 
        if self.search(hand, num):
          arr.append(game_num + count)
          count += 1
      hand_results[game_num] = arr
    #keep playing until you exhaust all cards 
    second_hand = [ val for val in list(hand_results.values()) if val ]
    while second_hand:
      candidate = second_hand.pop()
      for item in candidate:
        score += 1 
        if item in hand_results: 
          second_hand.append(hand_results[item])
    return score

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
assert s.check_board_part_one() == 23750
assert s.check_board_part_two() == 13261850