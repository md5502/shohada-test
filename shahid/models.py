from django.db import models


class Shahid(models.Model):
    name = models.CharField(max_length=200)
    lname = models.CharField(max_length=200, verbose_name="last name")
    martyrdom_location = models.CharField(max_length=200)
    martyrdom_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="shohada_images")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.lname}"
