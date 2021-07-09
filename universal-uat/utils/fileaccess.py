import os

from const.appconst import AppDefines
from const.tcconst import TCDefines
from const.textconst import AppMsg
from utils.apperror import ExitError

class CreateFile(object):

    def __init__(self, file_path, file_name, tc_file=True):
        self.__file_path = file_path
        if os.path.exists(self.__file_path) == False:
            ExitError.exit( \
                AppMsg.TC_WORKING_FOLDER_NOT_FOUND.format(self.__file_path))
        if tc_file:
            create_file = AppDefines.CODECEPT_FILE_EXT.format(file_name)
        else:
            create_file = file_name
        self.__target_file = os.path.join(file_path,create_file)

    def write(self, contents_to_write):
        contents = contents_to_write.splitlines()
        with open(self.__target_file
                 ,TCDefines.WRITE_ACCESS
                 ,encoding = TCDefines.UTF8_ENCODING) as tc_file:
            for line in contents:
                tc_file.write(line + AppMsg.NEW_LINE_SEPARATOR)
            tc_file.write(AppMsg.NEW_LINE_SEPARATOR)

