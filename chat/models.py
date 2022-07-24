from django.db import models
from account.models import Account

# Create your models here.

class Room(models.Model):
        name            = models.CharField("Name", max_length=50)
        slug            = models.SlugField("Slug", unique=True)
        owner           = models.ForeignKey("account.Account", verbose_name="Owner", related_name="owner", on_delete=models.CASCADE)
        # date_created    = models.DateTimeField("Date Created", auto_now=False, auto_now_add=False)

        def __str__(self):
                return self.name

class Message(models.Model):
        room            = models.ForeignKey(Room, verbose_name="Room", related_name='room', on_delete=models.CASCADE)
        user            = models.ForeignKey("account.Account", verbose_name="User", related_name="user", on_delete=models.CASCADE)
        message         = models.TextField()
        date_created    = models.DateTimeField("Date Created", auto_now_add=True)

        class Meta:
                ordering = ('date_created',)