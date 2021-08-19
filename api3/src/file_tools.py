import os
import json
import time

from api.settings import LAST_CHANGE_JSON_POSTFIX, MEDIA_ROOT


def write_now_time_to_file(got_model_instance):
    time_json_file_name = got_model_instance.__name__ + LAST_CHANGE_JSON_POSTFIX

    now_time = str(time.time())
    os.makedirs(MEDIA_ROOT, exist_ok=True)

    write_dict_to_file(
        got_object={"last_change_time": now_time},
        full_path=MEDIA_ROOT / time_json_file_name,
        create_path=True,
        raise_error=True
    )


def write_dict_to_file(got_object: dict, full_path: str, create_path: bool = True, raise_error: bool = True):
    assert type(got_object) == dict
    assert full_path

    file_name = os.path.basename(full_path)
    directory_path = str(full_path).replace(file_name, "")

    if create_path:
        os.makedirs(directory_path, exist_ok=True)

    try:
        with open(full_path, "w") as fil:
            json.dump(got_object, fp=fil)
    except OSError:
        if raise_error:
            raise


def read_dict_from_file(full_path: str, raise_error: bool = True):
    error = None
    try:
        with open(full_path, "r") as fil:
            return json.load(fil)
    except json.JSONDecodeError as err:
        error = err
    except FileNotFoundError as err:
        error = err
    except OSError as err:
        error = err

    if raise_error and error:
        raise
