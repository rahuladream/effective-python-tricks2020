"""
==1==
so assert statement make sure that the price of product doesn't fall to 0 and doesn't go up from the original price
"""

def apply_discount(product, discount):
	price = int(product['price'] * (1.0 - discount))
	assert 0 <= price <= product['price']
	return price


"""
==2==
in this case expression1 is the condition we test and the optional condition is expression2 is an error_message replicate this code will give"""
assert_stmt ::= "assert" expression1 [",", expression2]

"replicate previous code"
if __debug__:
	if not expression1:
		raise AssertionError(expression2)



"""
==3==
for providing th delete product permission as per a user's request
Never ever use assertion to do data validation
Instead use regular expression
"""

def delete_product(product_id, user):
	if not user.is_admin():
		raise AuthError('Must be admin to delete')
	if not store.has_product(product_id):
		raise ValueError('Unknown product id')
	store.get_product(product_id).delete()


"""
acquiring or writing the file using and try or fwrit() descriptor, and if exception captured during the f.write() call and therefore our program might leak a file descriptor.
WE USE INSTEAD THIS 
"""

# Better:
with some_lock:
	# Do something...



"""What’s a context manager? -- It’s a simple “protocol” (or interface) that your object needs to follow in order to support the with statement.

Basically, all you need to do is add __enter__ and __exit__ methods
to an object if you want it to function as a context manager.
"""
