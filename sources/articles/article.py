from dataclasses import dataclass
from typing import ClassVar, Tuple

from sources.utils.string import String


@dataclass
class Article:

    __MAX_LENGTH_DESCRIPTION: ClassVar[int] = 250
    __FORBIDDEN_CHARS_DESCRIPTION: ClassVar[Tuple[str]] = ("-", "...")

    __description: str
    __source: str
    __image_url: str
    __link: str

    def __post_init__(self):
        if self.is_complete():
            self.__description = String.decode(self.__description)

    def is_complete(self) -> bool:
        return not (self.__description is None or self.__source is None or
                    self.__image_url is None or self.__link is None)

    def is_valid(self) -> bool:
        char: str
        return len(self.__description) <= Article.__MAX_LENGTH_DESCRIPTION and \
            all(char not in self.__description for char in Article.__FORBIDDEN_CHARS_DESCRIPTION)

    def get_description(self) -> str:
        return self.__description

    def get_source(self) -> str:
        return self.__source

    def get_image_url(self) -> str:
        return self.__image_url

    def get_link(self) -> str:
        return self.__link