#!/bin/env python
#coding:utf-8
"""
APIとしてユーザが用いる関数を提供する
"""
import copy
import os
from likelihood_function import likelihood_function
from functions import sensor_update
from functions import retrospective_resetting
from functions import particles_resampling
from functions import decision_making
from functions import set_event
from functions import weight_reduce
from functions import particles_slide

class Event:
    def __init__(self):
        self.sensor = None
        self.action = None
        self.reward = None

class Episodes:
    def __init__(self,limit):
        self.events = []
        self.limit = limit
    def setEvent(self,event):
        self.events.append(copy.deepcopy(event))
    def getEpisode(self):
        return self.events

class Particles:
    def __init__(self,particle_num):
        self.num = particle_num
        self.distribution = [0] * particle_num
        self.weight =  [1.0 / particle_num ] * particle_num
        self.alpha = 0.0

class Robot:
    def __init__(self,sensor,choice,particle_num = 1000,limit = -1,threshold = 0.0,step = 4,reduction = 0.0):
        self.event = Event()
        self.episodes = Episodes(limit)
        self.particles = Particles(particle_num)

        self.sensor = [None] * sensor            #ロボットの得たセンサ値
        self.action = None                       #ロボットが選択した行動
        self.reward = None                       #ロボットの得た報酬値
        self.choice_num = choice                 #ロボットが取りうる選択肢の数

        self.resetting_threshold = threshold     #resettingを行うか否かを決定する閾値
        self.resetting_step = step               #何ステップをresettingに用いるか 
        self.reduction_rate = reduction          #辻褄のあわないエピソードをどの程度削減するか

    def read(self):
        """
        過去のエピソード、重み等をファイルから読み込む
        """
        if os.path.exists("episodes_data.txt") and os.path.exists("particles_data.txt"):
            f = open('episodes_data.txt','r')
            list = f.readlines()
            #最後の一文字(改行)を削除,文字列からリストにする
            for i in range( len(list) ):
                list[i] = list[i][:-1]
                list[i] = eval( list[i] )

            n = 0
            for i in range (0, len(list) ,3):
                self.event.sensor = list[i]
                self.event.action = list[i+1]
                self.event.reward = list[i+2]
                self.episodes.setEvent(self.event)
                n += 1
            f.close()

            f = open('particles_data.txt')
            list = f.readlines()
            self.particles.distribution = eval(list[0])
            self.particles.weight = eval(list[1])
        else:
            print "The files did not exists."

    def write(self):
        """
        学習結果をファイルに書き込む
        """
        f = open("episodes_data.txt","w")
        for i in range ( len ( self.episodes.events )  ):
            print self.episodes.events[i].sensor
            f.write(str(self.episodes.events[i].sensor))
            f.write("\n")
            f.write(str(self.episodes.events[i].action))
            f.write("\n")
            f.write(str(self.episodes.events[i].reward))
            f.write("\n")
        f.close()

        f = open("particles_data.txt","w")
        f.write(str(self.particles.distribution))
        f.write("\n")
        f.write(str(self.particles.weight))
        f.write("\n")
        f.close()

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
        if(len(sensor_val) != self.sensor):
            self.sensor = sensor_val
        else:
            print "Error: Incorrect number of sensor values"
            exit(1)
        self.particles = sensor_update(sensor_val,self.episodes,self.particles)
        self.particles = retrospective_resetting(self.particles, self.episodes, self.resetting_threshold, self.resetting_step, sensor_val, self.reduction_rate)
        self.particles = particles_resampling( self.particles,len(self.episodes.events) )
        self.action = decision_making(self.episodes, self.particles, self.choice_num)

        return self.action

    def set_reward(self,reward_val):
        """
        引数:ロボットが得た報酬(数値)
        戻り値:-
        処理: 
        1.最新のイベントをepisodes.eventsにアペンドする(set_event)
        2.各パーティクルが存在しているエピソードが最新のものと比較して矛盾している場合
          その重みを削減する(weight_reduce)
        3.すべてのパーティクルの分布を一つずらす(particle_slie)
        """
        self.episodes,self.particles = set_event(self.sensor,self.action,reward_val,self.event,self.episodes,self.particles)
        self.particles = weight_reduce(self.episodes,self.particles,self.reduction_rate)
        self.particles = particles_slide(self.particles,self.episodes)

    def see_distribution(self,star = 50):
        """
        処理:パーティクルの分布の様子を画面に表示する
        引数: 星の数
        戻り値: - 
        """
        particle_numbers = [0 for i in range( len(self.episodes.events) ) ]
        for i in range(self.particles.num):
            particle_numbers[ self.particles.distribution[i] ] += 1

        print "A\t|R\t|N\t|Distribution",


        for i in range( len(self.episodes.events) ):
            print "\n",self.episodes.events[i].action,"\t|",self.episodes.events[i].reward,"\t|",particle_numbers[i],"\t|",
            for ii in range(int( float(particle_numbers[i]) / float(self.particles.num) * float(star) ) ):
                print "*",
