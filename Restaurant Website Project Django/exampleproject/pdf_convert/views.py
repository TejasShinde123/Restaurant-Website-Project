from django.shortcuts import render
from exampleapp.models import MenuItem

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa


from django.template import RequestContext
# Create your views here.

def show_products(request):
    products = MenuItem.objects.all()

    context = {
        'products': products 
    }

    return render( request, 'pdf_convert/showinfo.html', context )


def pdf_report_create(request):
    ids = list(request.session.get('cart').keys())
    products = MenuItem.get_products_by_id(ids)

    template_path = 'pdf_convert/pdfreport.html'

    context ={'products': products,'request': request,}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposotion']='filename="products_report.pdf'

    template = get_template(template_path)

    html = template.render(context)

    pisa_status = pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse('error<pre>'+ html + '</pre>')
    return response
