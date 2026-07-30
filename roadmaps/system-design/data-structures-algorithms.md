---
name: Data Structures and Algorithms
category: system-design
status: researched
last-updated: 2026-07-30
sources:
  - https://en.wikipedia.org/wiki/Data_structure
  - https://en.wikipedia.org/wiki/Algorithm
  - https://en.wikipedia.org/wiki/Analysis_of_algorithms
  - https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
  - https://en.wikipedia.org/wiki/Introduction_to_Algorithms
  - https://leetcode.com/
  - https://neetcode.io/
  - https://github.com/jwasham/coding-interview-university
  - https://www.bigocheatsheet.com/
  - https://github.com/trekhleb/javascript-algorithms
  - https://github.com/TheAlgorithms/python
  - https://github.com/TheAlgorithms/C-Plus-Plus
  - https://github.com/TheAlgorithms/Go
  - https://github.com/TheAlgorithms/Rust
  - https://www.coursera.org/specializations/algorithms
  - https://hellointerview.com/
tags: [dsa, data-structures, algorithms, leetcode, complexity, big-o, interview]
---

# Data Structures and Algorithms

## One-liner

The catalog of structures (arrays, trees, graphs, hashes) and algorithms (sorting, searching, graph algorithms, DP) that every senior engineer is expected to know — and that every tech interview still tests.

## What It Is

DSA is the alphabet of computer science. It's not about memorizing implementations; it's about **choosing the right structure** for your access patterns and **predicting the cost** of your algorithm. Every non-trivial engineering decision touches DSA.

### Data structures

| Structure | Best for | Time complexities |
|-----------|----------|-------------------|
| **Array** | Indexed access; fixed-size; cache-friendly. | O(1) access; O(n) search; O(n) insert/delete. |
| **Linked List** | Frequent inserts/deletes; no random access. | O(n) access; O(1) insert/delete at head. |
| **Stack** | LIFO; recursion simulation; undo. | O(1) push/pop. |
| **Queue** | FIFO; BFS; producer-consumer. | O(1) enqueue/dequeue. |
| **Hash Table** | O(1) lookup; caches; sets. | O(1) avg; O(n) worst. |
| **Binary Tree** | Hierarchical data. | O(n) traversal. |
| **BST (Binary Search Tree)** | Sorted data with fast lookup. | O(log n) avg; O(n) worst (unbalanced). |
| **AVL / Red-Black Tree** | Self-balancing BST. | O(log n) guaranteed. |
| **B-Tree** | Disk-based; databases; filesystems. | O(log n) with low constant. |
| **Heap** | Priority queue; top-k. | O(log n) insert; O(1) peek. |
| **Trie** | Prefix search; autocomplete. | O(m) where m = key length. |
| **Graph** | Networks; dependencies; relationships. | O(V+E) traversal. |
| **Union-Find (DSU)** | Connected components; Kruskal's MST. | Near O(1) amortized. |
| **Segment Tree / Fenwick** | Range queries + updates. | O(log n) per op. |
| **Skip List** | Probabilistic sorted set; used in Redis. | O(log n) avg. |
| **Bloom Filter** | Probabilistic membership; caches. | O(1) check; false-positive possible. |
| **LRU Cache** | Cache eviction policy. | O(1) with hash + doubly-linked list. |

### Algorithm categories

| Category | Algorithms |
|----------|-----------|
| **Sorting** | Quicksort, Mergesort, Heapsort, Counting sort, Radix sort, Topological sort (DAG). |
| **Searching** | Binary search, Interpolation search, Ternary search. |
| **Graph** | BFS, DFS, Dijkstra, Bellman-Ford, A*, Floyd-Warshall, Prim, Kruskal, Tarjan (SCC), Kosaraju. |
| **Trees** | Inorder/preorder/postorder, Morris traversal, lowest common ancestor, AVL rotations. |
| **Greedy** | Interval scheduling, Huffman coding, Activity selection. |
| **Dynamic Programming** | Knapsack, LCS, Edit distance, Coin change, Matrix chain multiplication. |
| **Divide & Conquer** | Merge sort, Quick sort, Closest pair of points, Strassen. |
| **Backtracking** | N-Queens, Sudoku, Permutations, Subset sum. |
| **String** | KMP, Rabin-Karp, Z-algorithm, suffix arrays. |
| **Bit Manipulation** | XOR tricks, bitmask DP, Brian Kernighan's algorithm. |

### Complexity analysis (Big-O)

| O | Name | Example |
|---|------|---------|
| O(1) | Constant | Hash lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array scan |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(n³) | Cubic | Naive matrix mult |
| O(2ⁿ) | Exponential | Brute-force subsets |
| O(n!) | Factorial | Brute-force permutations |

Amortized, space, average vs worst case — all matter.

## When To Use It

- **You're interviewing for software engineering roles** — every company tests this.
- **You're choosing a data structure for a non-trivial problem** — right choice = 1000× speedup.
- **You're debugging performance** — algorithmic complexity is the first thing to check.
- **You're writing libraries / frameworks** — your users will hit edge cases.
- **You want to think like a computer scientist** — abstraction + rigor.

## When NOT To Use It

- **You're shipping a CRUD app** — stdlib / ORM has the structures.
- **You can use a well-tested library** — don't roll your own hash table.
- **The performance is fine** — premature optimization.
- **The problem is simple** — over-engineering with fancy structures wastes time.
- **Your language hides the details** — JS Map / Python dict / Go map handle the common cases.

## Why It Matters in 2026

Three forces:

1. **AI writes the code; humans design the algorithm.** Cursor / Claude Code can implement any algorithm from a description. The value is in choosing *which* algorithm and *why*. Knowing DSA = knowing what's possible.
2. **Performance still matters.** Hot paths in production systems often need optimal data structures. LRU caches, hash tables, B-trees — these aren't academic.
3. **Interview culture.** Tech interviews gate careers; DSA is the universal language. Top companies still test it.

Practitioner playbook in 2026:
1. **Master the basics first** — arrays, linked lists, stacks, queues, hash tables, trees, graphs.
2. **Practice on LeetCode / NeetCode / Hello Interview** — pattern recognition matters.
3. **Read CLRS** if you want depth (the algorithms bible).
4. **Apply in your day job** — when you hit a perf issue, ask "is this the right data structure?"
5. **Know your language's stdlib** — most algorithms are built in.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 100 | The canon of CS; taught in every university since the 1960s. |
| Community | 100 | Massive; LeetCode, NeetCode, every interview prep resource. |
| Learning curve | 30 | Steep; years of practice to internalize. |
| Performance | N/A | Knowledge. |
| Cost | 95 | LeetCode free / cheap; CLRS $80; OSSU free. |
| DX | 80 | Algorithms libraries + LeetCode make practice easy. |
| Production readiness | 100 | Every production system uses these. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Skip DSA; learn frameworks** | Short-term job placement. | Long-term engineering depth. |
| **LeetCode-only** | Interview prep. | Real-world system design. |
| **Math-only** | Theory research. | Practical engineering. |
| **Domain-specific (e.g. ML algorithms)** | Specialized roles. | General SWE. |

## Sources

- [Wikipedia — Data Structure](https://en.wikipedia.org/wiki/Data_structure) — 2026
- [Wikipedia — Algorithm](https://en.wikipedia.org/wiki/Algorithm) — 2026
- [Wikipedia — Analysis of Algorithms](https://en.wikipedia.org/wiki/Analysis_of_algorithms) — 2026
- [CLRS (Introduction to Algorithms, MIT Press)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) — 2022 (4th ed)
- [Wikipedia — Introduction to Algorithms](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) — 2026
- [LeetCode](https://leetcode.com/) — 2026
- [NeetCode](https://neetcode.io/) — 2026
- [Coding Interview University (jwasham)](https://github.com/jwasham/coding-interview-university) — 2026
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) — 2026
- [JavaScript Algorithms (trekhleb)](https://github.com/trekhleb/javascript-algorithms) — 2026
- [The Algorithms — Python](https://github.com/TheAlgorithms/python) — 2026
- [The Algorithms — C++](https://github.com/TheAlgorithms/C-Plus-Plus) — 2026
- [The Algorithms — Go](https://github.com/TheAlgorithms/Go) — 2026
- [The Algorithms — Rust](https://github.com/TheAlgorithms/Rust) — 2026
- [Coursera — Algorithms Specialization](https://www.coursera.org/specializations/algorithms) — 2026
- [Hello Interview](https://hellointerview.com/) — 2026