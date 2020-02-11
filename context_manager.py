"""
you can use the contextlib.contextmanager decora-
tor to define a generator-based factory function for a resource that will
then automatically support the with statement.
"""


from contextlib import contextmanager
@contextmanager
def managed_file(name):
	try:
		f = open(name, 'w')
		yield f
	finally:
		f.close()

>>> with managed_file('hello.txt') as f:
... f.write('hello, world!')
... f.write('bye now')


"""
EXPLAINATION

In this case, managed_file() is a generator that first acquires the
resource. After that, it temporarily suspends its own execution and
yields the resource so it can be used by the caller. When the caller
leaves the with context, the generator continues to execute so that any
remaining clean-up steps can occur and the resource can get released
back to the system.