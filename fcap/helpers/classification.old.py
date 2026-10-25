from io import BytesIO
from PIL import Image
import os
import threading

from requests import post as rpost

from . import exceptions
from . import models
from . import hash

_created_dirs = set()
_created_dirs_lock = threading.Lock()


def ensure_dir(path: str) -> None:
    with _created_dirs_lock:
        if path not in _created_dirs:
            os.makedirs(path, exist_ok=True)
            _created_dirs.add(path)


def predict_image(img: bytes, challenge: models.Challenge, raw_image: bytes) -> str:
    payload = {"image": img, "question": challenge.variant}

    for _ in range(5):
        try:
            response = rpost(
                "http://2.58.15.152:9876/predict", json=payload, timeout=10
            )
            response_data = response.json()
            if response.status_code == 200 and not response_data.get("error", True):
                predicted_index = response_data.get("predicted", None)
                break
            else:
                raise exceptions.PredictionError(
                    f"Got {response.status_code}: {response.json()}"
                )
        except:  # NOQA
            continue
    else:
        raise exceptions.PredictionError(
            "Failed to predict image in max number of attempts"
        )
    #image: Image.Image = Image.open(BytesIO(raw_image))
    #filename = hash.md5hash(raw_image)

    #path = os.path.join("E:", "Dataset", challenge.variant)
    #filename_full = os.path.join(path, f"{filename}_{predicted_index}.webp")
    #ensure_dir(path)
    #image.save(filename_full, "WEBP", quality=80)
    return predicted_index
