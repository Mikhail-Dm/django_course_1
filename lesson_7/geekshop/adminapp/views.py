from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u:u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserRegisterForm()
    context = {
        'form': user_form
    }
    return render(request, 'adminapp/user_form.html', context)


@user_passes_test(lambda u:u.is_superuser)
def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda u:u.is_superuser)
def user_update(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:user_list'))
    else:
        user_form = ShopUserAdminEditForm(instance=current_user)
    context = {
        'form': user_form
    }
    return render(request, 'adminapp/user_form.html', context)


@user_passes_test(lambda u:u.is_superuser)
def user_delete(request, pk):
    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if current_user.is_active:
            current_user.is_active = False
        else:
            current_user.is_active = True
        current_user.save()
        return HttpResponseRedirect(reverse('adminapp:user_list'))

    context = {
        'object': current_user
    }
    return render(request, 'user_delete.html', context)


@user_passes_test(lambda u:u.is_superuser)
def category_create(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def categories(request):
    categories_list = ProductCategory.objects.all()
    content = {
        'object_list': categories_list
    }
    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u:u.is_superuser)
def category_update(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def category_delete(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def product_create(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'category': category,
        'objects': products_list,
    }
    return render(request, 'adminapp/products.html', content)


@user_passes_test(lambda u:u.is_superuser)
def product_update(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def product_delete(request):
    context = {

    }
    return render(request, '', context)


@user_passes_test(lambda u:u.is_superuser)
def product_detail(request):
    context = {

    }
    return render(request, '', context)