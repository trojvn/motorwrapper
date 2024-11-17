import contextlib

from motor import MotorCollection, MotorDatabase

from .base import MotorBase
from .models import MotorOptions


class MotorUser(MotorBase):
    def __init__(self, options: MotorOptions, collection: str):
        self.__collection = collection
        super().__init__(options)

    @property
    def db(self) -> MotorDatabase:
        return self[self.motor_options.db_name]

    @property
    def collection(self) -> MotorCollection:
        return self.db[self.__collection]

    async def check_auth(self) -> bool:
        """Проверка авторизации"""
        with contextlib.suppress(Exception):
            await self.collection.find_one({"_id": 1})
            return True
        return False
