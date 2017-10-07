import os


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Sony',
        'platformVersion': '5.1.1',
        'autoAcceptAlerts': 'true',
        'noReset': 'true',
        'appPackage': 'com.example.android.contactmanager',
        'appActivity': '.ContactManager',
        #'app': '/Users/venkateshakula/Desktop/ios/sample-code-master/sample-code/apps/ContactManager/ContactManager.apk',

    }
    return desired_caps
