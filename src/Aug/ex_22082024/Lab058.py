# Continue Statement
# Continue statement skips the current iteration of a loop and
# moves to the next iteration.

for number in range(10):
    if number % 2 == 0:
        continue  # even numbers will be skipped --> don't execute current condition and move to next value in loop
    print(number, end=" ")

# pass - can be used in the statement, functions, class & objects