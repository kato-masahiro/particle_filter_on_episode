#!/bin/env python
#coding:utf-8

import random
import math
import likelihood_function

"""
PFoEのための関数を提供するモジュール
likelihood_function.pyの中で尤度関数の内容を定義
"""
class Robot:
    def __init__(self,sensor,choice,particle=1000,maximum=100,resetting=False):
        self.sensor = [0 for i in range(sensor)] #センサ値
        self.particle_num = particle #パーティクルの数
        self.particle_distribution = [0 for i in range(particle)] #パーティクルの分布数
        self.particle_weight = [1.0 / particle for i in range(particle)] #パーティクルの重み
        self.choice = choice #選択肢の数
        self.action = 0 #選択された行動
        self.reward = 0 #報酬値
        self.episode = [[self.sensor,self.action,self.reward]] #エピソード集合
        self.maximum = maximum #エピソード数の上限
        self.resetting = resetting #resettingを行うかどうか
        self.alpha = 0.0 #各パーティクルの尤度の平均

    def likeli_func(self):
        """
        尤度関数のテスト
        """
        l = likelihood_function.func(self.sensor,self.episode)
        print "尤度:",l

    def test(self):
        """
        処理: てすと
        引数: sensor
        戻り値:sensor*2
        """
        for i in range(len(self.sensor)):
            self.sensor[i] = self.sensor[i] * 2

    def sensor_update(self):
        """
        処理:全てのパーティクルについて、尤度に基づいて重みを更新する
             新しい重みの平均でalphaを更新する
        引数: -
        戻り値: - 
        """
        likelihood = likelihood_function.func(self.sensor, self.episode) 
        s = 0.0
        self.alpha = 0.0

        for i in range(self.particle_num):
            self.particle_weight[i] = self.particle_weight[i]\
                                       * likelihood[ self.particle_distribution[i] ]
            s += self.particle_weight[i]
        for i in range(self.particle_num):
            self.particle_weight[i] = self.particle_weight[i] / s
            self.alpha = self.particle_weight[i]
        self.alpha /= self.particle_num

    def motion_update():
        """
        処理:重みに基づきパーティクルをリサンプリングする
        引数: - 
        戻り値: -
        """
        weight_of_episode = [0.0 for i in range( len(self.episode) ) ] 

        for i in range(self.particle_num):
            weight_of_episode[i] += self.particle_weight[i]
        for i in range(self.particle_num):
            seed = random.randint(1,10000)
            seed = float(seed) / 10000
            for ii in range( len(self.episode) ):
                

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
        処理:パーティクルの分布の様子を画面に表示する
        引数: - 
        戻り値: - 
        """
        pass
