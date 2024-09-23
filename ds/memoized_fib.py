def memo(fn):
	o = {}

	def cb(n):
		if n not in o:
			o[n] = fn(n)
		return o[n]
	
	return cb

def fib(n:int):
	if n == 1:
		return 1
	if n == 0:
		return 0
	return memo_fib(n - 1) + memo_fib(n-2)

memo_fib = memo(fib)
r = memo_fib(900)
print('r',r)


def memoized_fib(n: int, cache={0: 0, 1: 1}) -> int:
    if n not in cache:
        cache[n] = memoized_fib(n - 1, cache) + memoized_fib(n - 2, cache)  # Store in cache
    return cache[n]  # Return the cached value

