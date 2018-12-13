from django.db import models
from ckeditor.fields import RichTextField


class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.company
