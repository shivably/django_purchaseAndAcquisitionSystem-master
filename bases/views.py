from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from inventario.models import Product, Category, Subcategory, Brand
from compras.models import AcquisitionHeader 
from facturacion.models import BillingHeader, Customer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class MixinFormInvalid:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class NoPermission(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = "redirect_to"
    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:noPermission'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['total_product'] = Product.objects.count()
        context['total_customer'] = Customer.objects.count()
        context['total_purchase_invoice'] = AcquisitionHeader.objects.count()
        context['total_sales_invoice'] = BillingHeader.objects.count()
        return context

class HomeNoPermission(generic.TemplateView):
    template_name = "bases/nopermission.html"