from django.db import models

from mainxz.utils import create_file_upload_path

FILE_VERBOSE = 'Файл'
FILE_VERBOSE_PLURAL = 'Файлы'


class BaseObjectFile(models.Model):
    """
    Базовый класс файла обьекта.
    """

    class Meta:
        verbose_name = FILE_VERBOSE
        verbose_name_plural = FILE_VERBOSE_PLURAL
        abstract = True

    src = models.FileField(upload_to=create_file_upload_path, verbose_name='Файл')

    def __str__(self):
        return "{}".format(self.__class__.__name__ + str(self.pk))