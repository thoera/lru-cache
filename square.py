from functools import lru_cache


@lru_cache(maxsize=3)
def square(number: float) -> float:
    print(f"Computing the square for {number=}")
    return number**2
