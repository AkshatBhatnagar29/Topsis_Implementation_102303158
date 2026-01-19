# Topsis_Implementation_102303158


#  TOPSIS-AkshatBhatnagar-102303158

[![PyPI version](https://img.shields.io/pypi/v/topsis-akshatbhatnagar-102303158.svg)](https://pypi.org/project/topsis-akshatbhatnagar-102303158/1.0.2/)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python package to implement **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution). This method is used for multi-criteria decision-making (MCDM).

**PyPI Project Link:** [https://pypi.org/project/topsis-akshatbhatnagar-102303158/1.0.2/](https://pypi.org/project/topsis-akshatbhatnagar-102303158/1.0.2/)

---

##Installation

You can install the package directly from PyPI using pip:

```bash
pip install topsis-akshatbhatnagar-102303158
```


---

## 📊 Methodology

TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).

**The algorithm follows these steps:**

1. **Normalization:**
The decision matrix is normalized to scale all criteria to a uniform dimension.
$$ r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}} $$
2. **Weight Assignment:**
The normalized matrix is multiplied by the weights assigned to each criterion.
$$ v_{ij} = w_j \times r_{ij} $$
3. **Ideal Solution Determination:**
* **Ideal Best ():** Max value for beneficial attributes (+), Min value for non-beneficial attributes (-).
* **Ideal Worst ():** Min value for beneficial attributes (+), Max value for non-beneficial attributes (-).


4. **Distance Calculation:**
Euclidean distance is calculated for each alternative from the Ideal Best () and Ideal Worst ().
5. **Score Calculation:**
The similarity score is calculated as:
$$ P_i = \frac{S_i^-}{S_i^+ + S_i^-} $$
6. **Ranking:**
Alternatives are ranked based on the score (Highest Score = Rank 1).

---

## 🚀 Usage

This package provides a command-line interface (CLI) to perform TOPSIS analysis on a CSV dataset.

### Command Syntax

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>

```

### Parameters

| Parameter | Description | Example |
| --- | --- | --- |
| **InputDataFile** | Path to the input CSV file. The file should contain 3 or more columns. The first column is the object/model name, and the rest must be numeric. | `data.csv` |
| **Weights** | Comma-separated numbers representing the weight of each criterion. | `"1,1,1,2"` |
| **Impacts** | Comma-separated signs (`+` or `-`) indicating if a variable is beneficial (`+`) or non-beneficial (`-`). | `"+,+,-,+"` |
| **ResultFileName** | The name of the output CSV file where results will be saved. | `result.csv` |

---

## 📝 Example

### 1. Prepare your Data (`data.csv`)

Create a CSV file with your data. The first column should be the name/ID of the alternative, and subsequent columns should be numeric criteria.

| Model | Storage | Camera | Price | Looks |
| --- | --- | --- | --- | --- |
| M1 | 16 | 12 | 250 | 5 |
| M2 | 32 | 16 | 300 | 4 |
| M3 | 16 | 8 | 200 | 3 |
| M4 | 32 | 20 | 400 | 5 |
| M5 | 16 | 16 | 280 | 3 |

### 2. Run the Command

Run the following command in your terminal:

```bash
topsis data.csv "1,1,1,1" "+,+,-,+" result.csv

```

### 3. Result Table (`result.csv`)

The program will generate a new file `result.csv` with two additional columns: **Topsis Score** and **Rank**.

| Model | Storage | Camera | Price | Looks | **Topsis Score** | **Rank** |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | 16 | 12 | 250 | 5 | 0.534277 | 3 |
| M2 | 32 | 16 | 300 | 4 | 0.712391 | 1 |
| M3 | 16 | 8 | 200 | 3 | 0.341255 | 4 |
| M4 | 32 | 20 | 400 | 5 | 0.623101 | 2 |
| M5 | 16 | 16 | 280 | 3 | 0.482156 | 5 |

### 4. Result Graph

Below is a graphical representation of the TOPSIS scores for the given example.
<img width="1094" height="719" alt="image" src="https://github.com/user-attachments/assets/e25f3530-6e6c-4a03-910c-431d96d891f1" />


---

##  Constraints & Validation

* The input file must contain **three or more columns**.
* From the **2nd to the last column**, all values must be **numeric**.
* The number of **weights**, **impacts**, and **numeric columns** must be equal.
* Impacts must be either `+` or `-`.
* Proper error handling is implemented for "File Not Found" and input format mismatches.

---



```

```
