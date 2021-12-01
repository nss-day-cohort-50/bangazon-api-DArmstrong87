from django.urls import path
from .views import ExpensiveProducts

urlpatterns = [
    path('reports/expensiveproducts', ExpensiveProducts.as_view()),
]
