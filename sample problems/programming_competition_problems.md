# Python Programming Competition: Six Practice Problems

For IT Skills Olympics 2026 preparation. These are draft practice problems, not verified official UMak questions.

| # | Problem | Difficulty | Main skill |
|---|---|---|---|
| 1 | Digital Wallet Tracker | Easy | Simulation |
| 2 | Student Performance Analyzer | Easy | Aggregation and tie-breaking |
| 3 | Inventory Restocking System | Average | Inventory tracking |
| 4 | Circular Seating Arrangement | Average | Rotation and indexing |
| 5 | Emergency Network Routing | Difficult | Shortest paths and route counting |
| 6 | Maximum Profit from Scheduled Jobs | Difficult | Dynamic programming and binary search |

Each program reads from standard input and writes to standard output. Match the specified output exactly; do not print prompts.

---

## Problem 1: Digital Wallet Tracker

**Difficulty:** Easy · **Time limit:** 1 second · **Memory limit:** 64 MB

### Task

A wallet starts with balance `B`. Process `N` transactions in order:

- `D A`: deposit `A` into the wallet.
- `W A`: withdraw `A` if the current balance is at least `A`.

A withdrawal that exceeds the current balance is rejected and does not change the balance. Count successful and rejected transactions, then report the final balance.

### Input

1. An integer `B`: the initial balance.
2. An integer `N`: the number of transactions.
3. `N` lines, each containing a transaction type (`D` or `W`) and an amount `A`.

### Output

Print exactly three lines:

```text
Balance: X
Successful: Y
Rejected: Z
```

`X` is the final balance, `Y` is the number of successful transactions, and `Z` is the number of rejected transactions.

### Constraints

- `0 ≤ B ≤ 100000`
- `1 ≤ N ≤ 1000`
- `1 ≤ A ≤ 50000`

### Example

**Input**

```text
1000
5
D 500
W 200
W 1500
D 300
W 400
```

**Output**

```text
Balance: 1200
Successful: 4
Rejected: 1
```

The withdrawal of 1500 is rejected because only 1300 is available at that point.

---

## Problem 2: Student Performance Analyzer

**Difficulty:** Easy · **Time limit:** 1 second · **Memory limit:** 64 MB

### Task

Each student has a unique ID, a name, and three exam scores. Calculate each student's average and mark them `PASSED` if their average is at least 75; otherwise mark them `FAILED`.

Also report the student with the highest average, the number who passed, and the average across all students. If students tie for the highest average, choose the one with the smallest ID.

### Input

1. An integer `N`: the number of students.
2. `N` lines, each containing `ID NAME SCORE1 SCORE2 SCORE3`. Names contain no spaces.

### Output

For each student, in input order, print:

```text
ID NAME AVERAGE STATUS
```

Then print:

```text
TOP STUDENT: NAME
PASSED: COUNT
CLASS AVERAGE: AVERAGE
```

Display every average with exactly two decimal places.

### Constraints

- `1 ≤ N ≤ 1000`
- `1 ≤ ID ≤ 100000`; all IDs are unique.
- `0 ≤ SCORE ≤ 100`

### Example

**Input**

```text
4
103 Ana 90 85 95
101 Ben 80 75 85
104 Cara 60 70 65
102 Dan 90 90 90
```

**Output**

```text
103 Ana 90.00 PASSED
101 Ben 80.00 PASSED
104 Cara 65.00 FAILED
102 Dan 90.00 PASSED
TOP STUDENT: Dan
PASSED: 3
CLASS AVERAGE: 81.25
```

Ana and Dan both average 90, so Dan wins the tie with the smaller ID, 102.

---

## Problem 3: Inventory Restocking System

**Difficulty:** Average · **Time limit:** 2 seconds · **Memory limit:** 128 MB

### Task

Each product has a unique code, a current stock quantity, and a minimum stock requirement. Process these commands in order:

- `ADD CODE QUANTITY`: increase stock. Accept only if the code exists.
- `SELL CODE QUANTITY`: decrease stock. Accept only if the code exists and enough stock is available.
- `RESTOCK`: list every product whose stock is below its minimum. Sort the list by product code. The quantity needed is `minimum − current stock`.

Rejected commands do not change stock.

### Input

1. Two integers `N Q`: the number of products and commands.
2. `N` lines, each containing `CODE INITIAL_STOCK MINIMUM_STOCK`.
3. `Q` lines, each containing one command.

### Output

- For each `ADD` or `SELL`, print `ACCEPTED` or `REJECTED`.
- For each `RESTOCK`, print `RESTOCK REPORT`, followed by one `CODE QUANTITY_NEEDED` line per product that needs stock.
- If none need stock, print `ALL STOCKS SUFFICIENT` immediately after `RESTOCK REPORT`.

Do not print a column-heading line in a report.

### Constraints

- `1 ≤ N ≤ 1000`
- `1 ≤ Q ≤ 5000`
- Product codes contain uppercase letters and digits and are unique.
- `0 ≤ INITIAL_STOCK ≤ 100000`
- `1 ≤ MINIMUM_STOCK ≤ 100000`
- `1 ≤ QUANTITY ≤ 100000`

### Example

**Input**

```text
3 6
KB01 10 5
MS02 3 8
MN03 15 10
SELL KB01 7
ADD MS02 2
RESTOCK
SELL MS02 10
ADD MN03 5
RESTOCK
```

**Output**

```text
ACCEPTED
ACCEPTED
RESTOCK REPORT
KB01 2
MS02 3
REJECTED
ACCEPTED
RESTOCK REPORT
KB01 2
MS02 3
```

After the sale, `KB01` has 3 units and needs 2 more. `MS02` has 5 units and needs 3 more. The attempted sale of 10 units of `MS02` is rejected, so the second report is unchanged for those two products.

---

## Problem 4: Circular Seating Arrangement

**Difficulty:** Average · **Time limit:** 2 seconds · **Memory limit:** 128 MB

### Task

`N` participants with unique IDs are arranged in a circle. Treat the given list as the current displayed order. Process `Q` operations:

- `R K`: rotate the displayed order right by `K` positions.
- `L K`: rotate the displayed order left by `K` positions.
- `F ID`: report the participant's current position, numbered from 1 to `N` in the displayed order.

Rotations preserve relative order. Rotating by a multiple of `N` leaves the displayed order unchanged.

### Input

1. Two integers `N Q`.
2. `N` distinct participant IDs in their initial displayed order.
3. `Q` lines, each containing an operation.

Every `F` operation references an existing participant.

### Output

For each `F` operation, print:

```text
POSITION: P
```

After all operations, print:

```text
FINAL: ID1 ID2 ... IDN
```

### Constraints

- `1 ≤ N ≤ 100000`
- `1 ≤ Q ≤ 100000`
- `1 ≤ ID ≤ 10^9`; all IDs are unique.
- `0 ≤ K ≤ 10^9`

### Example

**Input**

```text
5 5
10 20 30 40 50
R 2
F 40
L 1
F 10
R 7
```

**Output**

```text
POSITION: 1
POSITION: 2
FINAL: 30 40 50 10 20
```

After `R 2`, the order is `40 50 10 20 30`. After `L 1`, it is `50 10 20 30 40`. Finally, `R 7` has the same effect as `R 2` because `7 mod 5 = 2`.

---

## Problem 5: Emergency Network Routing

**Difficulty:** Difficult · **Time limit:** 3 seconds · **Memory limit:** 256 MB

### Task

`N` emergency stations are connected by `M` two-way roads. Each road has a positive travel time. Some roads are closed and cannot be used.

Find the shortest travel time from station `S` to station `D` and count the different shortest routes, modulo `1,000,000,007`. Two routes are different if their sequences of stations differ. If `D` cannot be reached, print `NO ROUTE`.

There is at most one road between any pair of stations.

### Input

1. Three integers `N M K`: stations, roads, and closed roads.
2. `M` lines, each containing `U V W`: a two-way road with travel time `W`.
3. `K` lines, each containing `U V`: the endpoints of a closed road.
4. One line containing `S D`.

Every listed closed road exists in the original network.

### Output

If a route exists, print:

```text
SHORTEST TIME: T
NUMBER OF SHORTEST ROUTES: C
```

Otherwise, print:

```text
NO ROUTE
```

### Constraints

- `2 ≤ N ≤ 100000`
- `1 ≤ M ≤ 200000`
- `0 ≤ K ≤ M`
- `1 ≤ U, V, S, D ≤ N`; `U ≠ V`.
- `1 ≤ W ≤ 10^9`

### Example

**Input**

```text
5 6 1
1 2 2
1 3 2
2 4 3
3 4 3
2 5 5
4 5 2
2 4
1 5
```

**Output**

```text
SHORTEST TIME: 7
NUMBER OF SHORTEST ROUTES: 2
```

The road `2–4` is closed. Both `1 → 2 → 5` and `1 → 3 → 4 → 5` take 7 minutes.

### Suggested approach

Use Dijkstra's algorithm with a priority queue, skipping closed roads. Track `dist[v]` and `ways[v]`. On a shorter path, replace both values; on an equally short path, add route counts modulo `1,000,000,007`.

---

## Problem 6: Maximum Profit from Scheduled Jobs

**Difficulty:** Difficult · **Time limit:** 3 seconds · **Memory limit:** 256 MB

### Task

Each job has a start time `S`, finish time `F`, and profit `P`. Only one job can run at a time. A job occupies `[S, F)`, so another job may start exactly when it finishes.

Choose non-overlapping jobs to maximize total profit. Among schedules with the same maximum profit, choose one with the fewest jobs. Selecting no jobs is allowed and yields profit 0 with 0 jobs.

### Input

1. An integer `N`: the number of jobs.
2. `N` lines, each containing `S F P`.

### Output

Print exactly:

```text
MAXIMUM PROFIT: P
MINIMUM JOBS: K
```

### Constraints

- `1 ≤ N ≤ 200000`
- `0 ≤ S < F ≤ 10^9`
- `−10^9 ≤ P ≤ 10^9`

### Example

**Input**

```text
5
1 3 50
3 5 20
2 6 100
5 7 40
6 9 70
```

**Output**

```text
MAXIMUM PROFIT: 170
MINIMUM JOBS: 2
```

Choose the job `[2, 6)` with profit 100 and the job `[6, 9)` with profit 70. Their intervals do not overlap.

### Suggested approach

Sort jobs by finish time. For each job, use binary search to find the latest compatible earlier job. Dynamic programming can track the best `(total profit, job count)` for each prefix. Compare candidates by higher profit first, then fewer jobs.

---

## Organizer notes

| Problem | Useful hidden cases |
|---|---|
| 1 | Zero initial balance; all withdrawals rejected; all transactions successful |
| 2 | One student; tied top averages; scores of 0 and 100 |
| 3 | Unknown code; insufficient stock; empty restock report; multiple products needing stock |
| 4 | Zero rotation; rotation by a multiple of `N`; large `K`; repeated position queries |
| 5 | Unreachable destination; multiple shortest routes; closed critical road |
| 6 | Overlapping jobs; tied profits; negative or zero profits; jobs sharing endpoints |

The original draft had conflicting examples. This version corrects the overview and the sample outputs for Problems 3–6. Reference solutions and additional tests should be run before using the set for judging.
