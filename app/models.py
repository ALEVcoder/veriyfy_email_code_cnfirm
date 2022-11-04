from django.db import models
import random
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Users', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['region']

    class Meta:
        verbose_name = "Foydlanuvchi"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.username

class Code(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=6, null=True, blank=True)

    @property
    def genarate_code(self):
        number_list = list(range(10))
        code_items = ''
        for i in range(6):
            num = random.choice(number_list)
            code_items += str(num)
        self.number = code_items
        self.save()

    class Meta:
        verbose_name = "Email tasdiqlangan kodlar"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.number

