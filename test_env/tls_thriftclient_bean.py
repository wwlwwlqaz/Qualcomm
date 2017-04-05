'''
    TLS thrift client bean

    This is the class to storage thrift client.

   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:

'''

class ThriftClient:

    def __init__(self):
        self.transport_qsst = None
        self.client_qsst = None
        self.protocol_qsst = None
        self.transport_uiautomator = None
        self.client_uiautomator = None
        self.protocol_uiautomator = None
        self.transport_mytrackservice = None
        self.client_mytrackservice = None
        self.protocol_mytrackservice = None