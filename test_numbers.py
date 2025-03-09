
def load_numbers():
    numbers =[798] +[500]*98 +[42]
    return numbers

def find_product_triple(numbers, n):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] * numbers[j] * numbers[k] == n:
                    return (numbers[i], numbers[j], numbers[k])
    return None

def test_load_numbers_first():
    numbers = load_numbers()
    assert numbers[0] == 798, f"Expected first number 798, got {numbers[0]}"

def test_load_numbers_last():
    numbers = load_numbers()
    assert numbers[-1] == 42, f"Expected last number 42, got {numbers[-1]}"

def test_load_numbers_length():
    numbers = load_numbers()
    assert len(numbers) == 100, f"Expected list length 100, got {len(numbers)}"

def test_load_numbers_sum():
    numbers = load_numbers()
    assert sum(numbers) == 50979, f"Expected sum 50979, got {sum(numbers)}"
