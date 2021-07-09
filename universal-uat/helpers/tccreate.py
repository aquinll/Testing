import os

from const.appconst import AppDefines
from const.textconst import AppMsg
from utils.apperror import ExitError
from helpers.tcparser import TCParser

class GenerateTestCase(object):

    def __init__(self, parameters):
        self.__process_params(parameters)
        self.__check_valid_working_path()
        self.__check_output_path()

    def run(self):
        if len(self.__target_files) > 1:
            for file in self.__target_files:
                self.__parse_tc(file)
        else:
            self.__parse_tc(self.__target_files[0])

    def __check_output_path(self):
        self.__output_path = os.path.join(self.__file_path
                                         ,AppDefines.TEST_PATH)
        if os.path.exists(self.__output_path) == False:
            os.mkdir(self.__output_path)

    def __process_params(self, parameters):
        if len(parameters) > 1:
            self.__file_path = self.__get_exact_value(parameters[0])
            self.__target_file = self.__get_exact_value(parameters[1])

        elif len(parameters) > 0:
            self.__file_path = self.__get_exact_value(parameters[0])
            self.__target_file = AppDefines.ALL_TEST_CASES

        else:
            self.__file_path = os.getcwd()
            self.__target_file = AppDefines.ALL_TEST_CASES

    def __get_exact_value(self, parameter):
        if parameter == AppDefines.CURRENT_WORKING_DIR:
            return os.getcwd()
        elif parameter == AppDefines.ALL_TESTS:
            return AppDefines.ALL_TEST_CASES
        else:
            return parameter

    def __check_valid_working_path(self):
        if os.path.exists(self.__file_path) == False:
            ExitError.exit( \
                AppMsg.TC_WORKING_FOLDER_NOT_FOUND \
                      .format(self.__file_path))
        self.__get_valid_tc_files()

    def __get_valid_tc_files(self):
        if self.__target_file == AppDefines.ALL_TEST_CASES:
            self.__get_tc_files_in_path()

        else:
            target_file_path = os.path.join(self.__file_path
                                           ,self.__target_file)
            if os.path.exists(target_file_path) == False:
                ExitError.exit( \
                    AppMsg.TC_WORKING_FILES_NOT_FOUND \
                          .format(target_file_path))

            else:
                self.__target_files = [ target_file_path ]

    def __get_tc_files_in_path(self):
        self.__target_files = []
        for item in os.listdir(self.__file_path):
            item = os.path.join(self.__file_path, item)
            if os.path.isfile(item) and AppDefines.TC_FILE_EXT in item:
                self.__target_files.append(item)

        if len(self.__target_files) == 0:
            target_file_path = os.path.join(self.__file_path
                                           ,self.__target_file)
            ExitError.exit(AppMsg.TC_WORKING_FILES_NOT_FOUND \
                                 .format(target_file_path))

    def __parse_tc(self, file_path):
        test_case_in = TCParser(file_path)
        test_case_in.parse()
        test_case_out = test_case_in.tc_scenario
        test_case_out.write_tc(self.__output_path)
