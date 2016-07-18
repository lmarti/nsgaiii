# `nsgaiii`: An implementation of NSGA-III in Python

`nsgaiii` is a Python implementation of the selection algorithm of NSGA-III as described in:

* Deb, K., & Jain, H. (2014). An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point-Based Nondominated Sorting Approach, Part I: Solving Problems With Box Constraints. IEEE Transactions on Evolutionary Computation, 18(4), 577–601. doi:10.1109/TEVC.2013.2281535.

`nsgaiii` can be used with -as has been developed relying on- the [DEAP module](https://www.github.com/DEAP/deap).

This code is highly experimental. Contributions and bug fixes are welcome.

## Installation

So far, the only form of installation is to clone the project from GitHub,

```bash
git clone https://github.com/lmarti/nsgaiii.git
```

...and then installing it by running:

```bash
python setup.py install
```

## Demonstration

I have prepared a sample [Jupyter/IPython notebook](http://nbviewer.jupyter.org/github/lmarti/nsgaiii/blob/master/NSGA-III%20in%20Python.ipynb) that illustrates NSGA-III and the use of the module.
