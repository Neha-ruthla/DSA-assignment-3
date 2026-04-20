# Sorting Performance Analyzer (SPA)

##  Overview

This project implements and compares three fundamental sorting algorithms:

* Insertion Sort
* Merge Sort
* Quick Sort

The program analyzes their performance on different types of datasets and compares practical execution time with theoretical complexity.

---

##  Features

* Implementation of sorting algorithms from scratch (no built-in sort)
* Dataset generation:

  * Random data
  * Sorted data
  * Reverse sorted data
* Performance measurement using execution time
* Comparison of algorithm efficiency
* Correctness verification

---

##  Algorithms Used

### 1. Insertion Sort

* Time Complexity: O(n²)
* Best Case: O(n)
* Stable: Yes
* In-place: Yes

### 2. Merge Sort

* Time Complexity: O(n log n)
* Stable: Yes
* In-place: No

### 3. Quick Sort

* Average: O(n log n)
* Worst Case: O(n²)
* Stable: No
* In-place: Yes

---

##  Datasets

The program tests algorithms on:

* Random arrays (1000, 5000, 10000)
* Sorted arrays (1000, 5000, 10000)
* Reverse sorted arrays (1000, 5000, 10000)

---

##  How to Run

```bash
python spa_sorting.py
```

To save output in a file:

```bash
python spa_sorting.py > output.txt
```

---

##  Project Structure

```
SPA_Assignment/
│── spa_sorting.py
│── output.txt
│── report.pdf
│── README.md
```

---

##  Output

* Displays correctness check
* Shows execution time table for all datasets
* Results stored in `output.txt`

---

##  Conclusion

* Insertion Sort is efficient for small or nearly sorted data
* Merge Sort gives consistent performance
* Quick Sort is fast on average but depends on pivot selection

---

##  Note

* Built-in sorting functions are not used
* Same timing method is used for fair comparison

