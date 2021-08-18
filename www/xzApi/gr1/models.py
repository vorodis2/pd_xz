from django.db import models

from django.core.validators import validate_comma_separated_integer_list # Модуль для интов через запятую спиздил/вставил либы от джанги
from django.dispatch.dispatcher import receiver #Соб модель, 


from src.base_object import BaseObject # Ж1 Базовый обьект для всех ???
from src.base_object_type import BaseObjectType # Ж1 хрен его знает можно наверно удолить, хз



class GrType(BaseObjectType):
    pass


class Gr1(BaseObject):
	object_type = models.ForeignKey(GrType,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    verbose_name="TYPE_VERBOSEzdsdsgf")
	
	pass




# Create your models here.
