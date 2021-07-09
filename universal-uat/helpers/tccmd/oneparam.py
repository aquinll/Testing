from const.tcconst import TCDefines
from helpers.tccmd.firstparam import AttributeParam

class OneParamCmd(AttributeParam):

    def __init__(self, code="", parameter=""):
        AttributeParam.__init__(self, parameter)
        self.__actual_code = code.format(self.valid_param)

    @property
    def code(self):
        return self.__actual_code

class CheckURLCmd(OneParamCmd):

    def __init__(self, parameter):
        OneParamCmd.__init__(self, TCDefines.TC_CHECK_URL_CODE, parameter)

class ClickCmd(OneParamCmd):

    def __init__(self, parameter):
        OneParamCmd.__init__(self, TCDefines.TC_CLICK_CODE, parameter)
