# models, views, urls, tamplates

#  models used for definding structure of data base
class Product(model.Model):
    name = models.CharField(max_lenth=20)
    prise = models.DecimalField(max_digits=10, decimal_prices=2)


# views logic layer
# it handle users requests, business logic, fetch data from models send it to Templates

def product_list(request):
    products = Product.object.all()
    return render(requests, 'products.html', {'products': products})

# URLs in Django (Uniform Resource Locators)
# the are used for map we addrese to specific views
# Key roles  - routing requests, dynamic url patterns, decoupling logic (separetes url config from views logic)

from django.urls import path
from . import views

urlspatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]

# Templates - this layer define how data is displayed on html

{% for product in productss %}
    <p>{{product.name}} - ${{ product.price}}</p>
{% endfor %}

# conclusion:
# models - manage data and store
# views - retrive the data and apply business logic
# urls - dispatcher connects incomming requests to concrete function or views
# templates - present data to the user
# could be changed for - API-driven frontend development