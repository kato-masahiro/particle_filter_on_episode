#!/bin/env python
#coding:utf-8

"""
モジュール PFoE.pyを用いた実装の具体例
"""

import PFoE 

robot = PFoE.Robot(sensor=3,choice=3,threshold=0.5,reduction=0.5)

while 1:
    print "ロボットのセンサ値:",
    robot.sensor = input()
    robot.update()

    robot.see_distribution()

    action = robot.decision_making()

    #actionに従いロボットを行動させる
    print "\nロボットの行動は:",action
    print "報酬:",
    reward = input()

    robot.add_event(robot.sensor, action,reward)
    robot.sliding()
