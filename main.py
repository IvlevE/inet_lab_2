from django.views.generic import TemplateView, DetailView

from cart.forms import CartAddProductForm
from product.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class CartView(TemplateView):
    template_name = 'cart.html'


class CategoryView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class CheckView(TemplateView):
    template_name = 'checkout.html'


class ConfirmationView(TemplateView):
    template_name = 'confirmation.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class SingleView(TemplateView):
    template_name = 'single-blog.html'


class ProdView(DetailView):
    template_name = 'single-product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = CartAddProductForm

        return context


class ProductSingle(DetailView):
    template_name = 'single-product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = ProdView.get_context_data(self, **kwargs)

        try:
            prod = self.request.GET['prod']
            if int(prod) == 1:
                context['products'] = Product.objects.all()
            else:
                context['products'] = Product.objects.filter(product_id=int(prod))
        except:
            context['products'] = Product.objects.all()

        context['products'] = Product.objects.all()
        return context


class OrderView(TemplateView):
    template_name = 'tracking-order.html'
