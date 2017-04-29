#!/bin/env python
#coding:utf-8
"""
APIとしてユーザが用いる関数を提供する
"""
from likelihood_function import likelihood_function
import class_definition

def decision_making(self,sensor_val):
    """
    引数:ロボットの獲得したセンサ値(1次元リスト)
    戻り値: self.action(整数) 
    処理: 
    1. 受け取ったセンサ値を用いて、各パーティクルの尤度を更新する(sensor_update)
    2. パーティクルの合計値がthreshold以下の場合には、回想による尤度のリセットを行う(retrospective_resetting)
    3. 重みに基づき、パーティクルのリサンプリングを行う(particle_resampling)
    4. パーティクルの分布に基づき、最善と思われる行動を求める(decision_making)
    """
    self.particle = functions.sensor_update(sensor_val,self.event,self.episode,self.particle)
    self.particle = retrospective_resetting(self.particles, self.episodes, self.resetting_threshold, self.resetting_step, sensor_val)
    self.particle = particle_resampling( self.particles,len(self.episodes.events) )
    action = decision_making()

    return action

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
