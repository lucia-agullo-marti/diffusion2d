# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

`diffusion2d` is a Python package that provides a solver for the 2D diffusion equation using finite difference methods.

The implementation simulates heat diffusion in a square plate with the following initial conditions:
- cold square domain with T=300K
- hot circular disc at the center with T=700K

## Installing the package

You can install the package using `pip`:

```bash
pip install martilo_diffusion2d
```

## Running this package
After installation you can run the solver via Python:

```python
from martilo_diffusion2d import solve
solve()
```

## Citing
If you use `diffusion2d` in your work, please cite it as follows:

```makefile
Author: Lucia Agullo Marti
Title: diffusion2d - A 2D diffusion solver in Python
Version: 0.0.1
Repository: https://github.com/lucia-agullo-marti/diffusion2d
```
