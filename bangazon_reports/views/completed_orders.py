"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View
from bangazon_reports.views.helpers import dict_fetch_all


class CompletedOrders(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
                            SELECT
                            o.id,
                            printf("%.2f", sum(p.price)) Total,
                            u.first_name || " " || u.last_name Customer,
                            pt.merchant_name PaymentType
                            FROM bangazon_api_order o
                            JOIN auth_user u
                            on o.user_id = u.id
                            JOIN bangazon_api_paymenttype pt
                            on o.payment_type_id = pt.id
                            JOIN bangazon_api_orderproduct op
                            on op.order_id = o.id
                            JOIN bangazon_api_product p
                            on p.id = op.product_id
                            WHERE o.completed_on is not Null
                            GROUP BY o.id;
                             """)

            dataset = dict_fetch_all(db_cursor)
            completed_orders = []
            for row in dataset:
                completed_orders.append({
                    "id": row['id'],
                    "customer": row["Customer"],
                    "total": row['Total'],
                    "payment_type": row['PaymentType']
                })

        template = 'users/completedorders.html'

        context = {
            "completed_orders": completed_orders
        }

        return render(request, template, context)
