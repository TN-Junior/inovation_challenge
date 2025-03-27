# Innovation & IP Address Challenges

This project contains two independent Python scripts solving distinct algorithmic challenges:

1. **Innovation Level Calculation** – Calculate an innovation score based on historical organizational events.
2. **Possible IP Addresses** – Generate all valid IPv4 addresses from a string of digits.

---

## Challenge 1: Innovation Level

### Description

This script computes the **Innovation Level** of a company based on a list of organizational events. Each event can:

- Be an **Innovation Driver** → `+1`
- Be a **Barrier to Innovation** → `-1`
- Be neutral → `0` (not in either set)

### Rules

- Initial innovation level is `0`;
- Each event in the history affects the total according to its category;
- Repeated events are counted multiple times;
- Innovation drivers and barriers are **disjoint sets**.

### How to Run

```bash
python inovacao.py
```
The script will print the result of a sample input in the terminal.



### Example
```bash
history = [100, 200, 300, 100, 400]
boosters = {100, 500}
barriers = {200, 600}
# Output: 1 ( +1 -1 0 +1 0 )
````

## File Structure

```
.
├── inovacao.py           # Script with the main logic and sample execution
├── test_inovacao.py      # Automated tests using pytest
└── README.md             # This file
```

# Challenge 2: Possible IP Addresses

This script solves the challenge of generating valid IPv4 addresses from a string containing only digits.

---

## Description

Given a string of digits (without separators), this script attempts to insert three dots (`.`) to form all possible valid IPv4 addresses.

### Rules

- An IPv4 address consists of **4 parts** separated by dots (e.g., `192.168.0.1`);
- Each part must be a number between **0 and 255**;
- **Leading zeros are not allowed**, except for the number `"0"` itself;
- The input string must have a length between **4 and 12 characters**, inclusive.

---

## How to Run

Make sure you have **Python 3** installed. Then run:

```bash
python enderecos.py
```

The script will run a few sample inputs and print the resulting valid IP addresses to the console.

---

## Example

```python
ambiguous_ip = "25525511135"
# Output: ['255.255.11.135', '255.255.111.35']
```

---

## File Structure

```
.
├── enderecos.py         # Script with main logic and example tests
├── test_enderecos.py    # File with automated tests using pytest
└── README.md            # This file
```

---

## How It Works

1. It checks all combinations of 3 dots inserted into the input string to create 4 segments;
2. Each segment is validated using these rules:
   - Not empty;
   - No leading zero unless the segment is '0';
   - Must be ≤ 255;
3. Valid combinations are returned in sorted order.

---

## Requirements

- Python 3.7 or newer
- No external dependencies

---

## Optional: Running Unit Tests

You can also write and run automated tests using `pytest`.

### 1. Install pytest:

```bash
pip install pytest
```

### 2. Create a test file (e.g., `test_enderecos.py`) and run:

```bash
pytest
```

### Run the tests
Being at the root of the project:
```bash
pytest
````
Or run just the tests from one folder:
```bash
cd ChallengeOne
pytest
```

---

Results:

<img width="719" alt="image" src="https://github.com/user-attachments/assets/29d29088-21f6-467a-8aad-27bc26e69f0e" />




