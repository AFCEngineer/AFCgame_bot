import random

def generate_deck():
    colors = ["R", "G", "B", "Y"]
    values = list(range(10)) + ["S", "R", "+2"]  # Skip, Reverse, +2
    deck = [f"{c}{v}" for c in colors for v in values] * 2
    wilds = ["WILD", "WILD+4"] * 4
    deck += wilds
    random.shuffle(deck)
    return deck

def validate_move(card, top_card):
    # Check if card matches color, number, or is wild
    return (
        card.startswith("WILD") or
        card[0] == top_card[0] or  # Same color
        card[1:] == top_card[1:]    # Same number/symbol
    )
