from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.crypto import get_random_string
from transliterate import slugify
from django.contrib.auth.models import User


class Transport(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            while Transport.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string(8)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("slug1", kwargs={"slug1": self.slug})
    

class Marka_Legkovoe_Avto(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(Transport, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            while Marka_Legkovoe_Avto.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string(8)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("slug2", kwargs={"slug1": self.parent.slug, "slug2": self.slug})

class Model_Legkovoe_Avto(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(Marka_Legkovoe_Avto, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            while Model_Legkovoe_Avto.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string(8)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("slug3", kwargs={"slug1": self.parent.parent.slug, "slug2": self.parent.slug, "slug3":self.slug})
    

class Legkovoe_Avto(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    deskription = models.TextField()
    mileage = models.IntegerField()
    year = models.IntegerField()
    price = models.IntegerField()
    type = TreeForeignKey(Transport, on_delete=models.PROTECT)
    marka = TreeForeignKey(Marka_Legkovoe_Avto, on_delete=models.PROTECT)
    parent = TreeForeignKey(Model_Legkovoe_Avto, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            while Legkovoe_Avto.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{get_random_string(8)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("slug3", kwargs={"slug1": self.parent.parent.parent.slug, "slug2": self.parent.parent.slug, "slug3":self.parent.slug, "slug4":self.slug})
    
class Image_Legkovoe_Avto(models.Model): 
    avto = models.ForeignKey(Legkovoe_Avto, on_delete=models.CASCADE)
    images = models.FileField()
    
