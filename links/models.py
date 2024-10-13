from django.db import models
from django.utils.text import slugify  # converts a string into a slug
# slugify('Hello World') -> 'hello-world'


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"

    def click(self):
        self.clicks += 1
        self.save()

    # save method is called when an instance of the model is saved
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        # call the save method of the parent class
        return super().save(*args, **kwargs)
