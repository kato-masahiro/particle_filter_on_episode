#coding:utf-8
"""
functionモジュールのsensor_update関数をテストする
"""
import unittest

from functions import sensor_update
import class_definition 

robot1 = class_definition.Robot(sensor=4,choice=3,particle=12)

robot1.particle.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot1.particle.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

print robot1.episode.sets
print "---"

robot1.event.sensor = [1,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)
print robot1.episode.sets[0].sensor
print "---"

robot1.event.sensor = [0,0,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)
print robot1.episode.sets[0].sensor
print robot1.episode.sets[1].sensor
print "---"

robot1.event.sensor = [0,0,0,0]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episode.setEvent(robot1.event)
print robot1.episode.sets[0].sensor
print robot1.episode.sets[1].sensor
print robot1.episode.sets[2].sensor
print "---"

sen_val = [0,0,0,0]
robot1.particle = sensor_update(sen_val,robot1.episode,robot1.particle)
print robot1.particle.weight
