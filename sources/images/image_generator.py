from dataclasses import dataclass
from io import BytesIO
from typing import Tuple, ClassVar

import requests
from requests import Response
from PIL import Image

from sources.articles.article import Article


@dataclass
class ImageGenerator:

    __IMAGE_SIZE: ClassVar[int] = 400

    __article: Article

    def __post_init__(self):
        data: Response = requests.get(self.__article.get_image_url())
        self.__image: Image = Image.open(BytesIO(data.content))

        self.__format_to_square()
        self.__resize()

    def __format_to_square(self) -> None:
        rect: Tuple[int, int, int, int]

        width: int
        height: int
        width, height = self.__image.size

        if width >= height:
            rect = (
                (width - height) // 2,  # left
                0,                      # top
                (width + height) // 2,  # right
                height                  # bottom
            )
        else:
            rect = (
                0,                      # left
                (height - width) // 2,  # top
                width,                  # right
                (height + width) // 2   # bottom
            )

        self.__image = self.__image.crop(rect)

    def __resize(self) -> None:
        size: int = ImageGenerator.__IMAGE_SIZE
        self.__image = self.__image.resize((size, size))