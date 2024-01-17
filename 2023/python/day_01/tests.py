from solution import find_first_int_in_string, find_last_int_in_string, read_file_into_string, get_number_from_string, main

TEST_PATH = "puzzle.txt"
assert type(read_file_into_string(TEST_PATH)) == str

assert find_first_int_in_string('1abc') == '1' 
assert find_first_int_in_string('abc1') == '1' 
assert find_first_int_in_string('1') == '1'
assert find_first_int_in_string('12') == '1'

assert find_last_int_in_string('abc1') == '1'
assert find_last_int_in_string('1abc') == '1'
assert find_last_int_in_string('1') == '1'
assert find_last_int_in_string('21') == '1'

assert get_number_from_string('1abc2') == 12
assert get_number_from_string('1') == 11
assert get_number_from_string('1a3bc2') == 12

SOLUTION_PATH = 'test.txt'
#[1abc2, 1a, a1 , 12abc] // 12 + 11 + 11 + 12 == 46
assert main(SOLUTION_PATH) == 46


