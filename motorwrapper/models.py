from dataclasses import dataclass


@dataclass
class MotorOptions:
    user: str
    pswd: str
    host: str
    db_name: str = ""
    port: int = 27017

    def __post_init__(self):
        if not self.db_name:
            self.db_name = self.user
