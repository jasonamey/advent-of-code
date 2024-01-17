def read_file_into_string(path): 
    doc = ""
    with open(path) as fh: 
      doc = fh.read()
    return doc.strip()

def is_num(ch): 
  return ord(ch) >= ord('0') and ord(ch) <= ord('9')

def is_word_a_number(ch, str):
  d = {
      "one" : 1, 
      "two" : 2, 
      "three" : 3, 
      "four" : 4, 
      "five" : 5, 
      "six" : 6, 
      "seven" : 7, 
      "eight" : 8, 
      "nine" : 9
  }
  char_to_number = {
      "o" : ["one"], 
      "t" : ["two", "three"],
      "f": ["four", "five"], 
      "s": ["six", "seven"], 
      "e": ["eight"], 
      "n": ["nine"]
  }
  for num_word in char_to_number[ch]:
    if str.find(num_word, 0, len(num_word) + 1) != -1 :
      return d[num_word]
  return -1

def is_this_a_number(ch, str):
    if is_num(ch):
      return int(ch)
    elif ch in "otfsen":
      return is_word_a_number(ch, str)
    return -1 

def find_num_word_from_front(str): 
  i = 0
  while i < len(str):
    test = is_this_a_number(str[i],str[i:])
    if test != -1: 
      return test  
    i += 1 

def find_num_word_from_back(str):
  i = len(str) - 1
  while i > -1: 
    test = is_this_a_number(str[i], str[i:])
    if test != -1: 
      return test 
    i -= 1

def main(path):
  doc = read_file_into_string(path)
  arr = doc.split('\n')
  total = 0
  for word in arr: 
    total += find_num_word_from_front(word) * 10 + find_num_word_from_back(word)
  return total

if __name__ == "__main__":
  path = "puzzle.txt"
  answer = main(path)
  print(answer)