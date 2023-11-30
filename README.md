# HP Lattice Model

An HP 2D Lattice Model for python, based on the hydrophobic-polar two-dimensional lattice model (Lau and Dill's, 1989).

## Requirements

For you to be able to run this program you need python (preferably Python 3.10) and the numpy (preferably Python 1.24) package.

## How to execute

The code is widely commented and any reader with enough python experience, time and attention should be able to understand. But it would be wise to first run the pre-made available codes:

`python src/main.py  data/instances/instance1.dat`

For running the instance in the `instance1.dat` file. The model best solution to this instance will be save under: `data/solutions/instance1-DD-MM-YYYY-HH-MM-SS.dat`

## Directories and Files

Inside `src` folder is all the source code for the project, the file `main.py` holds the main script that creates the model, runs the SA and saves the best model and the `ica.py` has the Simulated Annealing Algorithm.

Everything inside the `src/lib` folder is about the library utils made to fit the HP 2D Lattice models, they should not be ignored in this report because they're very important and all of them must fit the SA algorithm. The library utils were made to be generic enough to be able to run in any heuristic.
