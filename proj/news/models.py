from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField("Name" ,  max_length=50)
    anons = models.CharField("Anons", max_length=250)
    full_text = models.TextField("Statia")
    date = models.DateTimeField("Day of publication")

    def __str__(self):
        return self.title
