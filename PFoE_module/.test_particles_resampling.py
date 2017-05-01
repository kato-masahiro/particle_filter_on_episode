#coding:utf-8
"""
functionモジュールのparticle_resampling関数をテストする
"""
from functions import particles_resampling 
import pfoe

robot1 = pfoe.Robot(sensor=4,choice=3,particle_num=100)

#case1:パーティクルの分布・重みは等分
for i in range(100):
    robot1.particles.distribution[i] = i % 5
    robot1.particles.weight[i] = 1.0 / 100.0

robot1.particles = particles_resampling(robot1.particles,5) 
print robot1.particles.weight
print robot1.particles.distribution

#case2:パーティクルの分布は等分、重みはイベント0に集中
for i in range(100):
    robot1.particles.distribution[i] = i % 5
    if i % 5 == 0:
        robot1.particles.weight[i] = 1.0 / 20.0
    else:
        robot1.particles.weight[i] = 0.0

robot1.particles = particles_resampling(robot1.particles,5) 
print robot1.particles.weight
print robot1.particles.distribution
