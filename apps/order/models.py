from django.db import models
from globals.models import BaseModel
from user.models import User


class Order(BaseModel):
    orderid = models.UUIDField(verbose_name='订单id', auto_created=True)
    user = models.ForeignKey(verbose_name='消费者', to=User, on_delete=models.CASCADE)
    cost = models.DecimalField(verbose_name='花费', decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
