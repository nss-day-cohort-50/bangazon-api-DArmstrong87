"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all


class ExpensiveProducts(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                             SELECT *
                             FROM bangazon_api_product
                            WHERE price >= 1000;
                              """)

            dataset = dict_fetch_all(db_cursor)
            expensive_products = []
            for row in dataset:
                expensive_products.append({
                    "name": row['name'],
                    "price": row['price']
                })
            
        template='users/expensiveproducts.html'
        
        context={
            "expensive_products": expensive_products
        }
        
        return render(request, template, context)