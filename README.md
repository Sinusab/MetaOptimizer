# MetaOptimizer

## Overview
MetaOptimizer is a Python tool for optimizing the production of key metabolites (P, N, Q) 
using linear programming with predefined constraints. The project leverages SciPy's 
optimization library to solve steady-state metabolic flux balance models.

## Features
- Linear programming-based metabolite production optimization
- Incorporates steady-state equality constraints
- Supports variable bounds reflecting biological or process limits
- Outputs optimal flux values and objective function

## Requirements
- Python 3.x
- numpy
- scipy

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Sinusab/MetaOptimizer.git
pip install numpy scipy
