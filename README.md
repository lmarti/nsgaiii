# `nsgaiii`: Understanding the Implementation of NSGA-III in Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lmarti/nsgaiii/blob/master/NSGA-III%20in%20Python.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/lmarti/nsgaiii/blob/master/NSGA-III%20in%20Python.ipynb)

A Python implementation of the NSGA-III selection algorithm as described in:

- Deb, K., and Jain, H. (2014). *An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point-Based Nondominated Sorting Approach, Part I: Solving Problems With Box Constraints*. IEEE Transactions on Evolutionary Computation, 18(4), 577–601. doi: [10.1109/TEVC.2013.2281535](https://ieeexplore.ieee.org/document/6600851).
- Jain, H. and Deb, K. (2014). *An Evolutionary Many-Objective Optimization Algorithm Using Reference-Point Based Nondominated Sorting Approach, Part II: Handling Constraints and Extending to an Adaptive Approach*. IEEE Transactions on Evolutionary Computation, 18(4), 602-622. doi: [10.1109/TEVC.2013.2281534](https://ieeexplore.ieee.org/document/6595567).

`nsgaiii` can be used with -as has been developed relying on- the [DEAP module](https://www.github.com/DEAP/deap).

This code is highly experimental. Contributions and bug fixes are welcome.

⚠️ **Important notice:** The `nsgaiii` code has been integrated in [DEAP](https://github.com/DEAP/deap) as their function [`selNSGA3`](https://github.com/DEAP/deap/blob/master/deap/tools/emo.py#L492). I recommend you use that implementation as it is actively maintained.

## Demonstration

I have prepared a sample [Jupyter/IPython notebook](http://nbviewer.jupyter.org/github/lmarti/nsgaiii/blob/master/NSGA-III%20in%20Python.ipynb) that illustrates NSGA-III.

## Installation

So far, the only form of installation is to clone the project from GitHub,

```bash
git clone https://github.com/lmarti/nsgaiii.git
```

...and then installing it by running:

```bash
python setup.py install
```
