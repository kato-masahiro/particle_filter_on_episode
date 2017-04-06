#!/bin/env python
#coding:utf-8
"""
クラスの定義と
APIとしてユーザが用いる関数の定義
"""
class Event
    def __init__(self):
        self.sensor = None
        self.action = None
        self.reward = None

class Episode:
    def __init__(self,limit):
        self.episode = []
        self.limit = limit
    def setEvent(self,event):
        self.episode.append(event)
    def getEpisode(self):
        return self.episode

class Particle:
    def __init__(self,particle):
        self.particle_num = particle
        self.particle_distribution = [0] * particle
        self.particle_weight =  [1.0 / particle] * particle

class Robot:
    def __init__(self,sensor,choice,particle = 1000,limit = 100,threshold = 0.0,step = 4,reduction = 0.0):
        self.event = Event(sensor)
        self.episode = Episode(limit)
        self.particle = Particle(particle)

        self.choice_num = choice                             #ロボットが取りうる選択肢の数
        self.alpha = 0.0                                     #各パーティクルの重みの平均

        self.resetting_threshold = threshold                 #resettingを行うか否かを決定する閾値
        self.resetting_step = step                           #何ステップをresettingに用いるか 
        self.reduction_rate = reduction                      #辻褄のあわないエピソードをどの程度削減するか

    def decision_making():
        """
        引数:ロボットの獲得したセンサ値(1次元リスト)
        戻り値:ロボットの選択した行動
        """
        pass

    def set_reward():
        """
        引数:ロボットが得た報酬(数値)
        戻り値:-
        """
        pass

    def see_distribution():
        """
        引数:星の数
        戻り値:分布の様子のテキスト
        """
        pass
