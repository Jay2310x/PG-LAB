import random

def job_sequencing(jobs):
    # jobs = [(job_id, deadline, profit)]
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by highest profit

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    job_order = []

    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                job_order.append(job_id)
                break

    return job_order, total_profit


# ---------- MAIN PROGRAM ----------

# Number of jobs
N = int(input("Enter number of jobs: "))

# Randomly generate deadlines and profits
jobs = []
for i in range(1, N+1):
    job_id = f"J{i}"
    deadline = random.randint(1, N)     # deadline between 1 and N
    profit = random.randint(20, 200)    # profit between 20 and 200
    jobs.append((job_id, deadline, profit))

print("\nGenerated Jobs (ID, Deadline, Profit):")
for j in jobs:
    print(j)

# Run job sequencing
order, profit = job_sequencing(jobs)

print("\nScheduled Job Order:", order)
print("Total Profit =", profit)
