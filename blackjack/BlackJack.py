import random

class BlackJack:
    def __init__(self):
        self.deck = []
        self.suits = ['♠', '♡', '♢', '♣']
        # spade, heart, diamond, clover
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # J, Q, K은 10, A는 필요에 따라 1, 11의 값을 가질 수 있음
        self.score = 0
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append((suit, value))
        random.shuffle(self.deck)

    def deal_initial_hands(self):
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]

    def draw_card(self):
        return self.deck.pop()

    def calculate_score(self, hand):
        score = 0
        num_aces = 0
        for card in hand:
            value = card[1]
            if value.isnumeric():
                score += int(value)
            elif value == 'A':
                score += 11
                num_aces += 1
            else:
                score += 10
        while score > 21 and num_aces > 0:
            score -= 10
            num_aces -= 1
        # 만약 ace값 11을 더해서 21을 초과하게 된다면, ace값을 1로 취급
        return score

    def player_turn(self):
        while True:
            print(f"players cards: {self.player_hand}, current score: {self.calculate_score(self.player_hand)}")
            print(f"Dealer's card: {self.dealer_hand[0]}")
            choice = input("Do you want to draw another card? 'y' or 'n': ")
            if choice == 'y':
                self.player_hand.append(self.draw_card())
                score = self.calculate_score(self.player_hand)
                if score > 21:
                    print(f"You went over 21. You lose! Your final score: {score}")
                    return False
            else:
                return True

    def dealer_turn(self):
        while self.calculate_score(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw_card())
        dealer_score = self.calculate_score(self.dealer_hand)
        print(f"Dealer's cards: {self.dealer_hand}, dealer's score: {dealer_score}")

    def compare_scores(self):
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)
        if player_score > 21:
            print("You went over 21. You lose!")
        elif dealer_score > 21:
            print("Dealer went over 21. You win!")
        elif player_score == dealer_score:
            print("It's a draw!")
        elif player_score > dealer_score:
            print("You win!")
        else:
            print("You lose!")

    def play_game(self):
        print("Welcome to Blackjack!")
        self.create_deck()
        self.deal_initial_hands()
        game_over = self.player_turn()
        if game_over:
            self.dealer_turn()
            self.compare_scores()

        play_again = input("Do you want to play again? 'y' or 'n': ")
        if play_again == 'y':
            self.play_game()
        else:
            print("Thanks for playing!")

def main():
    blackJack = BlackJack()
    blackJack.play_game()
if __name__ == "__main__":
    main()




