#coding:utf-8

import likelihood_function

def sensor_update(self,sensor_val,event,episode,particle):
    """
    処理:全てのパーティクルについて、尤度に基づいて重みを更新する
         重みの平均値でalphaを更新する
         alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
    引数: センサ値、イベントクラス、エピソードクラス、パーティクルクラス
    戻り値: particleクラス
    """
    likelihood = likelihood_function.func(sensor_val, episode.sets) 
    particle.alpha = 0.0

    for i in range(particle.num):
        particle.weight[i] = particle.weight[i] * likelihood[ particle.distribution[i] ]
        particle.alpha += self.particle_weight[i]

    if particle.alpha != 0.0:
        for i in range(particle.num):
            particle.weight[i] = particle.weight[i] / particle.alpha
    else:
        for i in range(particle.num):
            self.particle_weight[i] = 1.0 / self.particle_num
    return particle
