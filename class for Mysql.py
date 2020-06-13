from django.db import models

class Game (models.Model):
    num = models.PositiveIntegerField("id")
    date = models.DateField(auto_now=False, auto_now_add=False)
    reiting = models.PositiveIntegerField("reiting", default=0)
    url = models.SlugField(maxlenght=100)

    def __str__(self):
        return self.num
