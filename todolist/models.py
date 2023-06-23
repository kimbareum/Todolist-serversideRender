from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.name}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    is_clear = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} - {self.title}'
