from django.core.validators import MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from moniTouring.accounts.models import MoniTouringUser


class Monitor(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    brand = models.CharField(max_length=30)
    size = models.IntegerField(validators=[MaxValueValidator(9999)])
    refresh_rate = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    brightness = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    resolution = models.CharField(max_length=15)
    extra_characteristics = models.CharField(max_length=10000)
    photo = models.ImageField(upload_to='images')
    date_of_publication = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    user = models.ForeignKey(to=MoniTouringUser, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"