def count_ones(n):
    return bin(n).count('1')

def next_larger_with_same_ones(n):
    target_ones = count_ones(n)
    next_n = n + 1
    while count_ones(next_n) != target_ones:
        next_n += 1
    return next_n

def run_tests():
    test_cases = [5, 6, 7, 1, 31, 0]
    for n in test_cases:
        result = next_larger_with_same_ones(n)
        print(f"{n} -> {result}")
        print(f"{bin(n)} -> {bin(result)}")

if __name__ == "__main__":
    run_tests()
