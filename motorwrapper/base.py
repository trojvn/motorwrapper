from motor import MotorClient

from .models import MotorOptions


class MotorBase(MotorClient):
    def __init__(self, options: MotorOptions):
        self.__motor_options = options
        while True:
            try:
                super().__init__(
                    host=options.host,
                    port=options.port,
                    username=options.user,
                    password=options.pswd,
                    authSource=options.db_name,
                    connectTimeoutMS=60000,
                )
                break
            except Exception:
                pass

    @property
    def motor_options(self) -> MotorOptions:
        return self.__motor_options
