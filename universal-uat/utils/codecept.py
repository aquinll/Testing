import os
import shutil
import subprocess

from const.appconst import AppDefines
from const.textconst import AppMsg
from utils.apperror import ExitError
from utils.fileaccess import CreateFile

class CodeCept(object):

    def __init__(self, uat_config, parameters):
        self.__uat_config = uat_config
        self.__path = self.__find_path()
        self.__get_test_path(parameters)

    def run(self):
        self.__create_codecept_cfg()
        self.__rebuild_codecept_exec_paths()
        self.__run_codecept( \
            AppDefines.CODECEPT_RUN_TEST_PARAMS.format(self.__target_test))

    def __rebuild_codecept_exec_paths(self):
        self.__remove_exec_path(AppDefines.TEST_DATA_PATH)
        self.__remove_exec_path(AppDefines.TEST_ENV_PATH)
        self.__remove_exec_path(AppDefines.TEST_OUTPUT_PATH)
        self.__remove_exec_path(AppDefines.TEST_SUPPORT_PATH)
        self.__run_codecept(AppDefines.CODECEPT_BUILD_PARAM)

    def __remove_exec_path(self, target_path):
        target_full_path = os.path.join(self.__test_path
                                       ,AppDefines.TEST_PATH
                                       ,target_path)
        if os.path.exists(target_full_path):
            shutil.rmtree(target_full_path)

    def __run_codecept(self, parameters):
        os.system(self.__path + parameters)

    def __get_test_path(self, parameters):
        if len(parameters) > 1:
            self.__test_path = self.__get_exact_value(parameters[0])
            self.__target_test = self.__get_exact_value(parameters[1])

        elif len(parameters) > 0:
            self.__test_path = self.__get_exact_value(parameters[0])
            self.__target_test = ""

        else:
            self.__test_path = os.getcwd()
            self.__target_test = ""

    def __get_exact_value(self, parameter):
        if parameter == AppDefines.CURRENT_WORKING_DIR:
            return os.getcwd()
        else:
            if os.path.exists(parameter) == False:
                ExitError.exit( \
                    AppMsg.TC_WORKING_FOLDER_NOT_FOUND.format(parameter))
            return parameter

    def __create_codecept_cfg(self):
        contents = AppMsg.CODECEPTION_STANDARD_CONFIG \
                         .format(self.__uat_config.get_test_url()
                                ,self.__uat_config.get_window_size())
        CreateFile(self.__test_path
                  ,AppDefines.CODECEPT_FILE_NAME
                  ,tc_file=False).write(contents)

    def __find_path(self):
        file_path = AppDefines.CODECEPT_EXEC_NAME
        path_run = subprocess.run([file_path
                        , AppDefines.CODECEPT_VERSION]
                        , shell=True
                        , capture_output=True)
        path_found = path_run.returncode == 0

        if path_found == False:
            file_path = os.path.join( \
                                self.__uat_config.get_codecept_install_path()
                              , AppDefines.CODECEPT_EXEC_NAME)
            path_run = subprocess.run([file_path
                            , AppDefines.CODECEPT_VERSION]
                            , shell=True
                            , capture_output=True)
            path_found = path_run.returncode == 0

        if path_found == False:
            ExitError.exit(AppMsg.CODECEPTION_IS_NOT_INSTALLED)

        return file_path
