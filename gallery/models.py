from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):
    description = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    #
    # def get_source(self):
    #     directory = self.image.name.split('/gallery/')
    #     return directory[1]
    #
    # def get_name(self):
    #     directory = self.image.name.split('/')
    #     return directory[-1]

    # def __str__(self):
    #     return self.get_name()
