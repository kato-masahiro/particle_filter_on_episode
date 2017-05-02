#coding:utf-8
"""
functionモジュールのset_event関数をテストする
"""
from functions import set_event
import pfoe

robot1 = pfoe.Robot(sensor=4,choice=3,limit = 4) 

robot1.sensor = [0,0,0,0]
robot1.action = 1
reward_val = 1.0
robot1.episodes,robot1.particles = set_event(robot1.sensor,robot1.action,reward_val,robot1.event,robot1.episodes,robot1.particles)

robot1.sensor = [0,0,0,1]
robot1.action = 1
reward_val = -1.0
robot1.episodes,robot1.particles = set_event(robot1.sensor,robot1.action,reward_val,robot1.event,robot1.episodes,robot1.particles)

robot1.sensor = [0,0,1,1]
robot1.action = 1
reward_val = -1.0
robot1.episodes,robot1.particles = set_event(robot1.sensor,robot1.action,reward_val,robot1.event,robot1.episodes,robot1.particles)

robot1.sensor = [0,1,1,1]
robot1.action = 1
reward_val = 1.0
robot1.episodes,robot1.particles = set_event(robot1.sensor,robot1.action,reward_val,robot1.event,robot1.episodes,robot1.particles)
for i in range( len(robot1.episodes.events) ):
    print robot1.episodes.events[i].sensor,",", \
          robot1.episodes.events[i].action,",", \
          robot1.episodes.events[i].reward
print "---"

robot1.sensor = [1,1,1,1]
robot1.action = 1
reward_val = 1.0
robot1.episodes,robot1.particles = set_event(robot1.sensor,robot1.action,reward_val,robot1.event,robot1.episodes,robot1.particles)
for i in range( len(robot1.episodes.events) ):
    print robot1.episodes.events[i].sensor,",", \
          robot1.episodes.events[i].action,",", \
          robot1.episodes.events[i].reward
print "---"
