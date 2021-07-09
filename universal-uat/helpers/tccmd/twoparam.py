from const.tcconst import TCDefines
from helpers.tccmd.firstparam import AttributeParam

class TwoParamCmd(AttributeParam):

    def __init__(self, code, parameters):
        AttributeParam.__init__(self, parameters)
        self.__actual_code = code.format(self.valid_param, parameters[1])

    @property
    def code(self):
        return self.__actual_code

class EnterCmd(TwoParamCmd):

    def __init__(self, parameters):
        TwoParamCmd.__init__(self, TCDefines.TC_ENTER_CODE, parameters)
