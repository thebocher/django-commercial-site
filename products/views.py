from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product, Feedback, Category, CategoryTemplate, ProductCharacteristic

from .forms import FeedbackForm

from django.shortcuts import render


class ProductListView(ListView):
    queryset = Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.request.GET.get('category')
        context['category_filters'] = CategoryTemplate.objects.filter(category__name=category_name)
        ProductCharacteristic.objects.filter(product__category__name=category_name)
        context['categories'] = Category.get_dict()
        return context

class ProductDetailView(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = FeedbackForm()
        context['customers_feedbacks'] = Feedback.objects.all().order_by('-datetime')[:5]
        return context

def welcome(request):
    return render(request, 'products/index.html')