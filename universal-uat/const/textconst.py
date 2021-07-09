class AppMsg:

    NEW_LINE_SEPARATOR          = "\n"
    UAT_DESCRIPTION             = "The SPROBE UAT CLI command parser"
    UNKNOWN_CMD                 = "Skipping undefined command - {}"

    CODECEPTION_IS_NOT_INSTALLED = \
'''
CodeCeption executable is not found!
Please install CodeCeption first.
'''

    GENERATE_CLI_HELP = \
'''generate the test cases in PHP file.
E.g.

 --create_tc CWD *
   - generate all the test cases in the current folder.

 --create_tc 'c:\\tests' 'sample.tc'
   - generate the test case only for sample.tc file.

'''

    RUN_TEST_CLI_HELP = \
'''run the test cases.
E.g.

 --run_test 'c:\\tests'
   - performs all the test cases in the specified folder.

 --run_test CWD 'LoginTC:loginSucess'
   - performs the specific test case in the current folder.

'''

    TC_COMMAND_LACKS_PARAMETER = \
'''
The Test Case command [{}] has missing parameter(s)!
Kindly fix the test case.
'''

    TC_SCENARIO_IS_MISSING = \
'''
The Test Scenario is missing.
Kindly fix the test case.
'''

    TC_SHOULD_HAVE_ONLY_ONE_SCENARIO = \
'''
The Test Case Scenario [{}] is defined.
Kindly fix the test case.
'''

    UAT_CONFIG_NOT_FOUND = \
'''
The uat_config file is not found in the working directory!
Working Directory: {}
Kindly create the required configuration file.
'''

    TC_WORKING_FOLDER_NOT_FOUND = \
'''
The specified working folder does not exists!
Working Folder: {}
Please specify a valid directory path.
'''

    TC_WORKING_FILES_NOT_FOUND = \
'''
The specified working folder does not contain any test case(s)!
Test Case: {}
Please specify a valid test case file.
'''

    CODECEPTION_STANDARD_CONFIG = \
'''
suites:
    acceptance:
        actor: AcceptanceTester
        path: .
        modules:
            enabled:
                - WebDriver:
                    url: {}
                    browser: chrome
                    window_size: {}
              
        step_decorators:
            - Codeception\Step\ConditionalAssertion
            - Codeception\Step\TryTo
            - Codeception\Step\Retry
                
extensions:
    enabled:
      - Codeception\Extension\RunFailed
      - Codeception\Extension\Recorder:
          delete_successful: false

params: 
    - env

gherkin: []    

paths:
    tests: tests
    output: tests/_output
    data: tests/_data
    support: tests/_support
    envs: tests/_envs

settings:
    shuffle: false
    lint: true
'''
