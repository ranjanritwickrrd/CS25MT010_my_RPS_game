import random

CHOICES = ("rock", "paper", "scissors")

def get_player_choice() -> str:
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")

def get_computer_choice() -> str:
    return random.choice(CHOICES)

def decide_winner(player: str, comp: str) -> str:
    if player == comp:
        return "tie"
    winning_pairs = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
    }
    return "player" if (player, comp) in winning_pairs else "computer"

def play_once() -> str:
    player = get_player_choice()
    comp = get_computer_choice()
    print(f"Computer chose: {comp}")
    return decide_winner(player, comp)

def main():
    pprint("Welcome! Rock–Paper–Scissors — No ties allowed!")

    print("Rules: rock > scissors, scissors > paper, paper > rock.")

    while True:
        result = play_once()
        if result == "tie":
            print("It's a tie, let’s play again!\n")
            
            continue
        print(f"{result.capitalize()} wins!")
        break

if __name__ == "__main__":
    main()
