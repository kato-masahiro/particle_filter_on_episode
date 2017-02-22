#!/bin/env python
#coding:utf-8

import math

class Robot:
    def __init__(self,sensor,choice,particle=1000,maximum=100,resetting=False):
        self.sensor = [0 for i in range(sensor)] #センサ値
        self.particle_distribution = [0 for i in range(particle)] #パーティクルの分布数
        self.particle_weight = [0.0 for i in range(particle)] #パーティクルの重み
        self.choice = choice #選択肢の数
        self.action = 0 #選択された行動
        self.reward = 0 #報酬値
        self.episode = [[self.sensor,self.action,self.reward]] #エピソード集合
        self.maximum = maximum #エピソード数の上限
        self.resetting = resetting #resettingを行うかどうか
        self.alpha = 0.0 #各パーティクルの尤度の平均

    def sensor_update(self):
        """
        処理: てすと
        引数: sensor
        戻り値:sensor*2
        """
        likeli_func(self.sensor,self.episode)

        for i in range(len(self.sensor)):
            self.sensor[i] = self.sensor[i] * 2

    def retrospective_resetting():
        """
        処理:
        引数:
        戻り値:
        """
        pass

    def motion_update():
        """
        処理:
        引数:
        戻り値:
        """
        pass

    def decision_making(self):
        """
        処理:パーティクルの分布から行動を決定して返す
        今はとりあえず1を返す
        引数:
        戻り値:
        """
        return 1;

    def particle_sliding():
        """
        処理:全てのパーティクルの分布をひとつずらす
        引数:
        戻り値:
        """
        pass

    def particle_printing():
        """
        処理:パーティクルの分布を画面に表示する
        引数:
        戻り値:
        """
        pass

def likeli_func(sensor,episode):
    """
    処理:尤度関数を定義する
    引数:センサ値のリスト、エピソード集合のリスト
    戻り値:各エピソードの尤度のリスト
    """
    likelihood = [0.0 for i in range(len(episode)) ]
    n = [0.0 for i in range(len(sensor)) ]
    print "sensor:",sensor
    print "episode:",episode
    print "likeli:",likelihood

    for i in range(len(likelihood)):
        for ii in range(len(sensor)):
            n[ii] = math.fabs( sensor[ii] - episode[i][0] )
            
    return likelihood
