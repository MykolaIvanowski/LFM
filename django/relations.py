# models, views, urls, tamplates
from traceback import format_stack

from pyspark.task_i import username


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


        #*******

# Forms
# form automaticly validates fileds like email and ensures structured data

form django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=180)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


# Admin
# Admin panel allows developers to manage database models through a user frendly interface without sql queries

from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)  # register the model with admin site


# Middleware
#  middleware function process requests and responses globally across Django
# authentication checks, logining, modifying response


from django.utils.deprecation import MiddlawareMixin

class MyMiddleware(MiddlawareMixin):
    def process_request(self, requests):
        f'Middleware processing request'

    def process_response(self, request, reponce):
        f'Middleware processing response'
        return reponce


# Signals
# signals allow  decoupled applications to communicate with each ather
# They trier events then database action occur (pre_save, post_save ,etc)

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=UserProfile):
def create_profile(sender, instance, created, **kwargs):
    if create:
        f'new profile created for {instance.user}'


# AuthenticationSystem
# Django has a build-in-authentication system with user management, password handling, and login/logout views

from django.contrib.auth import authenticate, login

user = authenticate(username='mykola', password='secret')
if user is not None:
    login(request, user)