# トランプのカードデッキ生成
import random

suits = ["♠️", "♥️", "♦️", "♣️"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = []

## 以下組み合わせでカード生成
for i in range(len(suits)):
    for j in range(len(ranks)):
        cards.append(suits[i] + ranks[j])
cards.append("Joker")
print(cards)

## cardsをシャッフルしてdeckに代入
deck = random.sample(cards, len(cards))
print(deck)


# それぞれについて異なる書き方

##　より綺麗になる部分
suits = ["♠️", "♥️", "♦️", "♣️"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = []
for i in suits:
    for j in ranks:
        cards.append(i + j)
cards.append("Joker")
print(cards)

## 面倒だが異なる表現がある部分
deck = cards.copy()
random.shuffle(deck)
print(deck)
