#coding:utf-8
import sys

"""
functionモジュールのsensor_update関数をテストする
"""
sys.path.append('../PFoE/functions')
sys.path.append('../PFoE/class_definition')

from functions import sensor_update
import class_definition 

mouse1=class_definition.Robot(sensor=4,choice=3)
