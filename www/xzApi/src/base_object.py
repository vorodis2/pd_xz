from django.db import models
from mainxz import settings #Настройки сервера???? 
from django.contrib.auth.models import User


VERBOSE_NAME = 'Объект'
VERBOSE_NAME_PLURAL = 'Объекты'

MODEL_NAME_VERBOSE = 'Название объекта'

JSON_VERBOSE = 'JSON объекта'
ICON_VERBOSE = "Иконка"
ICON_ID_VERBOSE = "Айди иконки (нет защиты отношения в базе данных (можно задать любой))"
USER_VERBOSE = 'Пользователь объекта'
TYPE_MATERIAL_VERBOSE = 'Тип обьекта'
JSON_MATERIAL_VERBOSE = 'JSON объекта'

TYPE_VERBOSE = "Тип объекта"
SORT_VERBOSE = "Тип сортировки объекта"

MODEL_TYPE_NAME = "BaseObjectType"
MODEL_SORT_NAME = "BaseObjectSort"

ICON_DEFAULT_PATH = 'resources/image/notpic1.png'
APPROVED_VERBOSE = "Подтверждено (готово к использованию)"

TEXTS_VERBOSE = "Языки (обьект с переводами)"



# AUTH_USER_MODEL = 'django.contrib.auth.models' #модели юзера, для нашего проекта


class BaseObject(models.Model):
    """
    Базовый обхект.
    """

    class Meta: # :Ж1 в примерах такая хрень для интерфейса админ/форм/и гет/пост описалово
        pass
        verbose_name = VERBOSE_NAME
        verbose_name_plural = VERBOSE_NAME_PLURAL
        abstract = True  # :Ж1 разрешения наследоваться типо забанит поля которых нет а так не забанит
    # связи с таблицами   
    user = models.ForeignKey(User,# это кто?
                             on_delete=models.SET_NULL,# если грохнем юзера, дыра ресурсы не удоляються
                             null=True,# Можно ли этому полю задать null
                             blank=True,# Можно ли этому полю задать null  хз
                             verbose_name=USER_VERBOSE)# описалово
    
    # object_type = models.ForeignKey("BaseObjectType",
    #                                 on_delete=models.SET_NULL,
    #                                 null=True,
    #                                 blank=True,
    #                                 verbose_name=TYPE_VERBOSE)

    # # sort = models.ForeignKey(MODEL_SORT_NAME,
    # #                          on_delete=models.SET_DEFAULT,
    # #                          blank=False,
    # #                          verbose_name=SORT_VERBOSE,
    # #                          default=0
    # #                          )

    up = models.BooleanField(verbose_name=APPROVED_VERBOSE, default=False)#Bool это переменная для каждоги обьекта
    name = models.CharField(max_length=255,
                            blank=True,
                            verbose_name=MODEL_NAME_VERBOSE)
    texts = models.JSONField(verbose_name=TEXTS_VERBOSE,
                             blank=False,
                             null=True
                             )
    
    json = models.JSONField(blank=True,
                            null=True,
                            verbose_name=JSON_VERBOSE
                            )
    icon = models.CharField(max_length=512,
                            blank=False,
                            verbose_name=ICON_VERBOSE,
                            default=ICON_DEFAULT_PATH
                            )
    iconId = models.PositiveIntegerField(default=0, verbose_name=ICON_ID_VERBOSE)# инт не -
    # files <- assumed to be created by BaseObjectFile related_object
    # relation BaseObjectFile -> related_objects - will create files
    # in this model

    def __str__(self):# то как мы вывалим имя
        return f"{self.name or self.__class__.__name__} id: {str(self.pk)}"
