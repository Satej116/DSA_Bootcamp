# Longest Palindromic Substring Finder (Optimized)

## Description

This Python program finds and prints the **longest palindromic substring** in a given string using the **Expand Around Center** approach, which is significantly more efficient than brute-force methods.

---

## Logic

- For each character in the string:
  - Expand around a single character (odd-length palindrome).
  - Expand around a pair of characters (even-length palindrome).
- Track the longest valid palindrome found during these expansions.

---

## Features

- Converts input to lowercase for uniform comparison.
- Efficient time complexity: **O(n²)**.
- Clean implementation using helper function.