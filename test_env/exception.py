
''' qsst base exception '''
import logging_wrapper
class QsstException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg
    def __str__(self):
        return ('%s:%s'  % (self.__class__.__name__.upper(),self.msg))

class SocketException(QsstException):
    def __init__(self, msg):
        QsstException.__init__(self, msg)

class AssertFailedException(QsstException):
    def __init__(self, msg):
        QsstException.__init__(self, msg)

class AttributeException(QsstException):
    def __init__(self, msg):
        QsstException.__init__(self, msg)