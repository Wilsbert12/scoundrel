# Scoundrel

A text-based Python implementation of the card game Scoundrel, playable in the terminal.

## How to play

You move through a dungeon one room at a time. Each room contains 4 cards drawn from a modified deck. On your turn, choose a card to play — each suit has a different effect:

- **Clubs / Spades (black)** — Monsters. They deal damage equal to their rank value. If you have a weapon, you can use it to block some of the damage (up to the weapon's cap).
- **Hearts (red)** — Potions. Heal equal to the card's rank value, up to a max of 20 HP.
- **Diamonds (red)** — Weapons. Equip the card as your weapon. Higher-rank weapons deal more damage but cap out after blocking a hit.

You start with 20 HP. The game ends when the deck runs out (you win) or your HP hits 0 (you lose).

You can also **flee** a room — the remaining cards get shuffled back into the deck. You cannot flee two consecutive rooms.

## Requirements

- Python 3

## Running the game

```
python main.py
```
