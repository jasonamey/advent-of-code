from solution import Solution

assert Solution("test.txt").search([1,2,3], 3) == True
assert Solution("test.txt").search([1,2,3,4], 1) == True
assert Solution("test.txt").search([1,2,3,4], 4) == True
assert Solution("test.txt").search([1,2,3], 4) == False
assert Solution("test.txt").search([], 1) == False
assert Solution("test.txt").search([1], 1) == True

assert Solution("test.txt").check_board() == 13