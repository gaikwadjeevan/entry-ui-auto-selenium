import configparser

from tests.conftest import project_root

config = configparser.RawConfigParser()
config.read(f"{project_root}/pytest.ini")


class readConfig:

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password


rc = readConfig()
print(rc)
