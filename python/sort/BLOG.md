# Quick Sort - 03/07/2022

```text
(8,4,23,42,16,15) pivot:15
(8,4) pivot:4 (15) (42,16,23)
(4,8,15) (42,16,23) pivot:23
(4,8,15) (16) (23,42) pivot:42
(4,8,15,16,23,42)
```

### Unit tests

Run command `pytest` to run the unit tests

# Merge Sort - 03/03/2022

```text
      [8,4,23,42,16,15]
    [8,4,23]       [42,16,15]
  [8]   [4,23]   [42]     [16,15]
 [8]   [4] [23] [42]     [16]  [15]
 [8]   [4,23]   [42]     [15,16]
   [4,8,23]        [15,16,42]
      [4,8,15,16,23,42]
```

### Unit tests

Run command `pytest` to run the unit tests

# Insertion Sort - 02/28/2022

## Insertion sort stepping through - `[8,4,23,42,16,15]`

### Step 0: Initial values: i = 1, l = [8,4,23,42,16,15], l.length = 6

### Step 1: i = 1, j = 0, temp = 4

- while j >= 0 and temp < l[j]
  - l[1] = 8, j = -1, l = [8,8,23,42,16,15]
- l[0] = 4, l = [4,8,23,42,16,15]

### Step 2: i = 2, j = 1, temp = 23 -> nothing happens

### Step 3: i = 3, j = 2, temp = 42 -> nothing happens

### Step 4: i = 4, j = 3, temp = 16

- while j >= 0 and temp < l[j]
  - l[4] = 42 , j = 2 -> l = [4,8,23,42,42,15]
  - l[3] = 23, j = 1 -> l = [4,8,23,23,42,15]
- l[2] = 16 -> l = [4,8,16,23,42,15]

### Step 5: i = 5, j = 4, temp = 15

- while j >= 0 and temp < l[j]
  - l[5] = 42, j = 3 -> l = [4,8,16,23,42,42]
  - l[4] = 23, j = 2 -> l = [4,8,16,23,23,42]
  - l[3] = 16, j = 1 -> l = [4,8,16,16,23,42]
- l[2] = 15 -> l = [4,8,15,16,23,42]

### Unit tests: Run command `pytest` to run the test
