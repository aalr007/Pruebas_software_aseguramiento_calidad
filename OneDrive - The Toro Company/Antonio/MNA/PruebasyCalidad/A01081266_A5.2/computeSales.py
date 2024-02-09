"""
A01081266 Ejercicio programacion 2
The program shall compute the total cost
for all sales included in the second JSON archive.
"""


import json
import sys
import time


def load_json_file(file_path):
    """Open the json files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{file_path}'.")
        return None


def compute_total_cost(product_list, sales_record):
    """compute the cost multiplying price x quantity"""
    total_cost = 0
    for sale in sales_record:
        product = sale['Product']
        quantity = sale['Quantity']
        for item in product_list:
            if item['title'] == product:
                price = item['price']
                total_cost += price * quantity
                break
        else:
            print(f"Error: Product '{product}' not found in the product list.")
    return total_cost


def main():
    """main, it calls the open files and compute."""
    if len(sys.argv) != 3:
        print("Use:python computeSales.py ProductList.json salesRecord.json")
        return

    start_time = time.time()

    product_list_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    product_list = load_json_file(product_list_file)
    sales_record = load_json_file(sales_record_file)

    if product_list is None or sales_record is None:
        return

    total_cost = compute_total_cost(product_list, sales_record)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total cost of sales: ${total_cost:.2f}")
    print(f"Execution time: {execution_time:.2f} seconds")

    with open('SalesResults.txt', 'w', encoding='utf-8') as result_file:
        result_file.write(f"Total cost of sales: ${total_cost:.2f}\n")
        result_file.write(f"Execution time: {execution_time:.2f} seconds\n")


if __name__ == "__main__":
    main()
