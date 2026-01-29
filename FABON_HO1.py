word = input("Hello! Please enter a word ---> ").title()
strip_word = word.strip()
inputs = []

for i in range (1, len(strip_word) + 1, 1):
    numbers = eval(input("Please enter numbers equal to the amount of letters in the word ---> "))
    inputs.append(numbers)

print(inputs)
print(f"The amount of letters is {len(strip_word)}")
average = sum(inputs) / len(inputs)
print(f"The average of the numbers is {average}")

if average > len(strip_word):
    print("The average is greater than the amount of letters")
else:
    print("The average is less than the amount of letters")
