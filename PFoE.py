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
    def __init__(self,sensor,choice,particle = 1000,maximum = 100,threshold = 0.0,step = 4,reduction = 0.0):
        self.sensor = [None for i in range(sensor)] #センサ値が入るリスト
        self.particle_num = particle #パーティクルの数
        self.particle_distribution = [0 for i in range(particle)] #パーティクルの分布場所
        self.particle_weight = [1.0 / particle for i in range(particle)] #パーティクルの重み
        self.choice = choice #ロボットが取りうる選択肢の数
        self.action = None  #選択された行動
        self.reward = None  #報酬値
        self.episode = [ [self.sensor,self.action,self.reward] ] #エピソード集合
        self.maximum = maximum #エピソード集合に保存されるイベント数の上限
        self.alpha = 0.0 #各パーティクルの重みの平均
        self.resetting_threshold = threshold #resettingを行うか否かを決定する閾値
        self.resetting_step = step #何ステップをresettingに用いるか
        self.reduction_rate = reduction #辻褄のあわないエピソードをどの程度削減するか

    def add_event(self,sensor,action,reward):
        """
        処理:ロボットのエピソード集合に新しいイベントを追加する
             追加した結果、エピソード数の上限に達した場合は最も古いイベントを削除する
        引数:sensor[],action,reward
        戻り値: - 
        """
        l = []
        l.append(sensor)
        l.append(action)
        l.append(reward)
        if(self.episode[0][1] is None):
            self.episode[0] = l
        else:
            self.episode.append(l)

        if( len(self.episode) > self.maximum ):
            del self.episode[0]

    def likeli_func(self):
        """
        尤度関数のテスト
        """
        l = likelihood_function.func(self.sensor,self.episode)
        print "尤度:",l

    def sensor_update(self):
        """
        処理:全てのパーティクルについて、尤度に基づいて重みを更新する
             重みの平均値でalphaを更新する
             alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
        引数: -
        戻り値: - 
        """
        likelihood = likelihood_function.func(self.sensor, self.episode) 
        self.alpha = 0.0

        for i in range(self.particle_num):
            self.particle_weight[i] = self.particle_weight[i]\
                                       * likelihood[ self.particle_distribution[i] ]
            self.alpha += self.particle_weight[i]

        if self.alpha != 0.0:
            for i in range(self.particle_num):
                self.particle_weight[i] = self.particle_weight[i] / self.alpha
        else:
            for i in range(self.particle_num):
                self.particle_weight[i] = 1.0 / self.particle_num

    def retrospective_resetting(self):
        """
        処理:alphaがresetting_thresholdより小さい場合、回想に基づく重みのリセッティングを行う。
        引数:
        戻り値:
        """
        if self.alpha < self.resetting_threshold:
            # センサ値および直近のいくつかのエピソードについて、尤度を求めておく
            likelihood = [ [ 0.0 for i in range( len(self.episode) ) ] for ii in range(self.resetting_step) ]
            likelihood[0] = likelihood_function.func(self.sensor, self.episode)
            for i in range(1,self.resetting_step):
                likelihood[i] = likelihood_function.func(self.episode[-i][0], self.episode)
            for i in range(1,self.resetting_step):
                for ii in range( len(self.episode) ):
                    if self.episode[ii][1] != self.episode[-i][1] or self.episode[ii][2] != self.episode[-i][2]:
                        likelihood[i][ii] *= self.reduction_rate
            # 各エピソードの重みを求める
            weight_of_episode = [ likelihood[0][i] for i in range( len(self.episode) ) ]
            print weight_of_episode
            for i in range( len(self.episode) ):
                for ii in range(1,self.resetting_step):
                    try:
                        weight_of_episode[-(i+1)] *= likelihood[ii][-(i+1) - ii]
                    except:
                        weight_of_episode[-(i+1)] *= 0 
                
            print "likelihood:",likelihood            
            print "weight_of_episide:",weight_of_episode
            
    def particle_resampling(self):
        """
        処理:重みに基づきパーティクルをリサンプリングする
             1 % のパーティクルはランダムにリサンプリングする
        引数: - 
        戻り値: -
        """
        weight_of_episode = [0.0 for i in range( len(self.episode) ) ]

        for i in range( len(self.episode) ):
            for ii in range(self.particle_num):
                if self.particle_distribution[ii] == i:
                    weight_of_episode[i] += self.particle_weight[ii]

        if sum(weight_of_episode) == 0.0:
            for i in range( len(self.episode) ):
                weight_of_episode[i] = 1.0 / len(self.episode)

        for i in range(self.particle_num):
            seed = random.randint(1,100)
            if seed == 1:
                self.particle_distribution[i] = random.randint(0,len(self.episode) - 1)
            else:
                seed = random.randint(1,10000)
                seed = float(seed) / 10000
                for ii in range( len(self.episode) ):
                    seed -= weight_of_episode[ii]
                    if seed <= 0:
                        self.particle_distribution[i] = ii
                        break

    def randomly_resampling(self):
        """
        処理:全てのパーティクルをエピソード中に均等にリサンプリングする
             全てのパーティクルの重みを均等にする
        引数: -
        戻り値: -
        """
        for i in range(self.particle_num):
            self.particle_distribution[i] = random.randint(0,len(self.episode) - 1) 
            self.particle_weight[i] = 1.0 / self.particle_num

    def decision_making(self):
        """
        処理:パーティクルの分布から行動を決定して返す
        引数: - 
        戻り値: action
        """
        vote = [0.0 for i in range(self.particle_num) ]

        if(self.episode[0][1] == None):
            return random.randint(0,self.choice - 1)

        for i in range(self.particle_num):
            distance = 0
            non_zero_reward = 0.0
            for l in range( len(self.episode) - self.particle_distribution[i] ):
                distance += 1
                if self.episode[ self.particle_distribution[i] + l ][2] != 0:
                    non_zero_reward = self.episode[ self.particle_distribution[i] + l ][2]
                    break
            if non_zero_reward != 0:
                vote[i] = non_zero_reward / distance
            else:
                vote[i] = 0.0

        got = [0.0 for i in range(self.choice) ] #各選択肢が持つ得票数
        for p in range(self.particle_num):
            for g in range( len(got) ):
                if self.episode[self.particle_distribution[p]][1] == g:
                    got[g] += vote[p]
                    break

        #最大の評価を持つ選択肢を返す
        #最大値を持つ選択肢が複数存在する場合は、その中からランダムに返す
        mx = max(got)
        mx_n = 0 #有効な選択肢が幾つあるか
        mx_list = [0 for i in range(self.choice)] #有効な選択肢はどれか
        for i in range(self.choice):
            if got[i] == mx:
                mx_list[mx_n] = i
                mx_n += 1
        seed = random.randint(0,mx_n-1)
        action = mx_list[seed]
        return action

    def particle_sliding(self):
        """
        処理:全てのパーティクルの分布をひとつずらす
        引数:
        戻り値:
        """
        for i in range(self.particle_num):
            if self.particle_distribution[i] != (len(self.episode) - 1):
                self.particle_distribution[i] += 1

    def weight_reduction(self):
        """
        処理:パーティクルが持つ重み(particle_weight[])について、
             そのパーティクルが存在しているエピソードが、
             最新のイベントと比較して矛盾している場合に、
             係数(reduction_rate)を掛けて削減する
             最新のイベントを追加した後、パーティクルをスライドさせる前に実行する
        引数: - 
        戻り値: -
        """
        latest = len(self.episode) - 1
        # 行動による削減
        for i in range(self.particle_num):
            if( self.episode[ self.particle_distribution[i] ][1] != self.episode[latest][1] \
                or \
            self.episode[ self.particle_distribution[i] ][2] != self.episode[latest][2] ):
                self.particle_weight[i] *= self.reduction_rate

    def see_distribution(self,star = 50):
        """
        処理:パーティクルの分布の様子を画面に表示する
        引数:star 
        戻り値: - 
        """
        particle_numbers = [0 for i in range( len(self.episode) ) ]
        for i in range(self.particle_num):
            particle_numbers[ self.particle_distribution[i] ] += 1

        print "A\t|R\t|N\t|Distribution",

        for i in range( len(self.episode) ):
            print "\n",self.episode[i][1],"\t|",self.episode[i][2],"\t|",particle_numbers[i],"\t|",
            for ii in range(int( float(particle_numbers[i]) / float(self.particle_num) * float(star) ) ):
                print "*",
