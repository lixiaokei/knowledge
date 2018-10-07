"""
扑克游戏
"""
from enum import Enum
from random import shuffle as rshuffle


class Suite(Enum):
    """花色（枚举）"""

    SPADE = 0
    HEART = 1
    CLUB = 2
    DIAMOND = 3

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __str__(self):
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]} {faces[self.face]}'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.suite, self.face))

    def __eq__(self, other):
        return self.suite == other.suite and \
            self.face == other.face


class Poker():
    """扑克"""

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.index = 0

    def shuffle(self):
        """洗牌"""
        self.index = 0
        rshuffle(self.cards)

    @property
    def next_card(self):
        """发牌"""
        temp = self.cards[self.index]
        self.index += 1
        return temp

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """摸牌"""
        self.cards.append(card)

    def make_order(self):
        """整理手上的牌"""
        self.cards.sort(key=lambda card: (card.suite, card.face))


def main():
    """主函数"""  
    card1 = Card(Suite.DIAMOND, 5)
    card2 = Card(Suite.DIAMOND, 5)
    cards = {card1, card2}
    print(len(cards))
    poker = Poker()
    poker.shuffle()
    players = [
        Player('东邪'), Player('西毒'),
        Player('南帝'), Player('北丐')
    ]
    for _ in range(13):
        for player in players:
            if poker.has_more:
                player.get_card(poker.next_card)
    for player in players:
        print(player.name, end=': ')
        player.make_order()
        print(player.cards)


if __name__ == '__main__':
    main()
