#coding:utf-8
"""
functionモジュールのdecision_making関数をテストする
"""
from functions import decision_making
import class_definition 

robot1 = class_definition.Robot(sensor=4,choice=3,particle_num=100)

#case1:パーティクルの分布・重みは等分
for i in range(100):
    robot1.particles.distribution[i] = i % 5
    robot1.particles.weight[i] = 1.0 / 100.0

robot1.event.sensor=[1,1,1,1]
robot1.event.action = 0
robot1.event.reward = 0.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor=[1,1,1,1]
robot1.event.action = 0
robot1.event.reward = 0.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor=[1,1,1,1]
robot1.event.action = 0
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor=[1,1,1,1]
robot1.event.action = 2
robot1.event.reward = -0.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor=[1,1,1,1]
robot1.event.action = 0
robot1.event.reward = -1.0
robot1.episodes.setEvent(robot1.event)

action = decision_making(robot1.episodes,robot1.particles,robot1.choice_num)
