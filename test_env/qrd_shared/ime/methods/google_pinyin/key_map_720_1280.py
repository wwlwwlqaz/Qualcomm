#coding=utf-8
'''
   define the google pinyin key map with 1280*720 resolution DUT.

   The map value is x coordinate and y coordinate of the key.

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
#character keyboard
key_map = {}
key_map['q'] = (36,800)
key_map['w'] = (108,800)
key_map['e'] = (180,800)
key_map['r'] = (252,800)
key_map['t'] = (324,800)
key_map['y'] = (396,800)
key_map['u'] = (468,800)
key_map['i'] = (540,800)
key_map['o'] = (612,800)
key_map['p'] = (684,800)

key_map['a'] = (72,940)
key_map['s'] = (144,940)
key_map['d'] = (216,940)
key_map['f'] = (288,940)
key_map['g'] = (360,940)
key_map['h'] = (432,940)
key_map['j'] = (504,940)
key_map['k'] = (576,940)
key_map['l'] = (648,940)

#caps Lock in English , comma(,) in Chinese  alt in sign
key_map['caps'] = (72,1080)
key_map['z'] = (144,1080)
key_map['x'] = (216,1080)
key_map['c'] = (288,1080)
key_map['v'] = (360,1080)
key_map['b'] = (432,1080)
key_map['n'] = (504,1080)
key_map['m'] = (580,1080)
#del key
key_map['del'] = (648,1080)

#Switch key in Chinese and English
key_map['ch_en'] = (72,1215)
#switch key in character and number
key_map['num_sign'] = (198,1215)
#blank space
key_map[' '] = (360,1215)
#full stop or apostrophe
key_map['.'] = (522,1215)
#next or complete
key_map['next'] = (648,1215)

#number and sign key
#key:1 or ~
key_map['1'] = (36,800)
#key:2 or ±
key_map['2'] = (108,800)
#key:3 or ×
key_map['3'] = (180,800)
#key:4 or ÷
key_map['4'] = (252,800)
#key:5 or •
key_map['5'] = (324,800)
#key:6 or °
key_map['6'] = (396,800)
#key:7 or <
key_map['7'] = (468,800)
#key:8 or >
key_map['8'] = (540,800)
#key:9 or {
key_map['9'] = (612,800)
#key:0 or }
key_map['0'] = (684,800)

#key:@ or ©
key_map['sign_1'] = (36,950)
#key:# or £
key_map['sign_2'] = (108,950)
#key:$ or €
key_map['sign_3'] = (180,950)
#key:% or ^
key_map['sign_4'] = (252,950)
#key:" or ®
key_map['sign_5'] = (324,950)
#key:* or °F
key_map['sign_6'] = (396,950)
#key:- or _
key_map['sign_7'] = (468,950)
#key:/ or =
key_map['sign_8'] = (540,950)
#key:( or [
key_map['sign_9'] = (612,950)
#key:) or ]
key_map['sign_10'] = (684,950)
#key:! or ™
key_map['sign_11'] = (144,1080)
#key:" or ‘
key_map['sign_12'] = (216,1080)
#key:' or ’
key_map['sign_13'] = (288,1080)
#key:: or +
key_map['sign_14'] = (360,1080)
#key:; or |
key_map['sign_15'] = (432,1080)
#key:, or \
key_map['sign_16'] = (504,1080)
#key:? or √
key_map['sign_17'] = (648,1080)

#number keyboard
#key:1 or (
key_map['num_1'] = (90,810)
#key:2 or /
key_map['num_2'] = (270,810)
#key:3 or )
key_map['num_3'] = (450,810)
#key:-
key_map['num_dash'] = (630,810)

#key:4 or N
key_map['num_4'] = (90,945)
#key:5 or 暂停
key_map['num_5'] = (270,945)
#key:6 or ,
key_map['num_6'] = (450,945)
#key:.
key_map['num_full_stop'] = (630,945)

#key:7 or *
key_map['num_7'] = (90,1080)
#key:8 or 等待
key_map['num_8'] = (270,1080)
#key:9 or #
key_map['num_9'] = (450,1080)
#key:del
key_map['num_del'] = (630,1080)

#key:123 or *#(  switch key
key_map['num_switch'] = (90,1215)
#key:0 or +
key_map['num_0'] = (270,1215)
#key: ˽
key_map['num_bracket'] = (450,1215)
#key:next
key_map['num_next'] = (630,1215)
