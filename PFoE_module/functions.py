#coding:utf-8
from likelihood_function import likelihood_function

def sensor_update(sensor_val,episodes,particles):
    """
    処理:全てのパーティクルについて、尤度に基づいて重みを更新する
         重みの平均値でalphaを更新する
         alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
    引数: センサ値、エピソードクラス、パーティクルクラス
    戻り値: particlesクラス
    """
    # episodes.setsの中のセンサ値集合をまとめる
    sensor_set = []
    if len(episodes.sets) == 0: #エピソード集合がまだない場合
        return particles
    else:
        for i in range(len(episodes.sets)):
            sensor_set.append(episodes.sets[i].sensor)

    likelihood = likelihood_function(sensor_val,sensor_set) 
    particles.alpha = 0.0

    for i in range(particles.num):
        particles.weight[i] = particles.weight[i] * likelihood[ particles.distribution[i] ]
        particles.alpha += particles.weight[i]

    if particles.alpha != 0.0:
        for i in range(particles.num):
            particles.weight[i] = particles.weight[i] / particles.alpha
        particles.alpha /= particles.num
    else:
        for i in range(particles.num):
            particles.weight[i] = 1.0 / particles.num
    return particles

#def retrospective_resetting()
#   """
#   処理：
#       Particle.alphaがRobot.resetting_thresholdより小さく、
#       かつ
#       Robot.Episode.sets[] の数が充分存在している場合
#       回想に基づくリセッティングを行う
#   引数: particlesクラス,episodesクラス,resetting_threshod,resetting_step,sensor_val
#   引数: resetting_threshold
#   戻り値:
#   """
#   if self.alpha < self.resetting_threshold and len(self.episodes) > self.resetting_step:
#       # センサ値および直近のいくつかのエピソードについて、尤度を求めておく
#       likelihood = [ [ 0.0 for i in range( len(self.episodes) ) ] for ii in range(self.resetting_step) ]
#       likelihood[0] = likelihood_function(self.sensor, self.episodes)
#       for i in range(1,self.resetting_step):
#           likelihood[i] = likelihood_function(self.episodes.sets[].sensor, self.episode)
#       for i in range(1,self.resetting_step):
#           for ii in range( len(self.episodes) ):
#               if self.episodes[ii][1] != self.episode[-i][1] or self.episode[ii][2] != self.episode[-i][2]:
#                   likelihood[i][ii] *= self.reduction_rate
#       # 各エピソードの重みを求める
#       weight_of_episodes = [ likelihood[0][i] for i in range( len(self.episode) ) ]
#       for i in range( len(self.episodes) ):
#           for ii in range(1,self.resetting_step):
#               try:
#                   weight_of_episodes[-(i+1)] *= likelihood[ii][-(i+1) - ii]
#               except:
#                   weight_of_episodes[-(i+1)] *= 0 

#       # パーティクルをランダムにリサンプリング
#       # 重みはweight_of_episodesで更新
#       s = 0.0
#       for i in range(self.particles_num):
#           self.particles_distribution[i] = random.randint(0,len(self.episodes) - 1)
#           self.particles_weight[i] = weight_of_episodes[ self.particles_distribution[i] ]
#           s += weight_of_episodes[ self.particles_distribution[i] ]
#       # 重みを正規化
#       if s != 0.0:
#           self.particles_weight = [ self.particles_weight[i] / s for i in range(self.particles_num) ]
#       else:
#           self.particles_weight = [ 1.0 / self.particles_num for i in range(self.particles_num) ]
