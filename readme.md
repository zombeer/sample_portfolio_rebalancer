# Portfolio Rebalancer

## Overview
Sample portfolio rebalancer. It calculates security values, determines allocation percentages, and generates rebalancing orders.

## Installation
Requires `Python3.10` or higher + `pytest` installed. Clone the repo and navigate to the directory:
```bash
git clone https://github.com/zombeer/sample_portfolio_rebalancer.git
cd sample_portfolio_rebalancer
```

## Usage
Modify the `securities`, `current_allocation`, and `desired_allocation` dictionaries in the script. 
Run:
```bash
python portfolio_rebalancer.py
```

## Testing
Run tests using `pytest`:
```bash
pytest
```
