# SLAYER Puzzle Solver

This is my first python project. 


## About
This program helps solve a number puzzle where you find a 6-digit number SLAYER that satisfies the equation:

```bash
SLAYER + SLAYER + SLAYER = LAYERS
```

Each letter represents a unique digit. The challenge is to guess the correct number that fits this equation.



## SLAYER Puzzle
You need to replace the letters **S**, **L**, **A**, **Y**, **E**, and **R** with digits so that the equation holds true.

### Example:
For a guess of **SLAYER** = ```bash 142857 ```, the program checks:
```bash
Solve: SLAYER + SLAYER + SLAYER = LAYERS
What is your guess? 142857
LAYERS = 428571 == SLAYER * 3 -> True
```
Try different guesses to find the correct solution!
