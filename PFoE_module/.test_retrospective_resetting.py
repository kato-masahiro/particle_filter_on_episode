#coding:utf-8
"""
functionモジュールのretrospective_resetting関数をテストする
"""
import unittest

from functions import retrospective_resetting
import class_definition 

robot1 = class_definition.Robot(sensor=4,choice=3,particle_num=12,step=2,threshold=0.5,reduction=0.5)

robot1.particles.alpha = 0.1

robot1.particles.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot1.particles.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

robot1.event.sensor = [1,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,0,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

sen_val = [1,1,1,1]

robot1.particles = retrospective_resetting(robot1.particles,robot1.episodes,robot1.resetting_threshold,robot1.resetting_step,sen_val)

print "distribution:",robot1.particles.distribution
print "weight:",robot1.particles.weight
print "sum_of_weight:",sum(robot1.particles.weight)
