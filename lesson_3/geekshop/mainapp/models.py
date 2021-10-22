from django.db import models



class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', max_length=256, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-id',)



class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=128, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='колличество на складе', default=0)

    def __str__(self):
        return self.name