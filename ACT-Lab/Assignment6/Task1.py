import random

def activity_selection(start, finish):
    n = len(start)

    # Pair activities and sort by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = []
    last_finish = -1

    for s, f in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected


# ---------- MAIN PROGRAM ----------

N = int(input("Enter number of activities: "))

# Randomly generating start and finish times
start = sorted([random.randint(1, 20) for _ in range(N)])
finish = [s + random.randint(1, 10) for s in start]   # finish > start

print("\nGenerated Start Times:", start)
print("Generated Finish Times:", finish)

selected = activity_selection(start, finish)

print("\nSelected Activities (start, finish):")
for act in selected:
    print(act)

print("\nMaximum Activities =", len(selected))
