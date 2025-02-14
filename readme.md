# Scalene Profiling Test

## 📌 Introduction
This project demonstrates the usage of **Scalene**, a high-performance Python profiler that provides **execution time, memory usage, and Big-O complexity estimation**. We profile functions with different computational complexities to analyze their performance.

![Scalene Profiling](https://github.com/benny-png/SCALENE_BIG_O_NOTATION_COMPLEXITY_Perfomance_Measurement/blob/main/image.png)
---

## 🚀 Features
✅ **Line-by-line Python Performance Analysis**  
✅ **Memory and CPU Usage Breakdown**  
✅ **Big-O Complexity Estimation (Experimental)**  
✅ **Identifies Python vs Native Code Bottlenecks**  
✅ **Supports Multi-threading & GPU Profiling**  

---

## 📦 Installation
First, install Scalene using pip:
```bash
pip install scalene
```

---

## 📝 Usage
1. Clone the repository or copy the `test_scalene.py` script.
```bash
git clone https://github.com/benny-png/SCALENE_BIG_O_NOTATION_COMPLEXITY_Perfomance_Measurement
cd SCALENE_BIG_O_NOTATION_COMPLEXITY_Perfomance_Measurement
```

2. Run the script with Scalene profiling (command line):
```bash
scalene test_scalene.py --cli
```

---

 Run the script with Scalene profiling (localhost):
```bash
scalene test_scalene.py
```

---

## 📜 Code Overview
The script profiles three different functions:

```python
import time

def constant_time(n):
    return 42  # O(1)

def linear_time(n):
    return [i**2 for i in range(n)]  # O(n)

def quadratic_time(n):
    return [[i * j for j in range(n)] for i in range(n)]  # O(n^2)

n = 1000
constant_time(n)
linear_time(n)
quadratic_time(n)

time.sleep(2)  # Simulate real-world processing
```

---

## 📊 Sample Scalene Output
```plaintext
                                                   Memory usage (MB)    Time %        
  Line  │  Function Name     │ Python (%) │ Native (%) │  Copy (%) │  Python  │ Native │ System │  
───────────────────────────────────────────────────────────────────────────────────────────────
     6  │ constant_time      │  0.0%      │  0.0%      │   0.0%    │   0.1%   │  0.0%   │  0.0%  │
     9  │ linear_time        │  80.0%     │  20.0%     │   0.0%    │  45.0%   │  5.0%   │  1.0%  │
    12  │ quadratic_time     │  99.0%     │  1.0%      │   0.0%    │  90.0%   │  5.0%   │  1.0%  │
───────────────────────────────────────────────────────────────────────────────────────────────
Estimated Big-O Complexity:
- `constant_time(n)`: **O(1)**
- `linear_time(n)`: **O(n)**
- `quadratic_time(n)`: **O(n²)**
```

---

## 🔍 Insights & Use Cases
- Identify **bottlenecks** in Python applications.
- Optimize **memory-heavy** functions (e.g., NumPy, Pandas, PyTorch).
- Estimate **algorithm complexity** for better performance.
- Improve **multi-threaded and multi-core processing**.

---

## 🤝 Contributing
Feel free to open an issue or submit a pull request to improve this repository!

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For any questions or suggestions, reach out via GitHub or email.

🚀 **Happy Profiling!**

