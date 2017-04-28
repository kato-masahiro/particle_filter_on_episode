#coding:utf-8
import random
from likelihood_function import likelihood_function

def sensor_update(sensor_val,episodes,particles):
    """
    処理:全てのパーティクルについて、尤度に基づいて重みを更新する
         重みの平均値でalphaを更新する
         alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
    引数: センサ値、エピソードクラス、パーティクルクラス
    戻り値: particlesクラス
    """
    # episodes.eventsの中のセンサ値集合をまとめる
    sensor_set = []
    if len(episodes.events) == 0: #エピソード集合がまだない場合
        return particles
    else:
        for i in range(len(episodes.events)):
            sensor_set.append(episodes.events[i].sensor)

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

def retrospective_resetting(particles,episodes,resetting_threshold,resetting_step,sensor_val):
    """
    処理：
        Particles.alphaがRobot.resetting_thresholdより小さく、
        かつ
        Robot.Episode.sets[] の数が充分存在している場合
        回想に基づくリセッティングを行う
    引数: particlesクラス,episodesクラス,resetting_threshold,resetting_step,sensor_val
    引数: resetting_threshold
    戻り値:
    """
    if particles.alpha < resetting_threshold and len(episodes.events) >= resetting_step:
        # センサ値および直近のいくつかのエピソードについて、尤度を求めておく
        sensor_set = []
        for i in range(len(episodes.events)):
            sensor_set.append(episodes.events[i].sensor)
        likelihood = [ [ 0.0 for i in range( len(episodes.events) ) ] for ii in range(resetting_step) ]
        likelihood[0] = likelihood_function(sensor_val, sensor_set)
        for i in range(1, resetting_step):
            likelihood[i] = likelihood_function(episodes.events[-i].sensor, sensor_set)
        print likelihood

        # ↓ ここでやっている処理は必要ない?(尤度の削減をやっている)
        #for i in range(1, resetting_step):
        #    for ii in range( len(episodes.events) ):
        #        if episodes[ii][1] != self.episode[-i][1] or self.episode[ii][2] != self.episode[-i][2]:
        #            likelihood[i][ii] *= self.reduction_rate

        # 各エピソードの重みを求める
        weight_of_episodes = [ likelihood[0][i] for i in range( len(episodes.events) ) ]
        for i in range( len(episodes.events) ):
            for ii in range(1,resetting_step):
                try:
                    weight_of_episodes[-(i+1)] *= likelihood[ii][-(i+1) - ii]
                except:
                    weight_of_episodes[-(i+1)] *= 0 
        print weight_of_episodes
        #↑ weight_of_episodeは適切に求めることができていることは確認した

        # パーティクルをランダムにリサンプリングし、その後重みをweight_of_episodesで更新する
        s = 0.0

        print "len(episodes.events):",len(episodes.events)
        for i in range(particles.num):
            particles.distribution[i] = random.randint(0,len(episodes.events) - 1)
            particles.weight[i] = weight_of_episodes[ particles.distribution[i] ]
            s += weight_of_episodes[ particles.distribution[i] ]
        # 重みを正規化
        if s != 0.0:
            particles.weight = [ particles.weight[i] / s for i in range(particles.num) ]
        else:
            particles.weight = [ 1.0 / particles.num for i in range(particles.num) ]

    return particles

def particles_resampling(particles,events_num):
    """
    処理：各パーティクルの重みの合計値に基づいて再配置を行う
          1%の確率でランダムに再配置する
    引数: particlesクラス,イベント数
    戻り値: particlesクラス 
    """
    weight_of_episode = [0.0] * events_num

    for i in range(events_num):
        for ii in range(particles.num):
            if particles.distribution[ii] == i:
                weight_of_episode[i] += particles.weight[ii]

    if sum(weight_of_episode) == 0.0:
        for i in range(events_num):
            weight_of_episode[i] = 1.0 / events_num

    for i in range(particles.num):
        seed = random.randint(1,100)
        if seed == 1:
            particles.distribution[i] = random.randint(0,events_num - 1)
        else:
            seed = random.randint(1,10000)
            seed = float(seed) / 10000
            for ii in range(events_num):
                seed -= weight_of_episode[ii]
                if seed <= 0:
                    particles.distribution[i] = ii
                    break
    return particles
