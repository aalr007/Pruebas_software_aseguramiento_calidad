"""
A01081266 Ejercicio programacion
The program shall convert the
numbers to binary and hexadecimal base.
"""
import sys
import time


def convert_to_binary(number):
    """Converts a number to binary."""
    if number == 0:
        return "0b0"
    result = ''
    num = int(number)
    while num > 0:
        result = str(num % 2) + result  #get the digit
        num //= 2   # "right shift" the number to get the next digit
    return "0b" + result


def convert_to_hexadecimal(number):
    """Converts a number to hexadecimal."""
    if number == 0:
        return "0x0"
    result = ''
    num = int(number)
    hex_chars = "0123456789ABCDEF"
    while num > 0:
        result = hex_chars[num % 16] + result   #get the digit
        num //= 16  #"right shift" the number to get the next digit
    return "0x" + result


def read_file(file_name):
    """Reads the file and returns a list of numbers."""
    numbers = []
    line_number = 0

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line_number += 1
                line_stripped = ""
                for char in line:
                    if char in ('\n', '\r'):  # Merge comparisons using 'in'
                        break
                    line_stripped += char
                try:
                    numbers.append(float(line_stripped))
                except ValueError:
                    print(f"Invalid data found: '{line_stripped}' at line: '{line_number}'")
    except FileNotFoundError:
        print("File not found.")
    return numbers


def main():
    """
    main, here we open the file and call the conversions.
    """
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py dataFile.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    numbers = read_file(file_name)

    start_time = time.time()

    if numbers:
        with open("ConversionResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.write("Conversion Results:\n")
            for number in numbers:
                binary_value = convert_to_binary(number)
                hexadecimal_value = convert_to_hexadecimal(number)
                print(f"Number: {number}, Binary: {binary_value}, Hexadecimal: {hexadecimal_value}")
                result_file.write(f"Number: {number}, "
                  f"Binary: {binary_value}, "
                  f"Hexadecimal: {hexadecimal_value}\n")

        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time_microseconds = elapsed_time_seconds * 1_000_000

        print(f"Time elapsed: {elapsed_time_microseconds} microseconds")

        with open("ConversionResults.txt", 'a', encoding='utf-8') as result_file:
            result_file.write(f"Time elapsed: {elapsed_time_microseconds} microseconds\n")

    else:
        print("No valid data found in the file.")

if __name__ == "__main__":
    main()
