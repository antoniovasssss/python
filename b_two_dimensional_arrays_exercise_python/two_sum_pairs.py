def two_sum_pairs(numbers, target):
    pairs = []
    seen = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = sorted([numbers[i], numbers[j]])
                if tuple(pair) not in seen:
                    pairs.append(pair)
                    seen.add(tuple(pair))
    return pairs

print(two_sum_pairs([2, 3, 4, 6, 5], 8))
print(two_sum_pairs([10, 7, 4, 5, 2], 12))
print(two_sum_pairs([3, 9, 8], 11))
print(two_sum_pairs([3, 9, 8], 10))