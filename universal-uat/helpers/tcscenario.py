from const.textconst import AppMsg
from const.tcconst import TCDefines
from helpers.tccase import TestCaseHandler
from utils.fileaccess import CreateFile

class TestScenarioHandler(object):

    def __init__(self, parameters):
        self.__tc_count = 0
        self.__codecept_tc = {}
        self.__set_scenario(parameters)

    @property
    def name(self):
        return self.__name

    def add_tc(self, test_case_obj):
        self.__tc_count += 1
        self.__codecept_tc[ \
            TCDefines.TC_KEY.format(self.__tc_count) \
            + TCDefines.PERIOD + \
            test_case_obj.name] = test_case_obj

    def write_tc(self, file_path):
        contents = self.__get_file_contents()
        CreateFile(file_path, self.name).write(contents)

    def __get_file_contents(self):
        test_case = ""
        for key in self.__codecept_tc:
            if type(self.__codecept_tc[key]) == TestCaseHandler:
                test_case += self.__codecept_tc[key].get_tc_steps()
        test_scenario = self.__codecept_tc[TCDefines.TC_SCENARIO_KEY]
        test_scenario += TCDefines.TC_SCENARIO_BLOCK.replace( \
             TCDefines.TC_LIST_TEXT, test_case)
        return test_scenario

    def __set_scenario(self, parameters):
        self.__name = parameters[1].strip(TCDefines.STRING_MARK)
        self.__codecept_tc[TCDefines.TC_SCENARIO_KEY] = \
            TCDefines.TC_SCENARIO_CLASS.format(self.__name)
