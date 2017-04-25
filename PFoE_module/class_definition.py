#coding:utf-8
import copy

class Event:
    def __init__(self):
        self.sensor = None
        self.action = None
        self.reward = None

class Episodes:
    def __init__(self,limit):
        self.set = []
        self.limit = limit
    def setEvent(self,event):
        self.set.append(copy.deepcopy(event))
    def getEpisode(self):
        return self.set

class Particles:
    def __init__(self,particle_num):
        self.num = particle_num
        self.distribution = [0] * particle_num
        self.weight =  [1.0 / particle_num ] * particle_num
        self.alpha = 0.0

class Robot:
    def __init__(self,sensor,choice,particle_num = 1000,limit = 100,threshold = 0.0,step = 4,reduction = 0.0):
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
