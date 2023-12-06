def extract_digits(string):
    # Find the first and last digits in the string
    first_digit = next(filter(str.isdigit, string))
    last_digit = next(filter(str.isdigit, string[::-1]))

    # Combine the first and last digits to form a 2-digit integer
    two_digit_integer = int(first_digit + last_digit)

    return two_digit_integer

# Input file containing strings
file_path = "day1/day1input.txt"

# List to store the extracted 2-digit integers
extracted_integers = []

#Sum of all of the calibration values
sum = 0

try:
    # Read each line from the file and process
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Check if the line is not empty
                two_digit_integer = extract_digits(line)
                extracted_integers.append(two_digit_integer)

    for i in extracted_integers:
        sum += i

    print(sum)

except FileNotFoundError:
    print("File not found. Please check the file path.")