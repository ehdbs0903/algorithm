from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
query = [*map(int, input().split())]

card_count = defaultdict(int)

for card in cards:
    card_count[card] += 1

for q in query:
    print(card_count[q], end=' ')
