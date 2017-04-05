#coding=utf-8
'''
   define the google pinyin key map with 800*480 resolution DUT.

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
key_map['q'] = (20,500)
key_map['w'] = (70,500)
key_map['e'] = (120,500)
key_map['r'] = (170,500)
key_map['t'] = (220,500)
key_map['y'] = (270,500)
key_map['u'] = (320,500)
key_map['i'] = (370,500)
key_map['o'] = (410,500)
key_map['p'] = (460,500)

key_map['a'] = (40,590)
key_map['s'] = (90,590)
key_map['d'] = (140,590)
key_map['f'] = (190,590)
key_map['g'] = (240,590)
key_map['h'] = (290,590)
key_map['j'] = (340,590)
key_map['k'] = (390,590)
key_map['l'] = (440,590)

#caps Lock in English , comma(,) in Chinese  alt in sign
key_map['caps'] = (40,670)
key_map['z'] = (90,670)
key_map['x'] = (140,670)
key_map['c'] = (190,670)
key_map['v'] = (240,670)
key_map['b'] = (290,670)
key_map['n'] = (340,670)
key_map['m'] = (390,670)
#del key
key_map['del'] = (450,670)

#Switch key in Chinese and English
key_map['ch_en'] = (40,750)
#switch key in character and number
key_map['num_sign'] = (130,750)
#blank space
key_map[' '] = (240,750)
#full stop or apostrophe
key_map['.'] = (350,750)
#next or complete
key_map['next'] = (440,750)

#number and sign key
#key:1 or ~
key_map['1'] = (20,500)
#key:2 or ±
key_map['2'] = (70,500)
#key:3 or ×
key_map['3'] = (120,500)
#key:4 or ÷
key_map['4'] = (170,500)
#key:5 or •
key_map['5'] = (220,500)
#key:6 or °
key_map['6'] = (270,500)
#key:7 or <
key_map['7'] = (320,500)
#key:8 or >
key_map['8'] = (370,500)
#key:9 or {
key_map['9'] = (410,500)
#key:0 or }
key_map['0'] = (460,500)

#key:@ or ©
key_map['sign_1'] = (20,590)
#key:# or £
key_map['sign_2'] = (70,590)
#key:$ or €
key_map['sign_3'] = (120,590)
#key:% or ^
key_map['sign_4'] = (170,590)
#key:" or ®
key_map['sign_5'] = (220,590)
#key:* or °F
key_map['sign_6'] = (270,590)
#key:- or _
key_map['sign_7'] = (320,590)
#key:/ or =
key_map['sign_8'] = (370,590)
#key:( or [
key_map['sign_9'] = (410,590)
#key:) or ]
key_map['sign_10'] = (460,500)
#key:! or ™
key_map['sign_11'] = (90,670)
#key:" or ‘
key_map['sign_12'] = (140,670)
#key:' or ’
key_map['sign_13'] = (190,670)
#key:: or +
key_map['sign_14'] = (240,670)
#key:; or |
key_map['sign_15'] = (290,670)
#key:, or \
key_map['sign_16'] = (340,670)
#key:? or √
key_map['sign_17'] = (390,670)

#number keyboard
#key:1 or (
key_map['num_1'] = (50,500)
#key:2 or /
key_map['num_2'] = (170,500)
#key:3 or )
key_map['num_3'] = (300,500)
#key:-
key_map['num_dash'] = (420,500)

#key:4 or N
key_map['num_4'] = (50,580)
#key:5 or 暂停
key_map['num_5'] = (170,580)
#key:6 or ,
key_map['num_6'] = (300,580)
#key:.
key_map['num_full_stop'] = (420,580)

#key:7 or *
key_map['num_7'] = (50,670)
#key:8 or 等待
key_map['num_8'] = (170,670)
#key:9 or #
key_map['num_9'] = (300,670)
#key:del
key_map['num_del'] = (420,670)

#key:123 or *#(  switch key
key_map['num_switch'] = (50,760)
#key:0 or +
key_map['num_0'] = (170,760)
#key: ˽
key_map['num_bracket'] = (300,760)
#key:next
key_map['num_next'] = (420,760)