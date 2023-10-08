#TODO: the task is as follows
# Design a supermarket simulator which decides how many cashers are needed to meet the patience of customers.

# The simulator runs in seconds, for every second:

# There is a chance of 𝑝_𝑖𝑛 that [0:N] customers may enter the market. Each customer will stay [𝑇_1,𝑇_2] seconds in the market

# When a customer ends the shopping, he proceeds to one of 𝑀 cashers. Each casher has a customer queue. The casher process the checkout for each customer in S∈[𝑆_1,𝑆_2] second. The profit from this customer is 𝜙𝑆, and the casher is paid 𝜌𝑆. 

# Every customer has a patience of 𝑃∈[𝑃_1,𝑃_2] seconds, and ticks down when he starts to follow a queue. If 𝑃 ticks to 0 and he is still not served. He will leave the queue and the supermarket will lose a profit of 𝐿 (for returning items and a bad reputation).

# [0:N], [𝑇_1,𝑇_2], [𝑆_1,𝑆_2], [𝑃_1,𝑃_2] are uniform distributions.

# Find 𝑀 that the profit is maximized for the following values: 𝑝_𝑖𝑛=0.3, 𝑁=10, 𝑇_1=60, 𝑇_2=300, 𝑆_1=10, 𝑆_2=60, 𝜙=0.1, 𝜌=0.005, 𝑃_1=100, 𝑃_2=200, 𝐿=5.


import random
#The simulation runs for 3600 seconds (1 hour) 
# and calculates the total profit for each value of 𝑀 from 1 to 10. 
# The value of 𝑀 that maximizes the total profit is then returned.
def simulate_supermarket(cashers, p_in, N, T1, T2, S1, S2, profEachCustomer, paidByCustomer, P1, P2, L):
    
    total_profit = 0 #our profit holder varianle

    # we set the range 3600 is in one hr of the work we get this much ,
    # we can adjest it to get more optimistic result like we set it for 1 day
    for i in range(3600):
        # first we Calculate number of customers that enter the market
        num_customers = random.randint(0, N)
        # lets add customers to queue
        for j in range(num_customers):
            customer_time = random.randint(T1, T2)
            customer_patience = random.randint(P1, P2)
            customer_queue = min(range(len(cashers)), key=lambda x: len(cashers[x]))
            cashers[customer_queue].append((customer_time, customer_patience))

        # we process checkout for each casher
        for j in range(len(cashers)):
            if len(cashers[j]) > 0:
                checkout_time = random.randint(S1, S2)
                customer_time, customer_patience = cashers[j][0]
                if customer_patience > checkout_time:
                    # Success customer is served
                    cashers[j].pop(0)
                    profit = profEachCustomer * checkout_time - paidByCustomer * checkout_time
                    total_profit += profit
                else:
                    # Failed customer leaves queue and the market
                    cashers[j].pop(0)
                    total_profit -= L
    return total_profit

# Given simulation parameters
p_in = 0.3 
N = 10
T1 = 60
T2 = 300
S1 = 10
S2 = 60
profEachCustomer = 0.1
paidByCustomer = 0.005
P1 = 100
P2 = 200
L = 5

# We Simulate supermarket for each value of M and we calculate total profit
profits = []
for M in range(1, 11):
    cashers = [[] for i in range(M)]
    profit = simulate_supermarket(cashers, p_in, N, T1, T2, S1, S2, profEachCustomer, paidByCustomer, P1, P2, L)
    profits.append(profit)

# finally Find value of M that maximizes total profit and return it
max_profit_index = profits.index(max(profits))
max_M = max_profit_index + 1

print(f"Value of M that maximizes profit is: {max_M}")
