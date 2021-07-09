from const.tcconst import TCDefines

class AttributeParam(object):

    def __init__(self, parameter):
        if type(parameter) == list:
            self.__valid_param = \
                self.__detect_attribute_param(parameter[0])
        else:
            self.__valid_param = \
                self.__detect_attribute_param(parameter)

    @property
    def valid_param(self):
        return self.__valid_param

    def __detect_attribute_param(self, parameter):
        last_char = len(parameter)
        if len(parameter) > TCDefines.MINIMUM_ATTRIBUTE_PARAM and \
           parameter[1] == TCDefines.OPEN_ATTRIBUTE_MARK and \
           parameter[last_char-2] == TCDefines.CLOSE_ATTRIBUTE_MARK:
            return parameter.strip(TCDefines.STRING_MARK)
        else:
            return parameter
