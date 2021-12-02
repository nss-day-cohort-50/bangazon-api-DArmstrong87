"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all


class InexpensiveProducts(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                             SELECT p.name Product,
                             p.price,
                             s.name Store
                             FROM bangazon_api_product p
                             JOIN bangazon_api_store s
                             on p.store_id = s.id
                             WHERE price <= 1000
                             ORDER By price desc
                             """)

            dataset = dict_fetch_all(db_cursor)
            inexpensive_products = []
            for row in dataset:
                inexpensive_products.append({
                    "name": row['Product'],
                    "price": row['price'],
                    "store": row["Store"]
                })

        template = 'users/inexpensiveproducts.html'

        context = {
            "inexpensive_products": inexpensive_products
        }

        return render(request, template, context)
