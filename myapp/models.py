from django.db import models

# Create your models here.
from django.db import models


class OrderForm(models.Model):
    clientId = models.CharField(max_length=200)
    orderId = models.CharField(unique=True, max_length=200)
    state = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Don hang'

    def __str__(self):
        return self.clientId


class Items(models.Model):
    id = models.CharField(max_length=200, primary_key=True, verbose_name='Item ID')
    position = models.CharField(max_length=200)
    quantity = models.IntegerField()

    order_Form = models.ForeignKey(OrderForm, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Item'

    #
    def __str__(self):
        return self.id

    def client(self):
        # return "\n".join([p.client_Id for p in self.order_Form.all()])
        return self.order_Form.clientId

    def order(self):
        # return "\n".join([p.order_Id for p in self.order_Form.all()])
        return self.order_Form.orderId

    def state(self):
        return self.order_Form.state
    # class OrderFormItems(models.Model):
    #     order_Form = models.ForeignKey(OrderForm, on_delete=models.CASCADE)
    #     items = models.ManyToManyField(Items)

    # class Meta:
    #     verbose_name_plural = ' OrderForm_Items'
