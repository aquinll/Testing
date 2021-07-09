from const.tcconst import TCDefines
from helpers.tccmd.firstparam import AttributeParam

class MultiParamCmd(object):

    def __init__(self, code, parameters):
        self.__actual_code = []
        for item in parameters:
            self.__actual_code.append( \
                code.format(AttributeParam(item).valid_param))

    @property
    def code(self):
        return self.__actual_code

class CheckCmd(MultiParamCmd):

    def __init__(self, parameters):
        MultiParamCmd.__init__(self, TCDefines.TC_CHECK_CODE, parameters)
