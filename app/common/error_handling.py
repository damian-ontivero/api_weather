'''
Error handler
'''

class AppErrorBaseClass(Exception):
    pass

class ObjectNotFound(AppErrorBaseClass):
    pass