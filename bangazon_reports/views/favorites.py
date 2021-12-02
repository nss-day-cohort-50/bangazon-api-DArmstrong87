from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from bangazon_api.models import Favorite

class Favorites(View):
    def get(self, request):
        
        customers = User.objects.all().filter()
        custwithfavs = []
        for customer in customers:
            favorites = Favorite.objects.all()
            for fav in favorites:
                if customer.id == fav.customer_id and customer not in custwithfavs:
                    custwithfavs.append(customer)
                    
        for customer in custwithfavs:
            customer.favorite_stores = customer.favorites.all()
        
        template = 'users/favorites.html'
        context = {'customers': custwithfavs}
        return render(request, template, context)

