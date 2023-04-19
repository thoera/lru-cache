# What is @lru_cache?

See the [official documentation](https://docs.python.org/3/library/functools.html#functools.lru_cache) for a complete description of @lru_cache.

Here are a few bits:

@lru_cache can be described as a decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.

Distinct argument patterns may be considered to be distinct calls with separate cache entries. For example, f(a=1, b=2) and f(b=2, a=1) differ in their keyword argument order and may have two separate cache entries.

If maxsize is set to None, the LRU (for Least Recently Used) feature is disabled and the cache can grow without bound.

# Example

```shell
python -i square.py
```

```python
square(2)
square(2)
square.cache_info()

square(3)
square(4)

square(2)
square(3)
square(4)
square.cache_info()

square(5)
square.cache_info()

square(2)
square.cache_info()

square(4)
square.cache_info()

square.cache_clear()
square.cache_info()
square(4)

square.__wrapped__(4)
```
