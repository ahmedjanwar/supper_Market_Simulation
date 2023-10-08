# supper_Market_Simulation

This Python script simulates a supermarket operation and helps determine the optimal number of cashiers (M) to maximize profit while considering various parameters and customer patience.

## Problem Statement

The supermarket simulation follows these rules:

- The simulation runs for a specified duration (1 hour in this case).
- In each second of the simulation:
  - A random number of customers (0 to N) may enter the market with a given probability (p_in).
  - Each customer stays in the market for a random time within the range [T1, T2] seconds.
  - When a customer finishes shopping, they proceed to one of M cashiers. Each cashier has a queue.
  - Cashiers take a random time within the range [S1, S2] seconds to process a customer.
  - The supermarket earns a profit (phi * S) from each customer and pays the cashier (rho * S).
  - Each customer has patience within the range [P1, P2] seconds. If their patience timer reaches 0 and they are not served, they leave the queue, resulting in a loss (L) for the supermarket.

The goal is to find the value of M (number of cashiers) that maximizes the total profit for the given parameters.

## Code Explanation

### `simulate_supermarket` Function

- Simulates the supermarket operation for a given set of parameters and returns the total profit.
- Given Parameters:
  - `cashers`: List of cashier queues.
  - `p_in`: Probability of customer entry.
  - `N`: Maximum number of customers.
  - `T1` and `T2`: Customer shopping time range.
  - `S1` and `S2`: Cashier processing time range.
  - `profEachCustomer`: Profit per customer.
  - `paidByCustomer`: Cashier cost per customer.
  - `P1` and `P2`: Customer patience range.
  - `L`: Loss for impatient customers.

### Main Loop

- Iterates through different values of M from 1 to 10.
- For each M, initializes cashier queues, runs the simulation using `simulate_supermarket`, and calculates the total profit.
- Stores the profits in the `profits` list.

### Finding the Optimal M

- Identifies the index of the maximum profit in the `profits` list.
- The index corresponds to the optimal value of M that maximizes profit.
- Prints the optimal M value.

## Usage

1. Ensure you have Python installed on your system.

2. Modify the simulation parameters as needed, such as `p_in`, `N`, `T1`, `T2`, etc.

3. Run the script using the Python interpreter:

   ```bash
   python supermarket_simulator.py
