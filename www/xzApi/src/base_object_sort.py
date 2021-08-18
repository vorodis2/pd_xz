from django.db import models


SORT_VERBOSE = 'Поле сортировки'
SORT_VERBOSE_PLURAL = 'Поля сортировок'
SORT_VERBOSE_NAME = 'Название параметра сортировки'
SORT_DEFAULT_NAME = "Не установлено"


class BaseObjectSort(models.Model):
    """
    Базовый класс типа сортировки обьекта.
    """

    class Meta:
        verbose_name = SORT_VERBOSE
        verbose_name_plural = SORT_VERBOSE_PLURAL
        abstract = True

    name = models.CharField(max_length=255,
                            blank=False,
                            default=SORT_DEFAULT_NAME,
                            verbose_name=SORT_VERBOSE_NAME)

    def __str__(self):
        return "{}".format(self.name or self.__class__.__name__ + str(self.pk))
