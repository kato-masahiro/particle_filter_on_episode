#coding:utf-8
"""
functionモジュールのretrospective_resetting関数をテストする

retrospective_resetting(particles,episodes,resetting_threshold,resetting_step,sensor_val):
    処理：
        Particles.alphaがRobot.resetting_thresholdより小さく、
        かつ
        Robot.Episode.sets[] の数が充分存在している場合
        回想に基づくリセッティングを行う
    引数: particlesクラス,episodesクラス,resetting_threshold,resetting_step,sensor_val
    引数: resetting_threshold
    戻り値:
"""
from functions import retrospective_resetting
import pfoe

### ケース1 ###
robot1 = pfoe.Robot(sensor=4,choice=3,particle_num=12,step=3,threshold=0.5,reduction=0.5)
robot1.particles.alpha = 0.1
robot1.particles.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot1.particles.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

robot1.event.sensor = [1,1,1,1]
robot1.event.action = 1
robot1.event.reward = -1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,1,1]
robot1.event.action = -1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,0,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

sen_val = [1,1,1,1]

robot1.particles = retrospective_resetting(robot1.particles,robot1.episodes,robot1.resetting_threshold,robot1.resetting_step,sen_val,robot1.reduction_rate)

print "distribution:",robot1.particles.distribution
print "weight:",robot1.particles.weight
print "sum_of_weight:",sum(robot1.particles.weight)

### ケース2 ###
robot2 = pfoe.Robot(sensor=4,choice=3,particle_num=12,step=3,threshold=0.5,reduction=0.5)
robot2.particles.alpha = 0.1
robot2.particles.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot2.particles.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

robot2.particles = retrospective_resetting(robot2.particles,robot2.episodes,robot2.resetting_threshold,robot2.resetting_step,sen_val,robot1.reduction_rate)

print "distribution:",robot2.particles.distribution
print "weight:",robot2.particles.weight
print "sum_of_weight:",sum(robot2.particles.weight)
