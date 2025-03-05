# calculator.py

import logging

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"Dividing {a} / {b} = {result}")
    return result


#pytest test_calculator.py -v --tb=short --log-cli-level=INFO | tee test_results.log