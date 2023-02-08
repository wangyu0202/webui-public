import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CASE_DIR = os.path.join(BASE_DIR, "test_case")
REPORT_DIR = os.path.join(BASE_DIR, "test_result/reports")
LOG_DIR = os.path.join(BASE_DIR, "test_result/logs")
ERROR_IMAGE_DIR = os.path.join(BASE_DIR, "test_result/error_images")
CONF_DIR = os.path.join(BASE_DIR, "confs")
DATA_DIR = os.path.join(BASE_DIR, "test_data")
