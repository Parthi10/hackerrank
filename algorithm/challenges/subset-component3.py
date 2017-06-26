from itertools import combinations


def get_subsets(num_of_digits, digits):
    for i in range(num_of_digits + 1):
        for combo in combinations(digits, i):
            yield combo


def calc_components(subsets, result=0):
    for subset in subsets:
        component = 64
        if subset:
            for digit in subset:
                component -= (bin(digit).count("1") - 1)
        result += component 
    return result



n = int(input().strip())
d = [int(x) for x in input().strip().split(' ')]
subsets = get_subsets(n, d)
output = calc_components(subsets)
print(output)
