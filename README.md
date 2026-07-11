# Python for Biology

[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kubomu/biology-python-course/main?labpath=Applied_Biology_Notebook.ipynb)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

Learn Python through biology. This course teaches programming by using it on real biological questions: reading DNA sequences, exploring health and ecology data, and making scientific plots. Everything runs in your browser, so there is nothing to install.

## Table of Contents

- [Start here (no install needed)](#start-here-no-install-needed)
- [What you will learn](#what-you-will-learn)
- [How to use it](#how-to-use-it)
- [Tips for beginners](#tips-for-beginners)
- [Run it on your own machine](#run-it-on-your-own-machine)
- [A note for Google Colab users](#a-note-for-google-colab-users)
- [For students at Gulu University](#for-students-at-gulu-university)

## Start here (no install needed)

Click the button below. Binder reads this course's `requirements.txt`, installs everything for you, and opens the notebook in your browser.

[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kubomu/biology-python-course/main?labpath=Applied_Biology_Notebook.ipynb)

The first launch takes a minute or two while Binder sets things up. When it opens, run each cell in order by pressing Shift and Enter.

Two ways to open the lesson:

| Notebook | Open (everything ready) | Open (fast) |
|----------|-------------------------|-------------|
| Applied Biology Notebook | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Kubomu/biology-python-course/main?labpath=Applied_Biology_Notebook.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Kubomu/biology-python-course/blob/main/Applied_Biology_Notebook.ipynb) |

## What you will learn

- Python basics, taught with biological examples
- Reading and analysing DNA sequences with biopython
- Working with health and ecology datasets using pandas
- Creating clear scientific visualisations with matplotlib and seaborn
- Simple statistical analysis for biology with scipy

No prior programming is assumed. Each idea is explained as it comes up.

## How to use it

**On a computer or laptop (recommended)**

1. Click the Binder button above.
2. Wait for it to load.
3. Run each cell in order and read the explanations as you go.

**On a phone**

It works, but it is much easier on a computer. Use a laptop if you can.

## Tips for beginners

- Run cells in order. Press Shift and Enter to run each code cell.
- Do not worry about errors. Reading an error message and fixing it is part of learning.
- Experiment. Change a number or a sequence and see what happens. You cannot break anything.
- Ask questions. If you are in a class, your instructor is there to help.

## Run it on your own machine

If you would rather not use the browser:

1. Clone the repository:
   ```bash
   git clone https://github.com/Kubomu/biology-python-course.git
   cd biology-python-course
   ```
2. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Start Jupyter and open the notebook:
   ```bash
   jupyter lab
   ```

You can also open the folder in GitHub Codespaces (Code button, then Codespaces) and the environment installs itself.

## A note for Google Colab users

Colab opens instantly and already has numpy, pandas, matplotlib, seaborn, scipy, and plotly. This course also uses biopython, which Colab does not include by default. When you open the notebook in Colab, add a new cell at the very top and run this once:

```python
!pip install biopython
```

Then run the rest of the notebook normally. Binder does not need this step because it installs everything from `requirements.txt` for you.

## For students at Gulu University

This course was created for Applied Biology students learning computational skills. Everyone starts as a beginner, so take your time and work through it at your own pace.
