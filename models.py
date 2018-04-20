from collections import Sequence


class GameVector(Sequence):

    def __init__(self, un, fe, ur):
        self.un = int(un)
        self.fe = int(fe)
        self.ur = int(ur)

    @property
    def items(self):
        return tuple([self.un, self.fe, self.ur])

    def __getitem__(self, i):
        return self.items[i]

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        if type(other) is GameVector:
            return GameVector(
                *(a + b for a, b in zip(self, other))
            )
        else:
            raise SyntaxError

    def __rmul__(self, other):
        return GameVector(
            *(p * other for p in self)
        )

    @property
    def norm(self):
        return sum(self)

    def __repr__(self):
        return "GameVector({},{},{})".format(
            self.un,
            self.fe,
            self.ur
        )


class Card(object):

    def __init__(self, vector, cost, title=""):
        self.vector = vector
        self.cost = int(cost)
        self.title = title

    def __repr__(self):
        return "Card({},{},{},{},{})".format(
            self.vector,
            self.cost,
            self.title
        )


class Deck(Sequence):

    def __init__(self, cards):
        self.cards = tuple(cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]

    @property
    def vector(self):
        return GameVector(
            *(sum(p.vector) for p in zip(*self))
        )

    @property
    def power(self):
        return sum(self.vector)

    def __repr__(self):
        return "Deck({})".format(
            self.cards
        )

