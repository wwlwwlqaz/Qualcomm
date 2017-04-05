#coding=utf-8
'''
   decompose the input content

   1.Developer can directly use the map as ime's input, Such as:

     from qrd_shared.case import *
     from qrd_shared.ime.methods.predefine_input_seq import input_seq_map

     email.access_browser(ime.IME_input_english(1,input_seq_map["address_url"]), ime.IME_input(1,input_seq_map["百度"]),'c'), 20):

   2.Developer can add some new map item here.
     When add Chinese, please make sure the new Chinese value is the first option in ime. It only select the first value when exists multiple options. 


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see:
   @note:
   @attention:
   @bug:
   @warning:



'''

#    decompose the input content
############################################

input_seq_map = {}
# www.baidu.cww
input_seq_map["address_url"] = "www.baidu.com"
input_seq_map["百度"] = "baidu"
