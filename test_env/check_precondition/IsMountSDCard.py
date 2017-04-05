#coding=utf-8
'''
Created on Aug 20, 2013

@author: shijunz
'''
from case_utility import is_external_storage_enable

def verify():
    '''
    is_external_storage_enable()
    '''
    if is_external_storage_enable():
        return 'ok'
    return 'NO SD Card found'

