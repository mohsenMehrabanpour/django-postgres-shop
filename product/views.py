from django.core import paginator
from django.http.response import HttpResponse
from product.models import Image, Product
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator


class Show_products(View):
    def get(self, request):
        products = Product.objects.all()
        print('products : ', products)
        paginator = Paginator(products,1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for product in page_obj:
            img = Image.objects.filter(product_id = product.id).first()
            if img is not None:
                setattr(product,'Image',str(img.image.url))
            else:
                setattr(product,'Image', '')
            print('page_obj : ', product.Image)

        return render(request, 'home.html', {'page_obj':page_obj})

class Product_single(View):
    def get(self, request, id):
        # id = request.GET.get('id',100)
        return HttpResponse('your id is : {}'.format(id))