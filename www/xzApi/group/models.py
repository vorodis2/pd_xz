

from django.core.validators import validate_comma_separated_integer_list # Модуль для интов через запятую спиздил/вставил либы от джанги
from django.db import models #хрени для бд

from django.dispatch.dispatcher import receiver #Соб модель, 

from src.base_object import BaseObject # Ж1 Базовый обьект для всех ???
from src.base_object import TYPE_VERBOSE # Ж1 Базовые константы
from src.base_object_file import BaseObjectFile # Ж1 Бо для работы с файлами
from src.base_object_sort import BaseObjectSort, SORT_VERBOSE_NAME  # Ж1 сортировки запросов
from src.base_object_type import BaseObjectType # Ж1 хрен его знает можно наверно удолить, хз
from src.file_tools import write_now_time_to_file # Ж1 дерг групы>> запись изаенеия вервени для файла ???

# Ж1 по еволу создаюет клас и для сортировок
MODEL_NAME = "Group"
MODEL_TYPE_NAME = "GroupType"
MODEL_FILE_NAME = "GroupFile"
MODEL_SORT_NAME = "GroupSort"

# Ж1 хелпы для полей
TOVARS_VERBOSE = "Дополнительные товары"
PARENT_VERBOSE = "Родитель"
CHILDREN_VERBOSE = "Наследники"
TWORK_JSON = "Обьект типа работы"

# это функция 
def get_default_sort():
    created_object, is_created = GroupSort.objects.get_or_create(pk=1)
    return created_object.id


class GroupFile(BaseObjectFile):
    """
    Модель файла Group.
    """
    rel_obj = models.ForeignKey(MODEL_NAME, related_name='files', on_delete=models.CASCADE)


class GroupType(BaseObjectType):
    """
    Модель GroupType.
    """
    pass



   
class GroupSort2(BaseObjectSort):
    """
    Модель GroupSort.
    """
    pass




# расшаривает BaseObject>>> 
class Group(BaseObject):
    """
    Модель Group.
    """
    # files -- Field is created by Object3DFile relation to Object3D -> files
    object_type = models.ForeignKey(MODEL_TYPE_NAME,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    verbose_name=TYPE_VERBOSE)

    sort = models.ForeignKey("GroupType",
                             on_delete=models.SET_DEFAULT,
                             blank=False,
                             default=get_default_sort,
                             verbose_name=SORT_VERBOSE_NAME
                             )

    sort1 = models.ForeignKey(BaseObjectType,
                             on_delete=models.SET_DEFAULT,
                             blank=False,
                             default=get_default_sort,
                             verbose_name=SORT_VERBOSE_NAME
                             )

    sort2 = models.ForeignKey(BaseObjectType,
                             on_delete=models.SET_DEFAULT,
                             blank=False,
                             default=get_default_sort,
                             verbose_name=SORT_VERBOSE_NAME
                             )

    tWork = models.JSONField(
        verbose_name=TWORK_JSON,
        blank=False,
        null=True,
    )

    parent = models.IntegerField(
        verbose_name=PARENT_VERBOSE,
        default=-1,
        blank=False,
    )

    children = models.CharField(
        validators=[validate_comma_separated_integer_list],
        verbose_name=CHILDREN_VERBOSE,
        max_length=1024,
        default="",
        blank=True,
    )

    tovars = models.JSONField(
        verbose_name=TOVARS_VERBOSE,
        blank=False,
        null=True
    )
    tPost = models.JSONField(
        verbose_name=TOVARS_VERBOSE,
        blank=False,
        null=True
    )
    tDo = models.JSONField(
        verbose_name=TOVARS_VERBOSE,
        blank=False,
        null=True
    )

    # Num
    num = models.FloatField(default=0, blank=False)
    num1 = models.FloatField(default=0, blank=False)
    num2 = models.FloatField(default=0, blank=False)
    num3 = models.FloatField(default=0, blank=False)

    # Bool
    bool = models.BooleanField(default=False, blank=False)
    bool1 = models.BooleanField(default=False, blank=False)
    bool2 = models.BooleanField(default=False, blank=False)
    bool3 = models.BooleanField(default=False, blank=False)

    # Str
    text = models.TextField(blank=True, default="")
    text1 = models.TextField(blank=True, default="")
    text2 = models.TextField(blank=True, default="")
    text3 = models.TextField(blank=True, default="")
    pass





@receiver(models.signals.post_delete, sender=eval(MODEL_NAME))
@receiver(models.signals.post_save, sender=eval(MODEL_NAME))
def object_change_handler(sender, instance, **kwargs):
    write_now_time_to_file(eval(MODEL_NAME))


@receiver(models.signals.post_delete, sender=GroupFile)
def group_file_delete(sender, instance, **kwargs):
    """
    Удаление GroupFile.
    """
    assert issubclass(instance.__class__, BaseObjectFile)
    instance.src.delete(save=False)
