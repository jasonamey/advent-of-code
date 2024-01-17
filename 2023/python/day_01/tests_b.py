from solution import is_num, find_num_word_from_front

assert is_num("1") == True
assert is_num("0") == True
assert is_num("a") == False

num_words = ["-", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(1, 10):
  assert find_num_word_from_front(num_words[i]) == i  


