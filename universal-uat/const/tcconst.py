class TCDefines:

    MINIMUM_ATTRIBUTE_PARAM     = 7
                                # means ", [, ' ', *, ' ', ], " and * is any character.

    PERIOD                      = "."
    READ_ACCESS                 = "r"
    WRITE_ACCESS                = "w"
    COMMENT_MARK                = "#"
    STRING_MARK                 = '"'
    NEWLINE_MARK                = "\n"
    OPEN_ATTRIBUTE_MARK         = "["
    CLOSE_ATTRIBUTE_MARK        = "]"
    UTF8_ENCODING               = "utf8"

    TC_PARAM_SEPARATOR          = ' "'
    TC_SCENARIO_CMD             = 'TestScenario'
    TC_CASE_CMD                 = 'TestCase'
    TC_CHECK_CMD                = 'Check'
    TC_CHECK_URL_CMD            = 'CheckURL'
    TC_CLICK_CMD                = 'Click'
    TC_ENTER_CMD                = 'Enter'

    TC_SCENARIO_KEY             = "SCENARIO"
    TC_KEY                      = "TESTCASE{}"

    TEST_CASE_KEY               = "FUNCTION"
    TEST_STEPS_KEY              = "STEPS"
    TC_FIRST_NAME               = "_before"

    TC_LIST_TEXT                = "%TC_LIST%"
    TC_STEPS_TEXT               = "%TC_STEPS%"

    TC_CHECK_CODE               = "        $I->see({});\n";
    TC_CHECK_URL_CODE           = "        $I->amOnPage({});\n";
    TC_CLICK_CODE               = "        $I->click({});\n";
    TC_ENTER_CODE               = "        $I->fillField({}, {});\n";

    TC_SCENARIO_CLASS = \
'''
<?php
class {}Cest'''

    TC_SCENARIO_BLOCK = \
'''
{
%TC_LIST%
}
'''

    TEST_CASE_FUNCTION = \
'''
    public function {}(AcceptanceTester $I)'''

    TEST_CASE_BLOCK = \
'''
    {
%TC_STEPS%
    }
'''
