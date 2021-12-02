from django.urls import path

from bangazon_reports.views.completed_orders import CompletedOrders
from bangazon_reports.views.favorites import Favorites
from bangazon_reports.views.incomplete_orders import IncompleteOrders
from .views import ExpensiveProducts, InexpensiveProducts, Favorites

urlpatterns = [
    path('reports/expensiveproducts', ExpensiveProducts.as_view()),
    path('reports/inexpensiveproducts', InexpensiveProducts.as_view()),
    path('reports/completedorders', CompletedOrders.as_view()),
    path('reports/incompleteorders', IncompleteOrders.as_view()),
    path('reports/favorites', Favorites.as_view()),
]
