from django.shortcuts import render
from .models import Employee, Product, Sale, Customer

# Create your views here.
def home(request):
    qset2 = Product.objects.all().select_related('supervising_employee')
    return render(request, "home.html", {'result':list(qset2)})
