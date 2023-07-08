class Node:
    def __init__(self, value, exponent):
        self.value = value
        self.exponent = exponent
        self.next = None


class polynomial_addition:
    def __init__(self, head=None):
        self.head = head

    def append(self, terms):
        current = self.head
        if self.head is not None:
            while current.next:
                current = current.next
            current.next = terms
        else:
            self.head = terms

    def print(self):
        current = self.head
        lstr = ""
        while current.next.value != "/0":
            lstr = lstr + "|{}|{}|-->".format(current.value, current.exponent)
            current = current.next
        lstr = lstr + "|{}|{}|".format(current.value, current.exponent)
        print(lstr)

    def delete(self, node):
        current = self.head
        if current.value == node.value:
            self.head = node.next
        else:

            while current.next:
                if current.value == node.value:
                    break
                prev = current
                current = current.next

            if current is None:
                return
            prev.next = current.next

    def print_polynomial(self):
        current = self.head
        lstr = ""
        while current.next.value != "/0":
            lstr = lstr + "({}x^{})+".format(current.value, current.exponent)
            current = current.next
        lstr = lstr + "({}x^{})".format(current.value, current.exponent)
        return lstr


def print_po(equation=polynomial_addition()):
    a = equation.print_polynomial()
    return a


def add_equation(a, b):
    eq1 = get_polynomial(a)
    eq2 = get_polynomial(b)
    current_eq1 = eq1.head
    current_eq2 = eq2.head
    eq_3 = polynomial_addition()
    n1 = Node("/0", "/0")
    n2 = Node("/0", "/0")
    eq1.append(n1)
    eq2.append(n2)
    while current_eq1.value != "/0" and current_eq2.value != "/0":
        if current_eq1.exponent == current_eq2.exponent:
            value = current_eq1.value + current_eq2.value
            node = Node(value, current_eq1.exponent)
            eq_3.append(node)
            eq1.delete(current_eq1)
            eq2.delete(current_eq2)
            (current_eq1, current_eq2) = (current_eq1.next, current_eq2.next)
        elif current_eq1.exponent > current_eq2.exponent:
            value = current_eq1.value
            node = Node(value, current_eq1.exponent)
            eq_3.append(node)
            eq1.delete(current_eq1)
            current_eq1 = current_eq1.next
        elif current_eq1.exponent < current_eq2.exponent:
            value = current_eq2.value
            node = Node(value, current_eq2.exponent)
            eq_3.append(node)
            eq2.delete(current_eq2)
            current_eq2 = current_eq2.next
    while current_eq1.value != "/0":
        eq_3.append(current_eq1)
        current_eq1 = current_eq1.next

    while current_eq2.value != "/0":
        eq_3.append(current_eq2)
        current_eq2 = current_eq2.next
    eq_3.append(n1)
    final = print_po(eq_3)
    return final


def get_polynomial(equation):
    terms = ""
    equation = equation + "+"

    eq = polynomial_addition()
    power_node = []
    power = None
    coefficient_node = []
    coefficient = None
    for j in equation:
        if j == "x":
            coefficient = int(terms)
            coefficient_node.append(coefficient)
            terms = ""
        elif j == "+":
            power = int(terms)
            power_node.append(power)
            terms = ""
        elif j == "^":
            continue
        else:
            terms = terms + j

    equation = polynomial_addition()
    for (k) in range(len(coefficient_node)):
        value = coefficient_node[k]
        exponent = power_node[k]
        a1 = Node(value, exponent)
        equation.append(a1)
    last_node = Node("/0", "/0")
    equation.append(last_node)
    return equation


