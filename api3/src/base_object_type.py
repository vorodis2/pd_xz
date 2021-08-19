from django.db import models


TYPE_VERBOSE = 'Тип'
TYPE_VERBOSE_PLURAL = 'Типы'
TYPE_VERBOSE_NAME = 'Название типа'


class BaseObjectType(models.Model):
    """
    Тип базового обьекта.
    """

    class Meta:
        verbose_name = TYPE_VERBOSE
        verbose_name_plural = TYPE_VERBOSE_PLURAL
        abstract = True

    name = models.CharField(max_length=255,
                            blank=True,
                            verbose_name=TYPE_VERBOSE_NAME)

    def __str__(self):
        return "{}".format(self.name or self.__class__.__name__ + str(self.pk))
