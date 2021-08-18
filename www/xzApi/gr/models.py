from django.db import models

from django.core.validators import validate_comma_separated_integer_list # Модуль для интов через запятую спиздил/вставил либы от джанги
from django.dispatch.dispatcher import receiver #Соб модель, 


from src.base_object import BaseObject # Ж1 Базовый обьект для всех ???
from src.base_object_type import BaseObjectType # Ж1 хрен его знает можно наверно удолить, хз
from src.base_object_sort import BaseObjectSort

from src.base_object_file import BaseObjectFile


class GrType(BaseObjectType):
    pass

class GrSort(BaseObjectSort):
    """
    Модель Group1Sort.
    """
    pass  

class GrFile(BaseObjectFile):
    """
    Модель файла Group1.
    """
    #rel_obj = models.ForeignKey(MODEL_NAME, related_name='files', on_delete=models.CASCADE)
    pass




# берет либо создают
def get_default_sort():
    created_object, is_created = GrSort.objects.get_or_create(pk=1)
    return created_object.id



class Gr(BaseObject):
	file = models.ManyToManyField(GrFile, null=True, blank=True, verbose_name="Файл обьекта") # on_delete=models.SET_NULL, 

	object_type = models.ForeignKey(GrType,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    verbose_name="grType")
	print("#########################")
	print(object_type)
	

	sort = models.ForeignKey(GrSort,
                             on_delete=models.SET_DEFAULT,
                             blank=False,
                             default=get_default_sort,
                             verbose_name="Описалово подсказки"

                             )
	pass




@receiver(models.signals.post_delete, sender=GrFile)
def group1_file_delete(sender, instance, **kwargs):
    """
    Удаление Group1File.
    """
    assert issubclass(instance.__class__, BaseObjectFile)
    instance.src.delete(save=False)

