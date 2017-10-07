import os


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone 7',
        'automationName': 'XCUITest',
        'platformVersion': '10.3',
        'autoAcceptAlerts': 'true',
        'noReset': 'true',
        #'app': '/Users/venkateshakula/Desktop/ios/sample-code-master/sample-code/apps/TestApp/build/release-iphonesimulator/TestApp.app',

    }
    return desired_caps
