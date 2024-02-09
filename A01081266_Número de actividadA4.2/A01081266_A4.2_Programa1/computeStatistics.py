"""
A01081266 Ejercicio programacion
 The program shall compute all
descriptive statistics from a file containing
numbers.
"""
import sys
import time


#statistic function definitions
# Statistic function definitions
def calculate_sum(numbers):
    """Calculates the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_length(numbers):
    """Calculates the length of a list of numbers."""
    length = 0
    for _ in numbers:
        length += 1
    return length

def mean(numbers):
    """Calculates the mean of a list of numbers."""
    total = calculate_sum(numbers)
    length = calculate_length(numbers)
    return total / length if length != 0 else None

def median(numbers, line_number):
    """Calculates the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    if line_number % 2 == 0 and numbers:
        return (sorted_numbers[line_number // 2 - 1] + sorted_numbers[line_number // 2]) / 2
    return sorted_numbers[line_number // 2] if numbers else None

def mode(numbers):
    """Calculates the mode of a list of numbers."""
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values(), default=0)
    if max_count == 1:
        return None
    mode_values = [num for num, count in counts.items() if count == max_count]
    return mode_values

def calculate_squared_differences(numbers, mean_value):
    """Calculates the sum of squared differences from the mean."""
    total = 0
    for num in numbers:
        total += (num - mean_value) ** 2
    return total

def variance(numbers):
    """Calculates the variance of a list of numbers."""
    mean_value = mean(numbers)
    squared_diff_sum = calculate_squared_differences(numbers, mean_value)
    length = calculate_length(numbers)
    return squared_diff_sum / length if length != 0 else None

def standard_deviation(numbers):
    """Calculates the standard deviation of a list of numbers."""
    return variance(numbers) ** 0.5 if numbers else None


# Read file function definition
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
    return numbers, line_number

# Main function
def main():
    """main function to open the file and call the statistics."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py dataFile.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    numbers, line_number = read_file(file_name)

    if numbers:
        start_time = time.time()

        mean_value = mean(numbers)
        median_value = median(numbers, line_number)
        mode_values = mode(numbers)
        std_deviation_value = standard_deviation(numbers)
        variance_value = variance(numbers)

        end_time = time.time()

        elapsed_time_seconds = end_time - start_time
        elapsed_time_microseconds = elapsed_time_seconds * 1_000_000

        # Print results on screen
        print("Descriptive Statistics:")
        print(f"Mean: {mean_value}")
        print(f"Median: {median_value}")
        print(f"Mode: {mode_values}")
        print(f"Variance: {variance_value}")
        print(f"Standard Deviation: {std_deviation_value}")
        print(f"Elapsed time: {elapsed_time_microseconds} microseconds")

        # Write results to file
        with open("StatisticalResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.write("Descriptive Statistics:\n")
            result_file.write(f"Mean: {mean_value}\n")
            result_file.write(f"Median: {median_value}\n")
            result_file.write(f"Mode: {mode_values}\n")
            result_file.write(f"Variance: {variance_value}\n")
            result_file.write(f"Standard Deviation: {std_deviation_value}\n")
            result_file.write(f"Elapsed time: {elapsed_time_microseconds} "
                              "microseconds\n")
    else:
        print("No valid data found in the file.")

if __name__ == "__main__":
    main()
