import random
import matplotlib.pyplot as plt
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

def cross(p1, p2, p3):
    """Cross product of (p1->p2) x (p1->p3)."""
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def distance(p1, p2, p):
    """Area (as distance from line p1-p2 to point p)."""
    return abs(cross(p1, p2, p))

def side(p1, p2, p):
    """Check which side of line p1-p2 the point lies on."""
    val = cross(p1, p2, p)
    if val > 0: return 1   # left
    if val < 0: return -1  # right
    return 0               # collinear

def hull_set(p1, p2, points, side_flag, hull):
    """Recursive helper for QuickHull / divide & conquer."""
    idx = -1
    max_dist = 0
    for i, p in enumerate(points):
        d = distance(p1, p2, p)
        if side(p1, p2, p) == side_flag and d > max_dist:
            idx = i
            max_dist = d
    if idx == -1:
        hull.append(p1)
        hull.append(p2)
        return
    p = points[idx]
    hull_set(p, p1, points, -side(p, p1, p2), hull)
    hull_set(p, p2, points, -side(p, p2, p1), hull)

def convex_hull(points):
    """Main Divide & Conquer Convex Hull (QuickHull-style)."""
    if len(points) < 3:
        return points

    # 1. Find extreme points
    min_x = min(points, key=lambda p: p.x)
    max_x = max(points, key=lambda p: p.x)

    hull = []

    # 2. Split into two halves and recurse
    hull_set(min_x, max_x, points, 1, hull)
    hull_set(min_x, max_x, points, -1, hull)

    # Remove duplicates and order hull CCW
    hull = list(set(hull))
    hull.sort(key=lambda p: (p.x, p.y))

    # Graham-like ordering for proper polygon traversal
    center_x = sum(p.x for p in hull) / len(hull)
    center_y = sum(p.y for p in hull) / len(hull)
    hull.sort(key=lambda p: math.atan2(p.y - center_y, p.x - center_x))

    return hull

# -------------------------------
# Run and plot
# -------------------------------
def generate_random_points(n, seed=42):
    random.seed(seed)
    return [Point(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

if __name__ == "__main__":
    n = int(input("Enter number of points (>=3): "))
    points = generate_random_points(n)

    hull = convex_hull(points)

    print("Convex Hull Points:")
    for p in hull:
        print(p)

    plt.figure(figsize=(7, 7))
    # All points
    plt.scatter([p.x for p in points], [p.y for p in points], color="blue", label="Points")

    # Convex hull edges
    hx = [p.x for p in hull] + [hull[0].x]
    hy = [p.y for p in hull] + [hull[0].y]
    plt.plot(hx, hy, "r-", linewidth=2, label="Convex Hull")

    # Convex hull points highlighted
    plt.scatter([p.x for p in hull], [p.y for p in hull],
                color="green", s=100, marker="o", edgecolors="black", label="Hull Points")

    # Annotate convex hull points
    for p in hull:
        plt.text(p.x + 1, p.y + 1, f"({p.x:.1f},{p.y:.1f})", fontsize=8, color="darkgreen")

    # Title with total number of points
    plt.title(f"Convex Hull (Total Points: {n})")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect("equal", adjustable="box")

    # Save for Codespaces
    plt.savefig("ACT-Lab/convex_hull.png")
    print("✅ Plot saved as ACT-Lab/convex_hull.png")
