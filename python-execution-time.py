# Measure Time in Python

This code shows how to measure the time of your code in Python.

## Code

```python
import time

def measure_time(func):
  """Decorator to measure the execution time of a function."""

  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Elapsed time: {end - start:.2f} seconds")
    return result

  return wrapper

@measure_time
def factorial(n):
  """Calculates the factorial of a number."""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  print(factorial(5))


## Usage

To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as `measure_time.py`, you can run it by typing the following command into the command line:


python measure_time.py
