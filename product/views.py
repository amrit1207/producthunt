from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    producthome=Product.objects
    return render(request,'product/home.html',{'producthome':producthome})



@login_required(login_url="/account/signup")
def create(request):
    if request.method=='POST':## start matching data and stored in dtatbases
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.FILES['image'] and request.POST['url']:
            product=Product()
            product.title=request.POST['title']
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']

            else:
                product.url ='http://' + request.POST['url']
            product.image=request.FILES['image']
            product.icon=request.FILES['icon']
            product.pub_date=timezone.datetime.now()##current date and time
            product.hunter=request.user ## who can access the create page..
            product.save()## to save the data in the databases...
            return redirect('/product/' + str(product.id))

        else:
            return render(request, 'product/create.html',{'error':'All Fields Are Mandatory'} )

    else:
        return render(request,'product/create.html',)

def detail(request,product_id):
    productdetail=get_object_or_404(Product,pk=product_id)
    return render(request,'product/details.html',{'productdetail': productdetail})


@login_required(login_url="/account/signup" ,)
def upvote(request,product_id):
    if request.method=='POST':
        product=get_object_or_404(Product,pk=product_id)
        product.votes +=1
        product.save()
        return redirect('/product/' + str(product.id))
