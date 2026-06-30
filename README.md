# Finding a Motif in DNA

## OVERVIEW
This program finds all starting positions where a substring **t** occurs in a DNA string **s**, including overlapping occurrences. It is a solution to the Rosalind problem **"Finding a Motif in DNA" (ID: SUBS)**.

---

## FEATURES
- Reads <u>s and t</u> from a text file (rosalind_subs.txt)
- Finds <u>every occurrence</u> of t in s, including overlapping matches
- Returns positions using <u>1-based indexing</u> (Rosalind convention)
- Clean, well-commented code with proper functions

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input txt named rosalind_subs.txt in the same folder as the code, otherwise you will receive a File Not Found Error!!!**</u>

---

## EXAMPLE
**Input** (rosalind_subs.txt):
```
GATATATGCATATACTT
ATAT
```
**Output:**
```
2 4 10
```
- <u>s</u> = `GATATATGCATATACTT` → the DNA string to search within
- <u>t</u> = `ATAT` → the substring to find

---

## HOW IT WORKS
1. Reads <u>s</u> (first line) and <u>t</u> (second line) from file
2. Slides a window of length `len(t)` across `s`, one position at a time
3. At each position `i`, compares the slice `s[i:i+len(t)]` to `t`
4. If they match, records `i + 1` (converted to 1-based indexing)
5. Prints all recorded positions

---

## TECHNOLOGIES USED
- **Python**
- **File I/O** (txt)
