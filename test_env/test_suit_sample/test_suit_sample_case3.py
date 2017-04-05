#coding=utf-8

#需要import的一些package
from test_case_base import TestCaseBase
from logging_wrapper import *
from qrd_shared.case import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher

class test_suit_sample_case3(TestCaseBase):
    def test_case_main(self, case_results):
        #launch app which u want
        launcher.launch_from_launcher('gallery')
        postion = get_postion()
        log_test_framework("DUT's location, latitude and longitude", postion)
        #获得设备移动速度，并打印在log中
        speed = get_speed()
        log_test_framework("DUT's moving speed. Unit is meter per second", speed)
        #获取设备当前地区摄氏温度，并打印在log中
        celsius = get_battery_temperate(TEMP_UNIT_C)
        log_test_framework("get Celsius of battery temperate", celsius)
        #获取设备当前地区华氏温度，并打印在log中
        fahrenheit = get_battery_temperate(TEMP_UNIT_F)
        log_test_framework("get Fahrenheit of battery temperate", fahrenheit)
        #获取设备移动方位，以xyz显示，并打印在log中
        orientation = get_orientation()
        log_test_framework("DUT's moving orientation. The return value is x,y,z", orientation)
        #获取设备当前有效RAM大小，并打印在log中
        available_ram = get_available_ram()
        log_test_framework("Available RAM", available_ram)
        #获取设备当前有效ROM大小，并打印在log中
        available_rom = get_available_rom()
        log_test_framework("Available ROM", available_rom)
        #获取设备当前wifi信号好坏，有无信号，差，中等，好，非常好，并打印在log中
        wifi_rssi = get_wifi_rssi()
        log_test_framework("Wifi RSSI level. The return value can be: none or unknown, poor, moderate, good, great", wifi_rssi)
        #获取设备当前蓝牙状态（开/关），并打印在log中
        if is_bluetooth_enabled():
            log_test_framework("check whether bluetooth is enabled", "The return value is true")
        else:
            log_test_framework("check whether bluetooth is enabled", "The return value is False")
        #获取设备当前wifi状态（开/关），并打印在log中
        if is_wifi_enabled():
            log_test_framework("check whether wifi is enabled", "The return value is true")
        else:
            log_test_framework("check whether wifi is enabled", "The return value is False")
        #获取设备当前sim1卡信号好坏，有无信号，差，中等，好，非常好，并打印在log中
        sim_rssi = get_sim_card_rssi(SLOT_ONE)
        log_test_framework("sim card RSSI level. The return value can be: none or unknown, poor, moderate, good, great", sim_rssi)
        #获取设备当前sim卡2信号好坏，有无信号，差，中等，好，非常好，并打印在log中
        sim_status = get_sim_card_state(SLOT_TWO)
        log_test_framework("status of the device SIM card. The return value can be: no available sim card, ready, deactivated, unknown or locked or error", sim_status)
        qsst_log_case_status(STATUS_SUCCESS, 'Get environment context info', SEVERITY_HIGH)
