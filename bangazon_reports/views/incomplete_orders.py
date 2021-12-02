"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all


class IncompleteOrders(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                            SELECT
                            o.id,
                            printf("%.2f", sum(p.price)) Total,
                            u.first_name || " " || u.last_name Customer,
                            o.created_on
                            FROM bangazon_api_order o
                            JOIN auth_user u
                            on o.user_id = u.id
                            JOIN bangazon_api_orderproduct op
                            on op.order_id = o.id
                            JOIN bangazon_api_product p
                            on p.id = op.product_id
                            WHERE o.completed_on ISNULL
                            GROUP BY o.id;
                             """)

            dataset = dict_fetch_all(db_cursor)
            incomplete_orders = []
            for row in dataset:
                incomplete_orders.append({
                    "id": row['id'],
                    "customer": row["Customer"],
                    "total": row['Total'],
                    "created_on": row['created_on']
                })

        template = 'users/incompleteorders.html'

        context = {
            "incomplete_orders": incomplete_orders
        }

        return render(request, template, context)
