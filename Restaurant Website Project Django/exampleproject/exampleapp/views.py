import pandas as pd
from .models import MenuItem  # Import your MenuItem model
from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem

class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                            cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(cart)

        return redirect('index')




    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products=None
             
        # excel_file_path = 'C:\\Users\\Ravindra\\Desktop\\demo.xlsx'

        # try:
        #     excel_data = pd.read_excel(excel_file_path)
            
        #     # Print column names to console for debugging
        #     print(excel_data.columns)
            
        #     # Iterate over rows in the DataFrame and create MenuItem objects
        #     for _, row in excel_data.iterrows():
        #         menu_item = MenuItem(
        #             name1=row['name1'],  # Adjust column name here
        #             name2=row['name2'],  # Adjust column name here
        #             price=row['price']   # Adjust column name here
        #         )
        #         menu_item.save()  # Save the MenuItem object to the database
            
        #     # Retrieve all MenuItem objects from the database
        menu_items = MenuItem.objects.all()
            
        return render(request, 'index.html', {'menu_items': menu_items})
        
        # except FileNotFoundError:
        #     return render(request, 'index.html', {'error_message': 'Excel file not found!'})
        # except Exception as e:
        #     return render(request, 'index.html', {'error_message': 'An error occurred: ' + str(e)})

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = MenuItem.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products' : products} )
            

def search(request):
    query = request.GET['query']
    # products =MenuItem.objects.all()
    menu_items = MenuItem.objects.filter(name2__icontains=query)
    return render(request, 'index.html', {'menu_items': menu_items})

