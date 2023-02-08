import logging
from common import handle_congig
import os
from common import handle_path
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d')

log_level = handle_congig.conf.get("log", "log_level")
sh_level = handle_congig.conf.get("log", "sh_level")
fh_level = handle_congig.conf.get("log", "fh_level")
log_name = handle_congig.conf.get("log", "log_name")

file_path = os.path.join(handle_path.LOG_DIR, "log-{}.log".format(now_time))


class MyLogging(object):

    def __new__(cls, *args, **kwargs):

        mylog = logging.getLogger("mylog")
        mylog.setLevel(log_level)
        sh = logging.StreamHandler()
        sh.setLevel(sh_level)
        fh = logging.FileHandler(file_path, encoding="utf8")
        sh.setLevel(fh_level)
        mylog.addHandler(sh)
        mylog.addHandler(fh)
        formatter = logging.Formatter("%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s")
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        return mylog


logs = MyLogging()
