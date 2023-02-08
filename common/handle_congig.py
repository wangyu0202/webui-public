import os
from configparser import ConfigParser
from common import handle_path


class MyConfig(ConfigParser):

    def __init__(self):
        super().__init__()

        c = ConfigParser()
        c.read(os.path.join("xx.ini"), encoding="utf8")
        env = c.get("", "")

        if env == "":
            self.read(os.path.join("xx.ini"), encoding="utf8")

        elif env == "":
            self.read(os.path.join("xx.ini"), encoding="utf8")

        else:
            self.read(os.path.join("xx.ini"), encoding="utf8")

    def write_data(self, select, option, value, file_name=os.path.join(handle_path.CONF_DIR, "conf.ini")):
        self.set(select, option, value)
        self.write(fp=open(file_name, "w", encoding="utf8"))


conf = MyConfig()
