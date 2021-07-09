from const.tcconst import TCDefines
from const.textconst import AppMsg
from helpers.tcscenario import TestScenarioHandler
from helpers.tccase import TestCaseHandler
from helpers.tccmd.multiparam import CheckCmd
from helpers.tccmd.oneparam import CheckURLCmd, ClickCmd
from helpers.tccmd.twoparam import EnterCmd
from utils.apperror import ExitError

class TCParser(object):

    def __init__(self, file_path):
        self.__tc_scenario = None
        self.__tc_steps = None
        self.__file_path = file_path

    @property
    def tc_scenario(self):
        return self.__tc_scenario

    def parse(self):
        with open(self.__file_path
                 ,TCDefines.READ_ACCESS
                 ,encoding = TCDefines.UTF8_ENCODING) as test_case:
            for line in test_case:
                if line[0] == TCDefines.COMMENT_MARK:
                    continue
                line_texts = line.split()
                self.__parse_tc_commands(line_texts, line)

    def __parse_tc_commands(self, line_texts, orig_line):
        if len(line_texts) > 1:

            tc_cmd = line_texts[0]
            param_list = self.__get_tc_parameters(orig_line)
            if tc_cmd == TCDefines.TC_SCENARIO_CMD and \
                    self.__tc_scenario_is_not_defined():
                    self.__tc_scenario = TestScenarioHandler(param_list)
                    self.__tc_scenario.add_tc(TestCaseHandler())
            else:
                self.__parse_test_case(tc_cmd, param_list)

        elif len(line_texts) == 1:
            ExitError.exit(AppMsg.TC_COMMAND_LACKS_PARAMETER \
                    .format(line_texts[0]))

    def __get_tc_parameters(self, line):
        line_texts = line.split(TCDefines.TC_PARAM_SEPARATOR)
        return_texts = [ line_texts[0] ]
        for text in line_texts[1:]:
            if text == TCDefines.NEWLINE_MARK:
                continue
            text = text.replace(TCDefines.NEWLINE_MARK, "")
            text = text.replace(TCDefines.STRING_MARK, "")
            text = TCDefines.STRING_MARK + text + TCDefines.STRING_MARK
            return_texts.append(text)
        return return_texts

    def __parse_test_case(self, tc_cmd, line_texts):
        if self.__tc_scenario_is_defined():
            if tc_cmd == TCDefines.TC_CASE_CMD:
                self.__tc_steps = TestCaseHandler(line_texts[1])
                self.__tc_scenario.add_tc(self.__tc_steps)

            elif self.__tc_steps != None:
                self.__parse_tc_steps(tc_cmd, line_texts)
            else:
                print(AppMsg.UNKNOWN_CMD.format(tc_cmd))

    def __parse_tc_steps(self, tc_cmd, line_texts):

        if tc_cmd == TCDefines.TC_CHECK_CMD:
            self.__tc_steps.add_tc_step(CheckCmd(line_texts[1:]))

        elif tc_cmd == TCDefines.TC_CHECK_URL_CMD:
            self.__tc_steps.add_tc_step(CheckURLCmd(line_texts[1]))

        elif tc_cmd == TCDefines.TC_CLICK_CMD:
            self.__tc_steps.add_tc_step(ClickCmd(line_texts[1]))

        elif tc_cmd == TCDefines.TC_ENTER_CMD:
            self.__tc_steps.add_tc_step(EnterCmd(line_texts[1:]))
        else:
            print(AppMsg.UNKNOWN_CMD.format(tc_cmd))

    def __tc_scenario_is_defined(self):
        if self.__tc_scenario == None:
            ExitError.exit(AppMsg.TC_SCENARIO_IS_MISSING)
        return True

    def __tc_scenario_is_not_defined(self):
        if self.__tc_scenario != None:
            ExitError.exit(AppMsg.TC_SHOULD_HAVE_ONLY_ONE_SCENARIO \
                    .format(self.__tc_scenario.name))
        return True
