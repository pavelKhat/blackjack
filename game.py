
import random
from time import sleep


class Card(object):

    SUITES = ['Club', 'Diamond', 'Heart', 'Spade']

    COST_AND_NAME = [
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 'Ace'),
        (2, 'Jack'),
        (3, 'Queen'),
        (4, 'King'),
    ]

    def __init__(self):
        self.suite = random.choice(self.SUITES)
        random_card = random.choice(self.COST_AND_NAME)
        self.cost, self.name = random_card[0], random_card[1]

    def __add__(self, other):
        return other.cost + self.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.name == other.name and self.suite == other.suite

    def __str__(self):
        return '{} of {}s'.format(self.name, self.suite)

    def __repr__(self):
        return self.__str__()


class Deck(object):

    def __init__(self):

        self.cards = []
        while len(self.cards) < 52:
            card = Card()
            if card not in self.cards:
                self.cards.append(card)
            else:
                continue

    def make_new(self):
        return self.__init__()

    def __str__(self):
        return 'Deck: \n {}'.format(self.cards)


class Player(object):

    def __init__(self, player):
        self.name = player
        self.cards = []
        self.stats = {'Wins': 0, 'Looses': 0, 'Draws': 0}

    def get_card(self, card):
        self.cards.append(card)

    @property
    def score(self):
        return sum(card.cost for card in self.cards)


class Game(object):

    def __init__(self, player):
        self.player = Player(player)
        self.dealer = Player('Alfred')
        self.deck = Deck()

    def deal_single_cart(self, player):
        print('This one more')
        player.cards.append(self.deck.cards.pop(0))
        sleep(1)

    def extra(self):
        choice = ''
        while choice != 'n' and self.player.score <= 21:

            choice = input('One more (y or n): ').strip().lower()

            if choice != 'n' and choice != 'y':
                print('Type - y or on')

            if choice == 'y':
                self.deal_single_cart(self.player)
                print(self.player.cards)
                print('Your score now is {}'.format(self.player.score))
                sleep(1)

        if self.player.score > 21:
            print('You loose!')
            self.player.stats['Looses'] += 1

        else:
            print('Okey! Your score {}! Not bad! :)'.format(self.player.score))
            sleep(1)

            print('==============My turn!')

            while self.dealer.score < 18:
                self.deal_single_cart(self.dealer)
                sleep(1)

            print('Lets see!\nYour score is {player_score}!\nMy score {comp_score}\nThere is my cards\n{comp_cards}!\n'
                  ''.format(player_score=self.player.score, comp_score=self.dealer.score, comp_cards=self.dealer.cards))
            sleep(1)
            if 21 >= self.player.score and (self.dealer.score < self.player.score or self.dealer.score > 21):
                self.player.stats['Wins'] += 1
                print('Congratulations! You win!')
            if 21 >= self.dealer.score and (self.player.score < self.dealer.score or self.player.score > 21):
                self.player.stats['Looses'] += 1
                print('You loose!')
            if self.player.score == self.dealer.score:
                self.player.stats['Draws'] += 1
                print('Draw!')

    def game_again(self):
        choice = ''
        while choice != 'n':

            choice = input('One more game? (y or n): ').strip().lower()
            if choice != 'n' and choice != 'y':
                print('Type - y or on')

            if choice == 'y':
                self.play()

            if choice == 'n':
                break

        print('Yours stats:\n{stats}'.format(stats=self.player.stats))
        print('Have a nice day {player_name}!'.format(player_name=self.player.name))

    def play(self):

        self.deck.make_new()
        self.player.cards = []
        self.dealer.cards = []

        print('Preparing new Deck')

        sleep(1)

        print('Deck is ready! Lets start!\nShuffling Deck!')

        random.shuffle(self.deck.cards)

        sleep(1)

        print('Deck is shuffled! The game is begin!')

        sleep(1)

        for i in range(2):
            print('One for you - one for me!')

            self.player.cards.append(self.deck.cards.pop(0))
            print(self.player.cards)

            self.dealer.cards.append(self.deck.cards.pop(0))
            sleep(1)

        if (self.player.cards[0].name == 'Ace') and (self.player.cards[1].name == 'Ace'):
            print('Bingo! You win!')
            self.player.stats['Wins'] += 1

        else:
            print('Your score {score}'.format(score=self.player.score))
            self.extra()

        self.game_again()

    def __str__(self):
        return ('Hello {name}!\nMy name is {dealer_name}!\nThis is a BlackJack Game!'.
                format(name=self.player.name, dealer_name=self.dealer.name))


if __name__ == '__main__':

    name = ""
    while not name.isalpha():
        name = input('Please enter your name (only US character): ').capitalize()

    game = Game(player=name)

    print(game)

    game.play()

    import sys
    sys.exit()
