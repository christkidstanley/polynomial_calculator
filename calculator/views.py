from django.shortcuts import render
from . import polynomial_addition


def get_equation(request):
    if request.method == 'POST':
        num1 = str(request.POST['num1'])
        num2 = str(request.POST['num2'])
        result = polynomial_addition.add_equation(num1, num2)
        return render(request, 'index.html', {'result': result, 'equation1': num1, 'equation2': num2})

    return render(request, 'index.html')
