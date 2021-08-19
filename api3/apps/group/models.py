from django.core.validators import validate_comma_separated_integer_list
from django.db import models
import os

from api.settings import MEDIA_ROOT

from django.dispatch.dispatcher import receiver

from src.base_object import BaseObject#, TYPE_VERBOSE
from src.base_object_file import BaseObjectFile
from src.base_object_sort import BaseObjectSort#,  SORT_VERBOSE_NAME
# from src.base_object_type import BaseObjectType
from src.file_tools import write_now_time_to_file
from src.base_comment import BaseComment



MODEL_NAME = "Group"
# MODEL_TYPE_NAME = "GroupType"
# MODEL_FILE_NAME = "GroupFile"
# MODEL_SORT_NAME = "GroupSort"





def get_default_sort():
    created_object, is_created = GroupSort.objects.get_or_create(pk=1)
    return created_object.id


class GroupFile(BaseObjectFile):
    """
    Модель файла Group.
    """
    rel_obj = models.ForeignKey(MODEL_NAME, related_name='files', on_delete=models.CASCADE)



# class GroupType(BaseObjectType):
#     """
#     Модель GroupType.
#     """
#     pass


class GroupSort(BaseObjectSort):
    """
    Модель GroupSort.
    """
    pass




class Group(BaseObject):
    """
    Модель Group.
    """
    # files -- Field is created by Object3DFile relation to Object3D -> files
    # object_type = models.ForeignKey(GroupType,
    #                                 on_delete=models.SET_NULL,
    #                                 null=True,
    #                                 blank=True,
    #                                 verbose_name="тип")

    


    sort = models.ForeignKey(GroupSort,
                             on_delete=models.SET_DEFAULT,
                             blank=False,
                             default=get_default_sort,
                             verbose_name="Сортировка sort"
                             )



    ru = models.CharField(max_length=255,
                            blank=True,
                            verbose_name='текст ru',
                            default='programText(Вставка)'
                        )
    en = models.CharField(max_length=255,
                            blank=True,
                            verbose_name='text en',
                            default='programText(Вставка)',
                        )

    def __str__(self):
        return "{}".format(self.ru)

    pass

class GroupComment(BaseComment):
    """
    Модель GroupSort.
    """

    comment_obj = models.ForeignKey(Group, related_name='comments',on_delete=models.CASCADE, null=True, verbose_name='koment')

    # xzobj = models.ForeignKey(Group, related_name='files', on_delete=models.CASCADE)





@receiver(models.signals.post_delete, sender=Group)
@receiver(models.signals.post_save, sender=Group)
@receiver(models.signals.post_delete, sender=GroupFile)
@receiver(models.signals.post_save, sender=GroupFile)
def object_change_handler(sender, instance, **kwargs):
    write_now_time_to_file(Group)



@receiver(models.signals.post_save, sender=Group)
def auto_ru_en(sender, instance, **kwargs):
    if instance.ru == 'programText(Вставка)':
        instance.ru = MODEL_NAME+"_"+str(instance.id)+"_ru"
        instance.save()

    if instance.en == 'programText(Вставка)':
        instance.en = MODEL_NAME+"_"+str(instance.id)+"_en"
        instance.save()  

    


@receiver(models.signals.post_delete, sender=GroupFile)
def group_file_delete(sender, instance, **kwargs):
    """
    Удаление GroupFile.
    """
    assert issubclass(instance.__class__, BaseObjectFile)
    file_name = os.path.basename(str(instance.src))
    dir_path = str(instance.src).replace(file_name, "")
    dir_path = MEDIA_ROOT / dir_path
    instance.src.delete(save=False)

    if not os.listdir(dir_path):
        os.removedirs(dir_path)

