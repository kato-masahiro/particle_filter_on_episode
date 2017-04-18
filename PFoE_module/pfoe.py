#!/bin/env python
#coding:utf-8
"""
クラスの定義と
APIとしてユーザが用いる関数の定義
"""
import sys
sys.path.append("./functions")
import likelihood_function

class Event:
    def __init__(self):
        self.sensor = None
        self.action = None
        self.reward = None

class Episode:
    def __init__(self,limit):
        self.sets = []
        self.limit = limit
    def setEvent(self,event):
        self.sets.append(event)
    def getEpisode(self):
        return self.sets

class Particle:
    def __init__(self,particle):
        self.num = particle
        self.distribution = [0] * particle
        self.weight =  [1.0 / particle] * particle
        self.alpha = 0.0

class Robot:
    def __init__(self,sensor,choice,particle = 1000,limit = 100,threshold = 0.0,step = 4,reduction = 0.0):
        self.event = Event()
        self.episode = Episode(limit)
        self.particle = Particle(particle)

        self.sensor = [None] * sensor            #ロボットの得たセンサ値
        self.action = None                       #ロボットが選択した行動
        self.reward = None                       #ロボットの得た報酬値
        self.choice_num = choice                 #ロボットが取りうる選択肢の数

        self.resetting_threshold = threshold     #resettingを行うか否かを決定する閾値
        self.resetting_step = step               #何ステップをresettingに用いるか 
        self.reduction_rate = reduction          #辻褄のあわないエピソードをどの程度削減するか

    def decision_making(self,sensor_val):
        """
        引数:ロボットの獲得したセンサ値(1次元リスト)
        戻り値: self.action(整数) 
        処理: 
        1. 受け取ったセンサ値を用いて、各パーティクルの尤度を更新する(sensor_update)
        2. パーティクルの合計値がthreshold以下の場合には、回想による尤度のリセットを行う(retrospective_resetting)
        3. 尤度に基づき、パーティクルのリサンプリングを行う(particle_resampling)
        4. パーティクルの分布に基づき、最善と思われる行動を求める(decision_making)
        """
        self.particle = functions.sensor_update(sensor_val,self.event,self.episode,self.particle)
        """
        retrospective_resetting()
        particle_resampling()
        decision_making()
        """

    def set_reward():
        """
        引数:ロボットが得た報酬(数値)
        戻り値:-
        add_event()
        weight_reduction()
        particle_sliding()
        """
        pass

    def see_distribution():
        """
        引数:星の数
        戻り値:分布の様子のテキスト
        """
        pass
