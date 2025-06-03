#!/usr/bin/env python3
"""
Comprehensive Calculator Script for DIML Remote Testing
Supports various operations with numbers and strings
Usage: python calculator.py <value1> <value2> <operation>
"""

import sys
import json
import math

def add(a, b):
    """Addition operation"""
    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)  # String concatenation
    return a + b

def subtract(a, b):
    """Subtraction operation"""
    return a - b

def multiply(a, b):
    """Multiplication operation"""
    if isinstance(a, str) and isinstance(b, int):
        return a * b  # String repetition
    elif isinstance(b, str) and isinstance(a, int):
        return b * a  # String repetition
    return a * b

def divide(a, b):
    """Division operation"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    """Power operation"""
    return a ** b

def modulo(a, b):
    """Modulo operation"""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed")
    return a % b

def sqrt(a, b=None):
    """Square root operation (only uses first parameter)"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def max_val(a, b):
    """Maximum value"""
    return max(a, b)

def min_val(a, b):
    """Minimum value"""
    return min(a, b)

def compare(a, b):
    """Compare two values"""
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

def length(a, b=None):
    """Get length of string or list (only uses first parameter)"""
    return len(str(a))

# Available operations
OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'power': power,
    'modulo': modulo,
    'sqrt': sqrt,
    'max': max_val,
    'min': min_val,
    'compare': compare,
    'length': length,
    # Aliases
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': modulo,
    'pow': power,
    'mod': modulo,
    'concat': add,
    'len': length
}

def parse_value(value_str):
    """Parse a string value to appropriate type"""
    # Try to parse as number first
    try:
        if '.' in value_str:
            return float(value_str)
        else:
            return int(value_str)
    except ValueError:
        # If not a number, return as string
        return value_str

def main():
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <value1> <value2> <operation>")
        print("Available operations:", ', '.join(sorted(OPERATIONS.keys())))
        print("\nExamples:")
        print("  python calculator.py 10 5 add")
        print("  python calculator.py 'Hello' ' World' concat")
        print("  python calculator.py 12 3 divide")
        print("  python calculator.py 'Python' 3 multiply")
        sys.exit(1)
    
    try:
        # Parse command line arguments
        value1_str = sys.argv[1]
        value2_str = sys.argv[2]
        operation = sys.argv[3].lower()
        
        # Parse values
        value1 = parse_value(value1_str)
        value2 = parse_value(value2_str)
        
        # Validate operation
        if operation not in OPERATIONS:
            raise ValueError(f"Unknown operation: {operation}. Available: {', '.join(sorted(OPERATIONS.keys()))}")
        
        # Perform calculation
        operation_func = OPERATIONS[operation]
        
        # Some operations only need one parameter
        if operation in ['sqrt', 'length', 'len']:
            result = operation_func(value1)
        else:
            result = operation_func(value1, value2)
        
        # Output result as JSON for easy parsing
        output = {
            "calculation_result": result,
            "execution_details": {
                "operation": operation,
                "value1": value1,
                "value2": value2,
                "value1_type": type(value1).__name__,
                "value2_type": type(value2).__name__,
                "result_type": type(result).__name__,
                "status": "success"
            }
        }
        
        print(json.dumps(output, indent=2))
        
    except Exception as e:
        # Error output
        error_output = {
            "calculation_result": None,
            "execution_details": {
                "operation": operation if 'operation' in locals() else "unknown",
                "value1": value1_str if 'value1_str' in locals() else None,
                "value2": value2_str if 'value2_str' in locals() else None,
                "error": str(e),
                "status": "error"
            }
        }
        print(json.dumps(error_output, indent=2))
        sys.exit(1)

if __name__ == "__main__":
    main()
