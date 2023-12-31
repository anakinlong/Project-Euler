
# Project Euler

My python code to answer the questions on https://projecteuler.net

I am aiming mainly for extremely readable code. I try to make my solutions relatively well-optimised, although not to the effect of making the code unreadable or unable to be generalised or applied to other cases.

# System Requirements

1. Python version 3.11.0
2. pip

# Initial Setup

Create a virtual environment for this project by opening a terminal in the root directory of this repository and entering:

```shell
python -m venv venv
```

Then activate the environment and install the required packages from `requirements.txt`:

```shell
\venv\Scripts\activate

pip install -r requirements.txt
```

# Running the Code

The code for each question is its own file in the `questions` library. These files can be run directly, or you can interact with all the question code from `home.py`.

## home.py

`home.py` is a script in which you can directly interact with all the code I have written for the questions I have answered. The code for a each question is located in its own module `Q{n}` within the `questions` library, where `n` is the question number. For example, to access the functions used in question 1:

```python
import questions

questions.Q1.sum_of_multiples([3, 5], range(1, 1000))
```

The names of these modules are currently compiled at run-time, so won't show up on any inteli-sense IDE extensions like you may expect them to.

Alternatively, you can get the question text, answer, or any additional explanation from any answered question by using the `question`, `answer`, and `explanation` functions that are defined in this script. `all_answers` returns a dictionary mapping each question number to its answer.

## lib

In the `questions` directory there is a `lib` library, containing useful code which is often required for multiple questions. In `lib` there is also a `profiling` module, which contains the code I use to measure the performance of my solutions.
