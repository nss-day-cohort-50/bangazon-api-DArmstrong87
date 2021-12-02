from django.urls import path

from bangazon_reports.views.completed_orders import CompletedOrders
from .views import ExpensiveProducts, InexpensiveProducts

urlpatterns = [
    path('reports/expensiveproducts', ExpensiveProducts.as_view()),
    path('reports/inexpensiveproducts', InexpensiveProducts.as_view()),
    path('reports/completedorders', CompletedOrders.as_view()),
]
