# War Card Game

## Overview
This project implements the classic children's card game "War" using Object-Oriented Programming principles. The game will be played between two computer-controlled players. The goal is to simulate the game and determine a winner based on the rules of "War".

## Requirmenets
1. Game rules:
- Each player is dealt half the deck (26 cards each).
- Each turn, both players reveal the top card of their deck:
    - The player with the higher card wins the round and collects both cards.
    - In the case of a tie, "war" is initiated:
        * Each player places three cards face down and one card face up.
        * The player with the higher face-up card wins all cards in the "war".
        *If the face-up cards tie again, repeat the process until a winner is determined.
- The game ends when one player collects all the cards or after a fixed number of rounds (to avoid infinite games).

2. Implementation details:
- Use classes to model the game:
    - **Card**: Represents a single card with a suit and value.
    - **Deck**: Represents a deck of 52 cards, including shuffling and dealing.
    - **Player**: Represents a player with a hand of cards and methods to play and collect cards.
    - **Game**: Manages the game flow, including the rules and rounds.
- The game should automatically run without user input and display the results of each round.

3. Technical requirements:
- Use Python 3.
- Follow Object-oriented Programming principles.
- Use Git for version control.
- Provide clear output to show the progress of the game.

## Task breakdown
- Create the **Card** class
    - Attributes:
        - **rank**: Represents the rank (e.g., "2", "3", ..., "A")
        - **suit**: Represents the suit (e.g., "♠", "♦")
        - **value**: Numerical value for comparison (e.g., 2-14, where Ace is 14)
    - Method:
        - **`__repr__()`**: A string representation, eg., **"7♠"**
- Create the **Deck** class:
    - Attributes:
        - **cards**: A list of 52 **Cards** objects
    -Methods:
        - **shuffle()**: Shuffles the deck
        - **deal_half()**: Splits the deck into two halves (for the two players)
- Test the **Card** and **Deck** classes:
    - Create a small script to:
        - Initialize a deck
        - Shuffle it
        - Deal cards and print a sample output
- Create the **Player** class:
    - Attributes:
        - **hand**: A list of **Card** objects representing the player's cards
    - Methods:
        - **play_card()**: Removes and returns the top cards of the hand
        - **collect_cards(cards)**: Adds cards to the bottom of the hand
        - **has_cards()**: Checks if the player has any cards left
- Create the **Game** class:
    - Attributes:
        - Two **Player** objects
        - Game states variables (e.g., round count, max rounds)
    - Methods:
        - **play_round()**: Executes a single round, including handling "war" logic
        - **play_game()**: Loops through rounds until the game ends
        - **declare_winner()**: Determines and prints the winner
- Write the game logic:
    - Simulate rounds and print the results (e.g, who wins each round and the final winner)

## How to run

1. Clone this repository:
```
git clone https://github.com/tomska888/War---card-game-TC.git
```
2. Navigate to the repository:
```
cd War---card-game-TC.git
```
3. Run the game:
```
python war_game.py
```

## Example output
```
Round 1: Player 1 plays 7♠, Player 2 plays 5♦. Player 1 wins the round.
Round 2: Player 1 plays K♥, Player 2 plays K♣. It's a war!
...
Game Over: Player 1 wins!
```
