import sys
import argparse

from const.appconst import AppDefines
from const.textconst import AppMsg

class CLIOptions(object):

    def __init__(self):
        self.__construct_help()

    def __construct_help(self):
        self.__arg_parser = argparse.ArgumentParser(
             description = AppMsg.UAT_DESCRIPTION
            ,formatter_class = argparse.RawTextHelpFormatter)
        self.__arg_parser.add_argument(AppDefines.GENERATE_CLI
                , nargs=AppDefines.ALL_ARGS
                , metavar=( AppDefines.GENERATE_CLI_ARG_1
                , AppDefines.GENERATE_CLI_ARG_2 )
                , type=str
                , default=AppDefines.NOT_SPECIFIED
                , help=AppMsg.GENERATE_CLI_HELP)
        self.__arg_parser.add_argument(AppDefines.RUN_TEST_CLI
                , nargs=AppDefines.ALL_ARGS
                , metavar=( AppDefines.RUN_TEST_CLI_ARG_1 )
                , type=str
                , default=AppDefines.NOT_SPECIFIED
                , help=AppMsg.RUN_TEST_CLI_HELP)

    def __check_args(self):
        if (len(sys.argv) - 1) < 1:
            self.print_help()
            exit(1)

    def get_cli_args(self):
        self.__check_args()
        return self.__arg_parser.parse_args()

    def print_help(self):
        self.__arg_parser.print_help()
