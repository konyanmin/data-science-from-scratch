class Countingclicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count = 0) -> int:
        self.count = count

    def __repr__(self) -> str:
        return f"CountingClicker(count={self.count})"
    
    def click(self, num_times=1):
        """Click a clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0

clicker = Countingclicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two click, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

def add(a: int, b: int) -> int:
    return a + b

from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, 'type hints') == 'type hints, type hints'
