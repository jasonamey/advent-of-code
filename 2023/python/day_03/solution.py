class Solution:
  def __init__(self, path): 
    self.board = self.create_board(path)
    self.checks = [[0 for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
    self.right = len(self.board[0])
    self.bottom = len(self.board)

  def create_board(self,path):
    doc = "" 
    with open(path) as fh:
      doc = fh.read()
    return doc.split("\n")
  
  def is_valid_num(self, y,x): 
    ch_num = ord(self.board[y][x])
    return ch_num >= ord("0") and ch_num <= ord("9")

  def get_num(self, y,x):
    l = 0 
    r = 0 
    while x - l - 1 >= 0 and self.is_valid_num(y,x + l - 1):
      l -= 1
    while x + r + 1 < self.right and self.is_valid_num(y, x + r + 1): 
      r += 1
    num = self.board[y][x + l:x + r + 1]
    self.board[y] = self.board[y][:x + l] +  "".join(["." for _ in range(len(num))]) + self.board[y][x + r+1:]
    return num

  def is_symbol(self,ch):
    return not (ord(ch) >= ord("0") and ord(ch) <= ord("9")) and ord(ch) != ord('.')
  
  def check_point(self,y, x): 
    top_ok = y - 1 >= 0 
    left_ok = x - 1 >= 0 
    right_ok = x + 1 < self.right 
    bottom_ok = y + 1 < self.bottom 
    nums = []
    if top_ok: 
      if self.is_valid_num(y - 1, x):
        nums.append(self.get_num(y-1, x))
      if right_ok and self.is_valid_num(y - 1, x + 1):
        nums.append(self.get_num(y-1, x+1))
      if left_ok and self.is_valid_num(y -1, x - 1): 
        nums.append(self.get_num(y - 1, x - 1))
    if bottom_ok: 
      if self.is_valid_num(y + 1, x):
        nums.append(self.get_num(y + 1, x))
      if right_ok and self.is_valid_num(y + 1, x + 1):
        nums.append(self.get_num(y + 1, x + 1))
      if left_ok and self.is_valid_num(y + 1, x - 1):
        nums.append(self.get_num(y + 1, x - 1))
    if left_ok and self.is_valid_num(y, x - 1): 
      nums.append(self.get_num(y, x - 1))
    if right_ok and self.is_valid_num(y, x + 1):
      nums.append(self.get_num(y, x + 1))
    return nums
  
  def calculate_sums(self): 
    nums = []
    for y in range(len(self.board)): 
      for x in range(len(self.board[0])):
        if self.is_symbol(self.board[y][x]):
          nums += self.check_point(y,x)
    nums = list(map(int, nums))


s = Solution("puzzle.txt")
s.calculate_sums()

