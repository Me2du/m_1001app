from django.db import models

# Create your models here.
class mithu_1001(models.Model):
    text=models.CharField(max_length=45)

    def __str__(self):
        return self.text