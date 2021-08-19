import os

import logging

from django.contrib.auth import logout
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

from api.settings import EMAIL_HOST_USER

utils_logger = logging.getLogger("utils")


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    request = instance.request

    email_plaintext_message = "{HOST_URL}?token={TOKEN}".format(
        HOST_URL=request.build_absolute_uri().replace('/api/v1', ''),
        INNER_URI=reverse('api_v1:password_reset:reset-password-request'),
        TOKEN=reset_password_token.key
    )

    send_mail(
        # title:
        "Сброс пароля для Калейдоплан",
        # message:
        email_plaintext_message,
        # from:
        EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )


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
        foreign_object_pk_str = str(foreign_object_pk)
    except AttributeError as err:
        utils_logger.error(
            "While creating path to save file to instance of {} error occurred."
            " Reason: {}".format(instance.__class__.__name__, err)
        )
        foreign_object_pk_str = ""

    base_file_name = os.path.basename(filename)

    assert None not in (base_file_name, foreign_object_pk_str, instance_class_name)
    return os.path.join(instance_class_name, foreign_object_pk_str, base_file_name)







from django.http import HttpResponse
from rest_framework import status
import json

from api.settings import MEDIA_ROOT, LAST_CHANGE_JSON_POSTFIX
from src.file_tools import read_dict_from_file


def get_counter_response_from_file(got_model_instance) -> HttpResponse:
    model_root_path = MEDIA_ROOT
    time_json_file_name = got_model_instance.__name__ + LAST_CHANGE_JSON_POSTFIX
    got_file_path = model_root_path / time_json_file_name

    try:
        with open(got_file_path, "r") as fil:
            return HttpResponse(
                json.dumps(
                    read_dict_from_file(full_path=got_file_path, raise_error=True)
                ),
                status=status.HTTP_200_OK,
                content_type="Application/json"
            )
    except FileNotFoundError as ex:
        return HttpResponse(
            reason="Counter is not created yet.",
            status=status.HTTP_404_NOT_FOUND,
        )
    except BaseException as ex:
        return HttpResponse(
            json.dumps({"reason": str(ex)}),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

