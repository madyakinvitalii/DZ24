import os
from typing import Dict, List

from marshmallow import ValidationError

from classes.functions import create_generator
from consts import DEF_TYPE_COMMAND, DATA_DIR
from schemes.request import RequestSchema


class UserRequest:
    """
    Класс объектов "запрос"
    """

    def __init__(self, user_request: Dict[str, str]):
        correct_data = self._is_correct_request(user_request)
        self.__cmd1 = correct_data['cmd1']
        self.__value1 = correct_data['value1']
        self.__cmd2 = correct_data['cmd2']
        self.__value2 = correct_data['value2']
        # Проверка на наличие в запросе не обязательного поля file_name
        if "file_name" in correct_data.keys():
            self.__file_name = os.path.join(DATA_DIR, correct_data['file_name'])
        else:
            # Устанавливаем значение по умолчанию
            self.__file_name = os.path.join(DATA_DIR, "apache_logs.txt")

    def _is_correct_request(self, user_request: Dict[str, str]) -> Dict[str, str]:
        """
        Функция валидации запроса
        """
        try:
            return RequestSchema().load(user_request)
        except ValidationError as err:
            raise err

    def create_procedure(self) -> List[str]:
        """
        Функция формирования и обработки файла по данным из запроса
        """
        file_gen = create_generator(self.file_name)
        preparing_data = DEF_TYPE_COMMAND[self.cmd1](value=self.value1, data=file_gen)
        return list(DEF_TYPE_COMMAND[self.cmd2](value=self.value2, data=preparing_data))

    @property
    def cmd1(self) -> str:
        return self.__cmd1

    @property
    def cmd2(self) -> str:
        return self.__cmd2

    @property
    def value1(self) -> str:
        return self.__value1

    @property
    def value2(self) -> str:
        return self.__value2

    @property
    def file_name(self) -> str:
        return self.__file_name
