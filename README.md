
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

The code for each question is in the `questions` directory. These files can be run directly, or you can interact with all the question code from `home.py`.

## home.py

`home.py` is a script in which you can directly interact with all the code I have written for the questions I have answered. The code for a each question is located in its own module, which can be called using:

```python
import questions

questions.Qn.function_from_question()
```

where `n` is the question number.

## lib

In the `questions` directory there is a `lib` library, containing useful code which is often required for multiple questions. In `lib` there is also a `profiling` module, which contains the code I use to measure the performance of my solutions.
