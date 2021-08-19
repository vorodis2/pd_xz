from django.db import models
from api import settings

from django.contrib.auth.models import User


class BaseObject(models.Model):

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        abstract = True


    user = models.ForeignKey( User,#settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Юзер user"
    )

    # апнутые проекты
    up = models.BooleanField(verbose_name="апрув up", default=False)

    # Общедоступная хрень которую показывать
    public = models.BooleanField(verbose_name="публичны public", default=False)

    # имя
    name = models.CharField("Имя name", max_length=255, blank=True)

    # базовый обьект для этой модели
    json = models.JSONField("JSON json", blank=True, null=True )

    # путь к картинке
    icon = models.CharField("Иконка icon", max_length=512, blank=False, default='favicon.ico')
   
    # идишник картинки
    iconId = models.PositiveIntegerField("ид Файла iconId",default=0 )


    def __str__(self):
        return f"{self.name or self.__class__.__name__} id: {str(self.pk)}"
  