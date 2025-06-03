# models views, Tamplates

#  models used for definding structure of data base
class Product(model.Model):
    name = models.CharField(max_lenth=20)
    prise = models.DecimalField(max_digits=10, decimal_prices=2)


# views logic layer
# it handle users requests, business logic, fetch data from models send it to Templates

def product_list(request):
    products = Product.object.all()
    return render(requests, 'products.html', {'products': products})


# Templates - this layer define how data is displayed on html

{% for product in productss %}
    <p>{{product.name}} - ${{ product.price}}</p>
{% endfor %}

# conclusion:
# models - manage data and store
# views - retrive the data and apply business logic
# templates - present data to the user
# could be changed for - API-driven frontend development