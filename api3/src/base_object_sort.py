from django.db import models



class BaseObjectSort(models.Model):
    class Meta:
        verbose_name = "Сортировка"
        verbose_name_plural = "Сортировки"
        abstract = True

    name = models.CharField(max_length=255,
                            blank=False,
                            default="Не установлено",
                            verbose_name="Сортировка")

    def __str__(self):
        return "{}".format(self.name or self.__class__.__name__ + str(self.pk))
