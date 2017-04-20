#coding:utf-8

class Event:
    def __init__(self):
        sensor = None
        action = None
        reward = None

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
