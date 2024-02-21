from django.shortcuts import render
from .models import Product , Brand , Review
from django.views import generic
from .forms import ReviewForm
from django.shortcuts import redirect
# Create your views here.



class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'

class ProductDetial(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'


def add_review(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('products:product_detail', slug=slug)
    else:
        form = ReviewForm()
    return render(request, 'products/add_review.html', {'form': form})

class BrandList(generic.ListView):
    model = Brand
    template_name='products/brand_list.html'

class BrandDetail(generic.ListView):
    model = Product
    template_name='products/brand_detail.html'  # One brand has many
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    


    # products so it should be ListView not DetailView

