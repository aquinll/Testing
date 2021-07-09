from const.tcconst import TCDefines
from helpers.tccmd.oneparam import OneParamCmd

class TestCaseHandler(object):

    def __init__(self, name=TCDefines.TC_FIRST_NAME):
        self.__name = name.strip(TCDefines.STRING_MARK)
        self.__codecept_tc_steps = {}
        self.__codecept_tc_steps[TCDefines.TEST_CASE_KEY] = \
            TCDefines.TEST_CASE_FUNCTION.format(self.__name)
        if (name == TCDefines.TC_FIRST_NAME):
            self.add_before_step()

    @property
    def name(self):
        return self.__name

    def add_before_step(self):
        self.__codecept_tc_steps[TCDefines.TEST_STEPS_KEY] = [ OneParamCmd() ]

    def add_tc_step(self, tc_step_obj):
        if TCDefines.TEST_STEPS_KEY not in self.__codecept_tc_steps:
            self.__codecept_tc_steps[TCDefines.TEST_STEPS_KEY] = []

        self.__codecept_tc_steps[TCDefines.TEST_STEPS_KEY] \
            .append(tc_step_obj)

    def get_tc_steps(self):
        tc_block = ""
        tc_steps = self.__codecept_tc_steps[TCDefines.TEST_CASE_KEY]
        for step in self.__codecept_tc_steps[TCDefines.TEST_STEPS_KEY]:
            if type(step.code) == list:
                for line in step.code:
                    tc_block += line
            else:
                tc_block += step.code
        return tc_steps + \
               TCDefines.TEST_CASE_BLOCK.replace( \
                     TCDefines.TC_STEPS_TEXT
                    ,tc_block)
