# Number divisibility Classifier

This is a Python script designed to practice conditional logic, loop control, and advanced usage of the `range()` function. It takes a custom range from the user and categorizes numbers into different lists based on their divisibility.

## How it works:
1. It initializes four empty lists to store multiples of 5, 10, 20, and 30.
2. It asks the user to define a custom range by entering a `start`, `stop`, and `step` value.
3. It loops through the generated range using a `for` loop.
4. For each number, it uses independent `if` statements and the modulo operator (`%`) to check if the number is perfectly divisible by 5, 10, 20, or 30.
5. Finally, it prints all four categorized lists.

## What I practiced in this project:
- **Advanced `range()` Function:** Utilizing `start`, `stop`, and `step` parameters dynamically based on user input.
- **Independent Conditional Logic:** Using multiple sequential `if` statements instead of `elif` to allow a single number to match multiple conditions.
- **Mathematical Operators:** Mastering the modulo operator (`% == 0`) to determine divisibility and find mathematical multiples.
