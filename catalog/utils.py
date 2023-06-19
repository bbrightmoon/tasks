from io import BytesIO
from PIL import Image
from django.core.files import File
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination


def compress(image):
    if not image:
        return None
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=30)
    new_im = File(im_io, name=image.name)
    return new_im


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10










