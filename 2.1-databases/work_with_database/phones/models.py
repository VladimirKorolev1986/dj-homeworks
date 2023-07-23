from django.db import models
from django.utils.text import slugify


# В файле models.py нашего приложения создаём модель Phone
# с полями id, name, price, image, release_date, lte_exists и slug.
# Поле id — должно быть основным ключом модели.

class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    image = models.URLField(max_length=100, verbose_name='image')
    release_date = models.DateField(verbose_name='release_date')
    lte_exists = models.BooleanField(default=False, verbose_name='lte_exists')
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
