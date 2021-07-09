import os

from const.appconst import AppDefines
from utils.configfile import UATConfig
from utils.codecept import CodeCept
from helpers.clioptions import CLIOptions
from helpers.tccreate import GenerateTestCase

class RunApp(object):

    def __init__(self):
        self.__cli_args = CLIOptions()
        self.__uat_cfg = UATConfig()

    def run(self):
        cli_cfg = self.__cli_args.get_cli_args()

        create_tc_option = getattr(cli_cfg, AppDefines.GENERATE_CLI[2:])
        run_test_option = getattr(cli_cfg, AppDefines.RUN_TEST_CLI[2:])

        if create_tc_option != AppDefines.NOT_SPECIFIED:
            GenerateTestCase(create_tc_option).run()

        elif run_test_option != AppDefines.NOT_SPECIFIED:
            CodeCept(UATConfig(), run_test_option).run()

        else:
            self.__cli_args.print_help()

