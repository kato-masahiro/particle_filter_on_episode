#coding:utf-8
"""
*****************************************************
* functionモジュールのsensor_update関数をテストする *
*****************************************************

sensor_update(sensor_val,episodes,particles):

    処理:全てのパーティクルについて、尤度に基づいて重みを更新する
         重みの平均値でalphaを更新する
         alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
    引数: センサ値、エピソードクラス、パーティクルクラス
    戻り値: particlesクラス
"""
from functions import sensor_update
import pfoe

### パターン1 尤度が重みに対して適切なものになっているかどうかチェック###
robot1 = pfoe.Robot(sensor=4,choice=3,particle_num=12) 
robot1.particles.distribution=[0,1,2,0,1,2,0,1,2,0,1,2]
robot1.particles.weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

robot1.event.sensor = [1,1,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,1,1]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

robot1.event.sensor = [0,0,0,0]
robot1.event.action = 1
robot1.event.reward = 1.0
robot1.episodes.setEvent(robot1.event)

### パターン2 エピソード数が0の時の挙動をチェック ###
robot2 = pfoe.Robot(sensor=4,choice=3,particle_num=20)

### パターン3 エピソードの重みがすべて0の時のチェック ### 
robot3 = pfoe.Robot(sensor=4,choice=3,particle_num=10)
robot3.particles.distribution=[0,1,2,0,1,2,0,1,2,0]
robot3.particles.weight = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
robot3.episodes = robot1.episodes


sen_val = [0,0,0,0]


robot1.particles = sensor_update(sen_val,robot1.episodes,robot1.particles)
print "weight:",robot1.particles.weight
print "alpha:",robot1.particles.alpha
print "---"

robot2.particles = sensor_update(sen_val,robot2.episodes,robot2.particles)
print "weight:",robot2.particles.weight
print "alpha:",robot2.particles.alpha
print "---"

robot3.particles = sensor_update(sen_val,robot3.episodes,robot3.particles)
print "weight:",robot3.particles.weight
print "alpha:",robot3.particles.alpha
