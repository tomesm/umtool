import sys

if sys.platform.startswith('darwin'):
    # OSX support
    print("Platform supported")
elif sys.platform.startswith('linux'):
    print("Platform not supported")



