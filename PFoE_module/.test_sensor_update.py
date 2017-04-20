#coding:utf-8
"""
functionモジュールのsensor_update関数をテストする
"""
import unittest

from functions import sensor_update
import class_definition 

robot1 = class_definition.Robot(sensor=4,choice=3,particle=12) #尤度が重みにちゃんと掛けられているかチェック
robot2 = class_definition.Robot(sensor=4,choice=3,particle=20) #エピソード数が0の場合のチェック
robot3 = class_definition.Robot(sensor=4,choice=3,particle=10) #エピソードの重みがすべて0の場合のチェック

robot1.particle.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot1.particle.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

robot3.particle.distribution=[0,1,2,0,1,2,0,1,2,0]
robot3.particle.weight = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

robot1.event.sensor = [1,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)

robot1.event.sensor = [0,0,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)

robot1.event.sensor = [0,0,0,0]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)

robot3.episode = robot1.episode

sen_val = [0,0,0,0]

robot1.particle = sensor_update(sen_val,robot1.episode,robot1.particle)
print "weight:",robot1.particle.weight
print "alpha:",robot1.particle.alpha
print "---"

robot2.particle = sensor_update(sen_val,robot2.episode,robot2.particle)
print "weight:",robot2.particle.weight
print "alpha:",robot2.particle.alpha
print "---"

robot3.particle = sensor_update(sen_val,robot3.episode,robot3.particle)
print "weight:",robot3.particle.weight
print "alpha:",robot3.particle.alpha
