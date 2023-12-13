import random

def create_domino_set():
    domino_set = [[a, b] for b in range(7) for a in range(7) if a <= b]
    while True:
        random.shuffle(domino_set)
        stock_pieces = domino_set[0:14]
        computers_hand = domino_set[14:21]
        players_hand = domino_set[21:28]

        max_double = max(max(computers_hand), max(players_hand))
        if max_double[0] == max_double[1]:
            break
    return stock_pieces, computers_hand, players_hand, max_double

def turn(computers_hand, players_hand,max_double):
    if max_double in computers_hand:
        computers_hand.remove(max_double)
        status = "player"
    else:
        players_hand.remove(max_double)
        status = "computer"
    domino_snake = []
    domino_snake.append(max_double)
    return status, domino_snake

def game():
    stock_pieces, computers_hand, players_hand, max_double = create_domino_set()
    status, domino_snake = turn(computers_hand, players_hand, max_double)
    print("="*70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computers_hand))
    print("")
    print(domino_snake[0])
    print("")
    print("Your pieces:")
    print(*[f'{i + 1}:{e}' for i, e in enumerate(players_hand)], sep='\n')
    print("")
    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
def main():
    game()

if __name__ == "__main__":
    main()