# Armstrong.py
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == number

def armstrong_numbers_in_range(start, end):
    return [num for num in range(start, end) if is_armstrong(num)]

# Example usage
if __name__ == "__main__":
    start = 100
    end = 999
    print(armstrong_numbers_in_range(start, end))
