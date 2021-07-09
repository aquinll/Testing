import os
import configparser

from const.appconst import AppDefines
from const.textconst import AppMsg
from utils.apperror import ExitError

class UATConfig(object):

    def __init__(self):
        self.__config_file = configparser.ConfigParser()
        self.__load_cfg_file()

    def get_codecept_install_path(self):
        return self.__get_config(AppDefines.UAT_CODECEPT_INSTALL_PATH)

    def get_test_url(self):
        return self.__get_config(AppDefines.UAT_TEST_URL_CFG)

    def get_window_size(self):
        return self.__get_config(AppDefines.UAT_WINDOW_SIZE_CFG)

    def __get_config(self, config_name):
        return self.__config_file.get(AppDefines.UAT_CONFIG_SECTION
                    ,config_name) \
                    .strip(AppDefines.DOUBLE_QUOTE)

    def __load_cfg_file(self):
        file_path = os.path.join(os.getcwd()
                                ,AppDefines.UAT_CONFIG_PATH)
        if os.path.exists(file_path) == False:
            ExitError.exit(AppMsg.UAT_CONFIG_NOT_FOUND.format(os.getcwd()))
        self.__config_file.read(file_path)
