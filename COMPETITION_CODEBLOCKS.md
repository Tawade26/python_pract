# Python competition codeblocks

These patterns come from `rev6.py` through `rev23.py`, the six problems in
`sample problems/programming_competition_problems.md`, and the images in
`sample problems/`. The six complete answers are independent programs; the
smaller snippets use named placeholder variables and are meant to be adapted.
Use Python 3.

The written six-problem set expects **standard input and exact standard
output**, with no prompts. Some photographed problems explicitly ask for an
interactive prompt or `input.txt`/`output.txt`; follow the format of the actual
contest question. `collections`, `heapq`, and `bisect` are Python standard
library modules, not third-party packages. If the organizers really allow
imports from only the four *named* modules, confirm whether `heapq` and
`bisect` are permitted before using those two blocks.

## 1. The five lines to memorize

```python
import sys
input = sys.stdin.readline              # Fast line input; keeps trailing newline
n, q = map(int, input().split())          # Parse space-separated integers
parts = input().split()                   # Parse a command, regardless of spacing
print(f"{value:.2f}")                    # Exactly two decimal places
```

For large output, collect lines and write once:

```python
out = []
out.append("ANSWER")
sys.stdout.write("\n".join(out))
```

`split()` handles multiple spaces and tabs. `split(' ')` may create empty
tokens. Never use `input("Enter ...")` unless the required output explicitly
includes that prompt. For numbers, use `//` for integer division; `/` creates
a float.

## 2. Small reusable patterns

### Count values; find entries occurring exactly once

For the photographed *sum of unique integers* problem (`set()` prohibited):

```python
from collections import Counter

numbers = list(map(int, input().split()))
freq = Counter(numbers)
answer = sum(x for x, count in freq.items() if count == 1)
print(answer)
```

If the integers may span lines, read all tokens after the count:

```python
import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
numbers = data[1:1 + n]
```

### Keep the best answer with a tie rule

Compare tuples: larger score wins; for equal scores, smaller ID wins.

```python
best_key = None
best_name = None
for student_id, name, total_score in students:
    key = (total_score, -student_id)
    if best_key is None or key > best_key:
        best_key = key
        best_name = name
```

Initialize the best value **before** the loop. In `rev20.py`, `top_ave` and
`top_stud` are reset for every student, so only the last student can survive.
For three exam scores, comparing integer totals also avoids unnecessary
floating-point tie comparisons.

### Dictionary for item lookup and updates

```python
stock = {"KB01": 10, "MS02": 3}
code = "KB01"
amount = 7
if code in stock and stock[code] >= amount:
    stock[code] -= amount
    print("ACCEPTED")
else:
    print("REJECTED")
```

`code in stock` is typically O(1). Scanning every product for every command
is O(NQ). Parse a command with `parts = input().split()`; `parts[1]` is the
whole code, while `input()[1]` is only one character.

### Max consecutive run in a list or string

For *strictly increasing by exactly one*:

```python
best = run = 0
for i, x in enumerate(values):
    run = run + 1 if i == 0 or x == values[i - 1] + 1 else 1
    best = max(best, run)
print(best)
```

For *adjacent characters must differ*, replace the condition with
`i == 0 or x != text[i - 1]`. Both handle an empty input by printing 0.
These are O(N) time and O(1) extra space.

### Count the maximum number of balanced A/B blocks

Each return of the running balance to zero ends one block. Characters left
after the last return do not form a block.

```python
balance = blocks = 0
for ch in text:
    balance += 1 if ch == "A" else -1
    if balance == 0:
        blocks += 1
print(blocks)
```

For an interactive version, validate with
`if not text or any(ch not in "AB" for ch in text): ...` before counting.

### Count/filter an inclusive range

For the photographed *numbers without digit 5* problem, including negatives:

```python
start, end = map(int, input().split())
valid = [x for x in range(start, end + 1) if "5" not in str(x)]
print(len(valid))
```

`str(-15)` includes `5`, as required. This is suitable when the range is
small enough to enumerate. If the problem gives huge endpoints, use digit DP.
Print the list as well only if the required output asks for it.

### Substitution and base conversion

```python
def shift_char(ch):
    if "A" <= ch <= "Z":
        return chr(ord("A") + (ord(ch) - ord("A") + 3) % 26)
    if "a" <= ch <= "z":
        return chr(ord("a") + (ord(ch) - ord("a") - 2) % 26)
    if "0" <= ch <= "9":
        return str((int(ch) + 4) % 10)
    return ch

encrypted = "".join(shift_char(ch) for ch in text)
```

If the cipher question specifies files:

```python
with open("input.txt", encoding="utf-8") as f:
    text = f.read()
encrypted = "".join(shift_char(ch) for ch in text)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(encrypted)
```

The photographed Zarnox digits `A`–`G` represent base-7 digits 0–6:

```python
s = input().strip().upper()
if not s or any(ch not in "ABCDEFG" for ch in s):
    print("INVALID")
else:
    value = 0
    for ch in s:
        value = value * 7 + (ord(ch) - ord("A"))
    print(value)
    print(format(value, "b"))
    print(format(value, "o"))
    print(format(value, "x"))
```

For the photographed hexadecimal message, each pair is a byte shifted by 3:

```python
hex_text = input().strip()
message = "".join(chr(int(hex_text[i:i + 2], 16) - 3)
                  for i in range(0, len(hex_text), 2))
print(message)
```

### Arithmetic and simple simulations

```python
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_armstrong(n):
    digits = str(n)
    return n == sum(int(ch) ** len(digits) for ch in digits)

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
```

The leap rule handles 1900 (false) and 2000 (true). `collatz_steps(1)` is 0;
starting with an unconditional loop incorrectly adds a step. `rev13.py`
checks divisibility by 4 first, so it incorrectly accepts 1900.

### Hollow rectangle as a returned string

The photographed problem requests CRLF after **every** row, including the
last. This also handles width 1 and height 1.

```python
def rectangle(width, height):
    rows = []
    for y in range(height):
        if y == 0 or y == height - 1 or width <= 2:
            rows.append("*" * width)
        else:
            rows.append("*" + " " * (width - 2) + "*")
    return "\r\n".join(rows) + "\r\n"
```

### Insert `+`, `-`, or `*` between digits, with normal precedence

The `last` value lets multiplication replace the last term. This avoids
`eval()` and produces all valid expressions in O(3^(digits-1)) time.

```python
def expressions(digits, target):
    answers = []
    if not digits:
        return answers

    def dfs(i, expr, total, last):
        if i == len(digits):
            if total == target:
                answers.append(expr)
            return
        x = int(digits[i])
        dfs(i + 1, expr + "+" + digits[i], total + x, x)
        dfs(i + 1, expr + "-" + digits[i], total - x, -x)
        dfs(i + 1, expr + "*" + digits[i], total - last + last * x, last * x)

    first = int(digits[0])
    dfs(1, digits[0], first, first)
    return answers

print(*expressions("123", 6), sep="\n")
```

### First 1000 recursive 123-numbers

The pictured definition says that every digit must be 1, 2, or 3, and the
count of each *present* digit must itself be a 123-number. Generate candidates
by digit length and numeric order. Do not stop generating children of an
invalid candidate; a longer number may become valid.

```python
from collections import deque

memo = {1: True, 2: True, 3: True}

def is_123(n):
    if n in memo:
        return memo[n]
    s = str(n)
    if any(ch not in "123" for ch in s):
        memo[n] = False
    else:
        memo[n] = all(is_123(s.count(ch)) for ch in "123" if ch in s)
    return memo[n]

queue = deque(["1", "2", "3"])
answers = []
while len(answers) < 1000:
    s = queue.popleft()
    if is_123(int(s)):
        answers.append(s)
    for ch in "123":
        queue.append(s + ch)
print(*answers, sep="\n")
```

## 3. Complete answers for the six written practice problems

Each block below is a standalone program. Use these as typing drills: hide
the block, solve the problem, then compare your result and time complexity.

### Problem 1: Digital Wallet Tracker — O(N)

```python
import sys
input = sys.stdin.readline

balance = int(input())
n = int(input())
successful = rejected = 0
for _ in range(n):
    kind, amount = input().split()
    amount = int(amount)
    if kind == "D":
        balance += amount
        successful += 1
    elif balance >= amount:
        balance -= amount
        successful += 1
    else:
        rejected += 1

print(f"Balance: {balance}")
print(f"Successful: {successful}")
print(f"Rejected: {rejected}")
```

### Problem 2: Student Performance Analyzer — O(N)

```python
import sys
input = sys.stdin.readline

n = int(input())
passed = total_all = 0
best_key = None
best_name = ""
out = []
for _ in range(n):
    parts = input().split()
    student_id, name = int(parts[0]), parts[1]
    total = sum(map(int, parts[2:5]))
    passed_now = total >= 225
    passed += passed_now
    total_all += total
    key = (total, -student_id)
    if best_key is None or key > best_key:
        best_key, best_name = key, name
    status = "PASSED" if passed_now else "FAILED"
    out.append(f"{student_id} {name} {total / 3:.2f} {status}")

out.append(f"TOP STUDENT: {best_name}")
out.append(f"PASSED: {passed}")
out.append(f"CLASS AVERAGE: {total_all / (3 * n):.2f}")
sys.stdout.write("\n".join(out))
```

### Problem 3: Inventory Restocking System — O(N log N + QN)

Reports must inspect products, so the worst case has Q reports. Sorting
codes once avoids sorting for every report.

```python
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
stock = {}
minimum = {}
for _ in range(n):
    code, have, need = input().split()
    stock[code] = int(have)
    minimum[code] = int(need)

codes = sorted(stock)
out = []
for _ in range(q):
    parts = input().split()
    if parts[0] == "RESTOCK":
        out.append("RESTOCK REPORT")
        found = False
        for code in codes:
            gap = minimum[code] - stock[code]
            if gap > 0:
                out.append(f"{code} {gap}")
                found = True
        if not found:
            out.append("ALL STOCKS SUFFICIENT")
        continue

    kind, code, amount = parts[0], parts[1], int(parts[2])
    if code not in stock or (kind == "SELL" and stock[code] < amount):
        out.append("REJECTED")
    else:
        stock[code] += amount if kind == "ADD" else -amount
        out.append("ACCEPTED")

sys.stdout.write("\n".join(out))
```

### Problem 4: Circular Seating Arrangement — O(N + Q)

`offset` is the initial index now displayed at position 0. Keep each ID's
initial index in a dictionary. Never rotate a 100,000-element list for every
command.

```python
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
ids = list(map(int, input().split()))
original_index = {person: i for i, person in enumerate(ids)}
offset = 0
out = []
for _ in range(q):
    operation, value = input().split()
    value = int(value)
    if operation == "R":
        offset = (offset - value) % n
    elif operation == "L":
        offset = (offset + value) % n
    else:
        position = (original_index[value] - offset) % n + 1
        out.append(f"POSITION: {position}")

final_order = ids[offset:] + ids[:offset]
out.append("FINAL: " + " ".join(map(str, final_order)))
sys.stdout.write("\n".join(out))
```

### Problem 5: Emergency Network Routing — O((N + M) log N)

All road weights are positive, so Dijkstra works. Normalize a closed road's
endpoints so `u v` and `v u` name the same undirected road. Keep only a heap
of `(distance, station)` pairs; stale entries are skipped.

```python
import sys
from heapq import heappop, heappush
input = sys.stdin.buffer.readline

n, m, k = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
closed = set()
for _ in range(k):
    u, v = map(int, input().split())
    closed.add((min(u, v), max(u, v)))
start, destination = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for u, v, weight in roads:
    if (min(u, v), max(u, v)) in closed:
        continue
    graph[u].append((v, weight))
    graph[v].append((u, weight))

dist = [float("inf")] * (n + 1)
ways = [0] * (n + 1)
dist[start] = 0
ways[start] = 1
heap = [(0, start)]
MOD = 1_000_000_007

while heap:
    current, u = heappop(heap)
    if current != dist[u]:
        continue
    for v, weight in graph[u]:
        new_dist = current + weight
        if new_dist < dist[v]:
            dist[v] = new_dist
            ways[v] = ways[u]
            heappush(heap, (new_dist, v))
        elif new_dist == dist[v]:
            ways[v] = (ways[v] + ways[u]) % MOD

if dist[destination] == float("inf"):
    print("NO ROUTE")
else:
    print(f"SHORTEST TIME: {dist[destination]}")
    print(f"NUMBER OF SHORTEST ROUTES: {ways[destination]}")
```

### Problem 6: Maximum Profit from Scheduled Jobs — O(N log N)

Sort by finish time. `bisect_right(finishes, start, 0, i - 1)` gives the
number of earlier jobs finishing no later than this job starts. Store
`(profit, -job_count)` so tuple comparison applies both tie rules.

```python
import sys
from bisect import bisect_right
input = sys.stdin.buffer.readline

n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort(key=lambda job: job[1])
finishes = [finish for start, finish, profit in jobs]
dp = [(0, 0)] * (n + 1)

for i, (start, finish, profit) in enumerate(jobs, 1):
    compatible_count = bisect_right(finishes, start, 0, i - 1)
    previous_profit, previous_negative_count = dp[compatible_count]
    take = (previous_profit + profit, previous_negative_count - 1)
    dp[i] = max(dp[i - 1], take)

print(f"MAXIMUM PROFIT: {dp[n][0]}")
print(f"MINIMUM JOBS: {-dp[n][1]}")
```

## 4. Additional patterns from the photographed problems

### Circular fuel route — O(N)

If total fuel is negative, no starting position works. If a running segment
becomes negative at `i`, no point from the current candidate through `i` can
work; try `i + 1`.

```python
fuel = [4, -5, 3, 2, -1]
total = current = candidate = 0
for i, amount in enumerate(fuel):
    total += amount
    current += amount
    if current < 0:
        candidate = i + 1
        current = 0
answer = candidate % len(fuel) if total >= 0 else -1
print(answer)
```

### Breadth-first search for an unweighted graph — O(N + M)

```python
from collections import deque

distance = [-1] * (n + 1)
distance[start] = 0
queue = deque([start])
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if distance[v] == -1:
            distance[v] = distance[u] + 1
            queue.append(v)
```

### Prefix sums for many range-sum queries — O(N + Q)

For zero-based inclusive `[left, right]`:

```python
prefix = [0]
for x in values:
    prefix.append(prefix[-1] + x)
answer = prefix[right + 1] - prefix[left]
```

### Binary search for the first value at least `target` — O(log N)

Works on an already sorted list. This version needs no import.

```python
lo, hi = 0, len(values)
while lo < hi:
    mid = (lo + hi) // 2
    if values[mid] < target:
        lo = mid + 1
    else:
        hi = mid
index = lo
```

### Sliding window: longest range with sum at most `limit` — O(N)

This version requires **nonnegative** values and a nonnegative limit. Shrink
from the left until the range is valid again.

```python
left = total = best = 0
for right, x in enumerate(values):
    total += x
    while total > limit:
        total -= values[left]
        left += 1
    best = max(best, right - left + 1)
```

### Quick combinations and products

Useful when the search space is small. `permutations` respects order;
`combinations` does not. A Cartesian product chooses one option at each step.

```python
from itertools import permutations, combinations, product

for order in permutations(items, 2):
    print(order)
for pair in combinations(items, 2):
    print(pair)
for operations in product("+-*", repeat=3):
    print(operations)
```

### Grid neighbors and flood fill — O(rows × columns)

```python
from collections import deque

rows, cols = len(grid), len(grid[0])
seen = [[False] * cols for _ in range(rows)]
queue = deque([(start_row, start_col)])
seen[start_row][start_col] = True
while queue:
    row, col = queue.popleft()
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if not seen[nr][nc] and grid[nr][nc] != "#":
                seen[nr][nc] = True
                queue.append((nr, nc))
```

## 5. Quick checks before submitting

- Match capitalization, punctuation, spaces, and decimal places exactly.
- Check zero, one item, ties, unavailable items, large rotations, and negative
  profits where choosing no job is best.
- Check the largest constraints before choosing repeated list scans or rotations.
- In `rev23.py`, `int(input().split())` is invalid: use
  `list(map(int, input().split()))` or tuple unpacking.
- In `rev22.py`, `x[2]` only reads one character of a number; split the line.
  The shown loop also rotates the opposite way for `R` and `L` and takes O(K)
  time per rotation.
- In `rev19.py`, debug prints and prompts break exact output comparison.
- For the photographed problems with prompts, copy the requested prompt text
  literally. For the written six-problem set, print no prompts.
