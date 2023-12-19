import math
import re
from collections import Counter
from functools import cmp_to_key

card_value = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

card_value2 = {
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


def hand_sort(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    counter1, counter2 = Counter(hand1), Counter(hand2)

    for (card1, count1), (card2, count2) in zip(counter1.most_common(), counter2.most_common()):
        if count1 == 1 and count2 == 1:
            break

        if count1 > count2:
            return 1
        elif count2 > count1:
            return -1
        else:
            continue

    for card1, card2 in zip(hand1, hand2):
        card1 = int(card1) if card1.isdigit() else card_value[card1]
        card2 = int(card2) if card2.isdigit() else card_value[card2]

        if card1 > card2:
            return 1
        elif card2 > card1:
            return -1
        else:
            continue


def part1(filenum="7"):
    with open(f"../2023/inputs/{filenum}.txt", "r") as f:
        hands = f.read().split("\n")
        hands = [hand.split(" ") for hand in hands]
        hands = [(hand, int(bid)) for hand, bid in hands]

        sorted_hands = sorted(hands, key=cmp_to_key(hand_sort))

        total_winnings = sum(rank * bid for rank, (_, bid) in enumerate(sorted_hands, start=1))

        print(total_winnings)


def hand_sort2(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    counter1, counter2 = Counter(hand1), Counter(hand2)

    value1, _ = counter1.most_common(1)[0]
    value2, _ = counter2.most_common(1)[0]

    if value1 != 'J':
        counter1[value1] += hand1.count('J')
        counter1['J'] = 0

    if value2 != 'J':
        counter2[value2] += hand2.count('J')
        counter2['J'] = 0

    for (card1, count1), (card2, count2) in zip(counter1.most_common(), counter2.most_common()):
        if count1 <= 1 and count2 <= 1:
            break

        if count1 > count2:
            return 1
        elif count2 > count1:
            return -1
        else:
            continue

    for card1, card2 in zip(hand1, hand2):
        card1 = int(card1) if card1.isdigit() else card_value2[card1]
        card2 = int(card2) if card2.isdigit() else card_value2[card2]

        if card1 > card2:
            return 1
        elif card2 > card1:
            return -1
        else:
            continue


def part2(filenum="7"):
    with open(f"../2023/inputs/{filenum}.txt", "r") as f:
        hands = f.read().split("\n")
        hands = [hand.split(" ") for hand in hands]
        hands = [(hand, int(bid)) for hand, bid in hands]

        sorted_hands = sorted(hands, key=cmp_to_key(hand_sort2))

        total_winnings = sum(rank * bid for rank, (_, bid) in enumerate(sorted_hands, start=1))

        print(total_winnings)


if __name__ == "__main__":
    part1()
    part2()