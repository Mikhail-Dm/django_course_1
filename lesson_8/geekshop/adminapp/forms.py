from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserRegisterForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
