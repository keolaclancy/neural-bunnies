# Neural bunnies.

![alt text](https://raw.githubusercontent.com/keolaclancy/neural-bunnies/develop/neural-bunnies-1.png "Neural Bunnies")

## What is this ?
This is my first python project.
I wanted to learn the basics of a neural network system.
So here is a simple game where a bunny has to jump over obstacles.

- You can play the game.
- You can watch bunnies getting better through genetic selection.

## Installation.
### Requirements
- Python > 3.6
- Pygame > 1.9.6 (python3 must be installed)
`python3 -m pip install -U pygame --user`
- Clone the repository to your local environment.
`git clone https://github.com/keolaclancy/neural-bunnies.git`

### Run the script
From inside the cloned folder.

If you want to play the game, run the following command.
`python3 main.py play`

If you want to see the bunnies try their best
`python3 main.py`

## Neural network tweaking.
### Saving a bunny's brain
When a bunny achieves a new high score, his synapses weights
will be outputted in your terminal.

You can copy the output, then in the file `genetic/population.py`

Uncomment the line and set your own values :

`default_synapses = [1.22, 0.030000000000000027, -0.21000000000000002, 1.0, 2.31, 0.010000000000000009, -0.1100000000000001, -1.1400000000000001, -0.97, 1.05, -0.98, 0.11000000000000004, -0.75, 1.25, 1.4100000000000001, -0.9299999999999999, -1.03, 0.33999999999999997, 1.11, -0.029999999999999916]` 


### Change the population size
Edit this value `self.pop_size = 16` at the beginning of genetic/population.py

### Change the mutation factor
todo

