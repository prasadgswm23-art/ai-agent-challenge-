# Day 3: Practicing Variables, Lists, Loops, and If/Else

# A list of potential client budgets (in USD)
lead_budgets = [500, 3500, 1200, 5000]

# A variable to count how many good clients we find
good_clients = 0

for budget in lead_budgets:
    if budget >= 2000:
        print("High value lead found! Budget:", budget)
        good_clients = good_clients + 1
    else:
        print("Small budget lead. Budget:", budget)

print("Total high-value clients to contact:", good_clients)
