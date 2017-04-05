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

# raw's gap
gap_y = 164
# key q line' gap
gap = 105
# key q's x coordinate
q_x = 55
# key q's y coordinate
q_y = 1190
key_map['q'] = (q_x,q_y)
key_map['w'] = (q_x + gap,q_y)
key_map['e'] = (q_x + gap*2,q_y)
key_map['r'] = (q_x + gap*3,q_y)
key_map['t'] = (q_x + gap*4,q_y)
key_map['y'] = (q_x + gap*5,q_y)
key_map['u'] = (q_x + gap*6,q_y)
key_map['i'] = (q_x + gap*7,q_y)
key_map['o'] = (q_x + gap*8,q_y)
key_map['p'] = (q_x + gap*9,q_y)

# key a line' gap
gap_a = 108
# key a's x coordinate
a_x = 108
key_map['a'] = (a_x,q_y + gap_y)
key_map['s'] = (a_x + gap_a,q_y + gap_y)
key_map['d'] = (a_x + gap_a*2,q_y + gap_y)
key_map['f'] = (a_x + gap_a*3,q_y + gap_y)
key_map['g'] = (a_x + gap_a*4,q_y + gap_y)
key_map['h'] = (a_x + gap_a*5,q_y + gap_y)
key_map['j'] = (a_x + gap_a*6,q_y + gap_y)
key_map['k'] = (a_x + gap_a*7,q_y + gap_y)
key_map['l'] = (a_x + gap_a*8,q_y + gap_y)

#caps Lock in English , comma(,) in Chinese  alt in sign
key_map['caps'] = (key_map['q'][0],q_y + gap_y * 2)
key_map['z'] = (key_map['s'][0],q_y + gap_y * 2)
key_map['x'] = (key_map['d'][0],q_y + gap_y * 2)
key_map['c'] = (key_map['f'][0],q_y + gap_y * 2)
key_map['v'] = (key_map['g'][0],q_y + gap_y * 2)
key_map['b'] = (key_map['h'][0],q_y + gap_y * 2)
key_map['n'] = (key_map['j'][0],q_y + gap_y * 2)
key_map['m'] = (key_map['k'][0],q_y + gap_y * 2)
#del key
key_map['del'] = (key_map['p'][0],q_y + gap_y * 2)


#switch key in character and number
key_map['num_sign'] = (key_map['q'][0],q_y + gap_y * 3)
#
key_map[r'/'] = (key_map['z'][0],q_y + gap_y * 3)
#blank space
key_map[' '] = (key_map['v'][0],q_y + gap_y * 3)
#full stop or apostrophe
key_map['.'] = (key_map['m'][0],q_y + gap_y * 3)
#next or complete
key_map['next'] = (key_map['del'][0],q_y + gap_y * 3)

#number and sign key
#key:1 or ~
key_map['1'] = key_map['q']
#key:2 or ±
key_map['2'] = key_map['w']
#key:3 or ×
key_map['3'] = key_map['e']
#key:4 or ÷
key_map['4'] = key_map['r']
#key:5 or •
key_map['5'] = key_map['t']
#key:6 or °
key_map['6'] = key_map['y']
#key:7 or <
key_map['7'] = key_map['u']
#key:8 or >
key_map['8'] = key_map['i']
#key:9 or {
key_map['9'] = key_map['o']
#key:0 or }
key_map['0'] = key_map['p']

#key:@ or ©
key_map['sign_1'] = (key_map['a'][0],q_y + gap_y)
#key:# or £
key_map['sign_2'] = (key_map['s'][0],q_y + gap_y)
#key:$ or €
key_map['sign_3'] = (key_map['d'][0],q_y + gap_y)
#key:% or ^
key_map['sign_4'] = (key_map['f'][0],q_y + gap_y)
#add by huitingn: key:&
key_map['sign_18'] = (key_map['g'][0],q_y + gap_y)
#modified by huitingn: key:-     key:- or _
key_map['sign_7'] = (key_map['h'][0],q_y + gap_y)
#modified by huitingn: key:+     key:: or +
key_map['sign_14'] = (key_map['j'][0],q_y + gap_y)
#modified by huitingn: key:(     key:( or [
key_map['sign_9'] = (key_map['k'][0],q_y + gap_y)
#modified by huitingn: key:)     key:) or ]
key_map['sign_10'] = (key_map['l'][0],q_y + gap_y)

#key:* or °F
key_map['sign_6'] = (key_map['z'][0],q_y + gap_y*2)
#key:" or ®
key_map['sign_5'] = (key_map['x'][0],q_y + gap_y*2)
#key:" or ‘
key_map['sign_12'] = (key_map['x'][0],q_y + gap_y*2)
#key:' or ’
key_map['sign_13'] = (key_map['c'][0],q_y + gap_y*2)

#key:/ or =
key_map['sign_8'] = (key_map['k'][0],q_y + gap_y)

#key:! or ™
key_map['sign_11'] = (key_map['z'][0],q_y + gap_y*2)

#key:; or |
key_map['sign_15'] = (key_map['b'][0],q_y + gap_y*2)
#key:, or \
key_map['sign_16'] = (key_map['n'][0],q_y + gap_y*2)
#key:? or √
key_map['sign_17'] = (key_map['m'][0],q_y + gap_y*2)

'''number keyboard'''
# key 1's x coordinate
key_1_x = 75
# key 1's y coordinate
key_1_y = 617

# number keyboard's x-axis gap
gap_x_axis = 150

#key:1 or (
key_map['num_1'] = (key_1_x,key_1_y)
#key:2 or /
key_map['num_2'] = (key_1_x + gap_x_axis,key_1_y)
#key:3 or )
key_map['num_3'] = (key_1_x + gap_x_axis*2,key_1_y)
#key:-
key_map['num_dash'] = (key_1_x + gap_x_axis*3,key_1_y)

#key:4 or N
key_map['num_4'] = (key_map['num_1'][0],key_1_y + gap_y)
#key:5 or 暂停
key_map['num_5'] = (key_map['num_2'][0],key_1_y + gap_y)
#key:6 or ,
key_map['num_6'] = (key_map['num_3'][0],key_1_y + gap_y)
#key:.
key_map['num_full_stop'] = (key_map['num_dash'][0],key_1_y + gap_y)

#key:7 or *
key_map['num_7'] = (key_map['num_1'][0],key_1_y + gap_y*2)
#key:8 or 等待
key_map['num_8'] = (key_map['num_2'][0],key_1_y + gap_y*2)
#key:9 or #
key_map['num_9'] = (key_map['num_3'][0],key_1_y + gap_y*2)
#key:del
key_map['num_del'] = (key_map['num_dash'][0],key_1_y + gap_y*2)

#key:123 or *#(  switch key
key_map['num_switch'] = (key_map['num_1'][0],key_1_y + gap_y*3)
#key:0 or +
key_map['num_0'] = (key_map['num_2'][0],key_1_y + gap_y*3)
#key: ˽
key_map['num_bracket'] = (key_map['num_3'][0],key_1_y + gap_y*3)
#key:next
key_map['num_next'] = (key_map['num_dash'][0],key_1_y + gap_y*3)
