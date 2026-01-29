def unique_pair_sum(numbers, target):
    pairs = set()
    seen = set()

    for num in numbers:
        diff = target - num
        if diff in seen:
            pairs.add((min(num, diff), max(num, diff)))
        seen.add(num)

    return pairs


def main():
    numbers = [1, 2, 3, 4, 3, 5, 6]
    target = 7
    print(unique_pair_sum(numbers, target))


if __name__ == "__main__":
    main()
