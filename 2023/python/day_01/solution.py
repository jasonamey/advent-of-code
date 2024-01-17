def read_file_into_string(path): 
    doc = ""
    with open(path) as fh: 
      doc = fh.read()
    return doc.strip()

def find_first_int_in_string(str): 
    i = 0 
    str_digit = ord(str[i])
    while str_digit < ord('0') or str_digit > ord('9'):
        i += 1
        str_digit = ord(str[i])
    return chr(str_digit)

def find_last_int_in_string(str):
    i = len(str) - 1 
    str_digit = ord(str[i])
    while str_digit < ord('0') or str_digit > ord('9'):
        i -= 1
        str_digit = ord(str[i])
    return chr(str_digit)

def get_number_from_string(str): 
    return int(find_first_int_in_string(str) + find_last_int_in_string(str))

def main(path): 
    total = 0
    doc = read_file_into_string(path)
    arr = doc.split('\n')
    for word in arr: 
        total += get_number_from_string(word)
    return total 

if __name__ == "__main__":
    puzzle_path = "puzzle.txt"
    answer = main(puzzle_path)
    print(answer)



