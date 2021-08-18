import os

import logging

from django.contrib.auth import logout
from django.dispatch import receiver
from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# from planback.settings import EMAIL_HOST_USER

utils_logger = logging.getLogger("utils")


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     request = instance.request

#     email_plaintext_message = "{HOST_URL}?token={TOKEN}".format(
#         HOST_URL=request.build_absolute_uri().replace('/api/v1', ''),
#         INNER_URI=reverse('api_v1:password_reset:reset-password-request'),
#         TOKEN=reset_password_token.key
#     )

#     send_mail(
#         # title:
#         "Сброс пароля для Калейдоплан",
#         # message:
#         email_plaintext_message,
#         # from:
#         EMAIL_HOST_USER,
#         # to:
#         [reset_password_token.user.email]
#     )


def social_user_custom(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
        elif not user:
            user = social.user
    return {
        'social': social,
        'user': user,
        'is_new': user is None,
        'new_association': False
    }


def create_file_upload_path(instance, filename):
    """
    Генерирует и возвращает путь для нового,
    загружаемого на сервер файла.
    :param instance: обьект, куда будет
        пристегнут этот файл.
    :param filename: Оригинальное имя файла, что
        было принято сервером от клиента
    :return: Строка с сформированным путем.
    """

    try:
        instance_class_name = str(type(instance)).split(".")[0].split("\'")[-1]
    except BaseException as err:
        utils_logger.error(
            "While creating directory name to save {} - error occurred."
            " Reason: {}".format(instance.__class__.__name__, err)
        )
        instance_class_name = str(instance.__class__.__name__)
        instance_class_name = instance_class_name.lower()
        instance_class_name = instance_class_name.replace("file", "")

    try:
        foreign_object_pk = getattr(instance, "rel_obj" + "_id")
    except AttributeError as err:
        utils_logger.error(
            "While creating path to save file to instance of {} error occurred."
            " Reason: {}".format(instance.__class__.__name__, err)
        )
    foreign_object_pk_str = "files"

    base_file_name = os.path.basename(filename)

    assert None not in (base_file_name, foreign_object_pk_str, instance_class_name)
    return os.path.join(instance_class_name, foreign_object_pk_str, base_file_name)
