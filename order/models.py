from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Usuário', related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Nome', max_length=100)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=100)
    email = models.CharField(verbose_name='Email', max_length=100)
    address = models.CharField(verbose_name='Endereço', max_length=100)
    zipcode = models.CharField(verbose_name='CEP', max_length=100)
    place = models.CharField(verbose_name='Cidade', max_length=100)
    phone = models.CharField(verbose_name='Telefone', max_length=100)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    paid_amount = models.DecimalField(verbose_name='Valor pago', 
        max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(verbose_name='Token', max_length=100)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.first_name
    


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, verbose_name='Pedido',  related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Produto', related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Preço', max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantidade', default=1)

    class Meta:
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '%s' % self.id
