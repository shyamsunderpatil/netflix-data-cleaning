# Netflix Titles – Data Cleaning Project

This repository contains the solution for **Task 1: Data Cleaning and Preprocessing** assigned during the Elevate Internship. The dataset used is the **Netflix Movies and TV Shows dataset**, which contains information about TV shows and movies available on Netflix as of 2021.

---

## 📊 Dataset Overview

- **Source**: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Rows**: ~8,800
- **Columns**: 12 (e.g., title, director, cast, date_added, duration, country)

---

## 🧹 Cleaning Objectives

The goal was to clean the raw dataset by handling:
- Missing values
- Duplicates
- Inconsistent column formats
- Mixed data types
- Irregular text entries

---

## 🔧 Tools Used

- Python 3
- Pandas
- Jupyter Notebook / VS Code

---

## 🛠️ Cleaning Steps Performed

1. **Standardized column names**  
   → Lowercased, replaced spaces with underscores for consistency.

2. **Handled missing values**  
   → Replaced nulls in:
   - `director`, `cast`, `country` → `"Not Specified"`
   - `rating` → Most frequent value (mode)
   - `date_added` → Forward filled

3. **Date formatting**  
   → `date_added` was stripped of spaces and converted to `datetime` using format `"%B %d, %Y"`.

4. **Duplicate removal**  
   → Removed any duplicate rows.

5. **Duration column split**  
   → Extracted:
   - `duration_num` → Numeric part (e.g., 90)
   - `duration_unit` → Unit (e.g., "Minutes" or "Seasons")

6. **Standardized categorical text**  
   → Applied `.str.strip().str.title()` to columns like `type`, `rating`, `country`.

---

## 📁 Files in This Repo

| File                            | Description                                      |
|---------------------------------|--------------------------------------------------|
| `netflix_titles.csv`           | Original raw dataset                             |
| `netflix_cleaning.py`          | Python script used to clean the dataset          |
| `netflix_titles_cleaned.csv`   | Final cleaned dataset ready for analysis         |
| `README.md`                    | Summary of the project and steps followed        |

---

## 🧠 What I Learned

- How to identify and handle missing data using `fillna()` and `isnull()`
- Standardizing data types and text entries
- Using Pandas for efficient preprocessing
- Importance of clean, consistent data before analysis or modeling

---

## ✅ Task Completion

This project is submitted as part of **Elevate Internship Task 1 – Data Analyst Track**  
Submission Link: [https://forms.gle/o2uMAByM719GzebC7](https://forms.gle/o2uMAByM719GzebC7)

---
