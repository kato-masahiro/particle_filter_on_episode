#!/bin/env python
#coding:utf-8
"""
必要なクラス内容を定義する
"""
class History:
    def __init__(self,limit,sensor):
        self.limit = limit
        self.sensor_log = [[None]]
        self.action_log = [None]
        self.reward_log = [None]

class Particle:
    def __init__(self,particle):
        self.particle_num = particle
        self.particle_distribution = [0] * particle
        self.particle_weight =  [1.0 / particle] * particle

class Robot:
    def __init__(self,sensor,choice,particle = 1000,limit = 100,threshold = 0.0,step = 4,reduction = 0.0):
        self.history = History(limit, sensor)
        self.particle = Particle(particle)

        self.sensor = [None] * sensor                        #センサ値が入るリスト
        self.action = None                                   #選択された行動
        self.reward = None                                   #報酬値
        self.choice_num = choice                             #ロボットが取りうる選択肢の数
        self.alpha = 0.0                                     #各パーティクルの重みの平均

        self.resetting_threshold = threshold                 #resettingを行うか否かを決定する閾値
        self.resetting_step = step                           #何ステップをresettingに用いるか 
        self.reduction_rate = reduction                      #辻褄のあわないエピソードをどの程度削減するか
