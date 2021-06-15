from django.utils.translation import ugettext_lazy as _
from django.db import models


# Create your models here.
class Demo(models.Model):
    id = models.AutoField(_("ID Demo"), name="id", primary_key=True, db_column="id")
    name = models.CharField(_("Nombre"), max_length=50, db_column="name", null=False)
    surnames = models.CharField(_("Apellidos"), max_length=50, db_column="surnames", null=False)
    email = models.EmailField(_("Correo electrónico"), max_length=254, db_column="email", null=False)
    phone = models.CharField(_("Teléfono"), max_length=50, db_column="phone", null=False)
    day = models.DateTimeField(_("Día"), auto_now=False, auto_now_add=False, null=False, db_column="day")
    hour = models.DateTimeField(_("Hora"), auto_now=False, auto_now_add=False, null=False, db_column="hour")
    restaurant_name = models.CharField(_("Nombre del restaurante"), max_length=100, null=False, db_column="restaurant_name")

    class Meta:
        db_table = 'demos'

    def __init__(self, *args):
        super(Demo, self).__init__(*args)
