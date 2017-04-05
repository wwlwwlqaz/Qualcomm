#coding=utf-8
'''
   define the google pinyin key map with 960*540 resolution DUT.

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
key_map['q'] = (30,610)
key_map['w'] = (80,610)
key_map['e'] = (130,610)
key_map['r'] = (180,610)
key_map['t'] = (240,610)
key_map['y'] = (300,610)
key_map['u'] = (350,610)
key_map['i'] = (410,610)
key_map['o'] = (460,610)
key_map['p'] = (520,610)

key_map['a'] = (50,720)
key_map['s'] = (100,720)
key_map['d'] = (150,720)
key_map['f'] = (210,720)
key_map['g'] = (270,720)
key_map['h'] = (320,720)
key_map['j'] = (380,720)
key_map['k'] = (440,720)
key_map['l'] = (490,720)

#caps Lock in English , comma(,) in Chinese  alt in sign
key_map['caps'] = (40,820)
key_map['z'] = (100,820)
key_map['x'] = (160,820)
key_map['c'] = (220,820)
key_map['v'] = (280,820)
key_map['b'] = (330,820)
key_map['n'] = (380,820)
key_map['m'] = (430,820)
#del key
key_map['del'] = (500,820)

#Switch key in Chinese and English
key_map['ch_en'] = (60,920)
#switch key in character and number
key_map['num_sign'] = (150,920)
#blank space
key_map[' '] = (320,920)
#full stop or apostrophe
key_map['.'] = (390,920)
#next or complete
key_map['next'] = (480,920)

#number and sign key
#key:1 or ~
key_map['1'] = (30,610)
#key:2 or ±
key_map['2'] = (80,610)
#key:3 or ×
key_map['3'] = (130,610)
#key:4 or ÷
key_map['4'] = (180,610)
#key:5 or •
key_map['5'] = (240,610)
#key:6 or °
key_map['6'] = (300,610)
#key:7 or <
key_map['7'] = (350,610)
#key:8 or >
key_map['8'] = (410,610)
#key:9 or {
key_map['9'] = (460,610)
#key:0 or }
key_map['0'] = (520,610)

#key:@ or ©
key_map['sign_1'] = (30,720)
#key:# or £
key_map['sign_2'] = (80,720)
#key:$ or €
key_map['sign_3'] = (130,720)
#key:% or ^
key_map['sign_4'] = (180,720)
#key:" or ®
key_map['sign_5'] = (240,720)
#key:* or °F
key_map['sign_6'] = (300,720)
#key:- or _
key_map['sign_7'] = (350,720)
#key:/ or =
key_map['sign_8'] = (410,720)
#key:( or [
key_map['sign_9'] = (460,720)
#key:) or ]
key_map['sign_10'] = (520,720)
#key:! or ™
key_map['sign_11'] = (110,820)
#key:" or ‘
key_map['sign_12'] = (160,820)
#key:' or ’
key_map['sign_13'] = (210,820)
#key:: or +
key_map['sign_14'] = (270,820)
#key:; or |
key_map['sign_15'] = (320,820)
#key:, or \
key_map['sign_16'] = (380,820)
#key:? or √
key_map['sign_17'] = (430,820)

#number keyboard
#key:1 or (
key_map['num_1'] = (50,610)
#key:2 or /
key_map['num_2'] = (200,610)
#key:3 or )
key_map['num_3'] = (350,610)
#key:-
key_map['num_dash'] = (470,610)

#key:4 or N
key_map['num_4'] = (50,710)
#key:5 or 暂停
key_map['num_5'] = (200,710)
#key:6 or ,
key_map['num_6'] = (350,710)
#key:.
key_map['num_full_stop'] = (470,710)

#key:7 or *
key_map['num_7'] = (50,810)
#key:8 or 等待
key_map['num_8'] = (200,810)
#key:9 or #
key_map['num_9'] = (350,810)
#key:del
key_map['num_del'] = (470,810)

#key:123 or *#(  switch key
key_map['num_switch'] = (50,910)
#key:0 or +
key_map['num_0'] = (200,910)
#key: ˽
key_map['num_bracket'] = (350,910)
#key:next
key_map['num_next'] = (470,910)