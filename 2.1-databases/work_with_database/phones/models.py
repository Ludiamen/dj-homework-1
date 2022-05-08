from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField()
    image = models.ImageField(max_length=100)
    release_date = models.CharField(max_length=100)
    lte_exists = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
