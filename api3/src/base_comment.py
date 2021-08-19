from django.db import models
from api import settings

from django.contrib.auth.models import User



class BaseComment(models.Model):
    """
    Базовый обхект.
    """

    class Meta:
        verbose_name = "комент"
        verbose_name_plural = "коменты"
        abstract = True

    title = models.CharField(max_length=255,
                            blank=False,
                            default="Не установлено",
                            verbose_name="title")

    user = models.ForeignKey(User,#settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=False,
                             verbose_name="автор")
    
    text = models.TextField(max_length=1255,
                            blank=True,
                            verbose_name="комент")


    def __str__(self):
        return f"{self.title or self.__class__.__name__} id: {str(self.pk)}"
  