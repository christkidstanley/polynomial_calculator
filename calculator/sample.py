import polynomial_addition

a = input("Enter a equation:")
b = input("Enter a equation:")
a_equation = polynomial_addition.get_polynomial(a)
b_equation = polynomial_addition.get_polynomial(b)
result = polynomial_addition.add_equation(a_equation, b_equation)
polynomial_addition.print_po()