import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_QUICK_PICKS = int(input("How many quick picks? "))


def generate_quick_pick():
    # Function to generate a sorted quick pick
    quick_pick = []
    while len(quick_pick) < 6:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


for _ in range(NUM_QUICK_PICKS):
    # Generate and display quick picks
    quick_pick = generate_quick_pick()
    print(" ".join(map(str, quick_pick)))