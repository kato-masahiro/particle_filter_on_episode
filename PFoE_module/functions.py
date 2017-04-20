#coding:utf-8
import likelihood_function

def sensor_update(sensor_val,episode,particle):
    """
    処理:全てのパーティクルについて、尤度に基づいて重みを更新する
         重みの平均値でalphaを更新する
         alphaを用いて重みを正規化(すべてのパーティクルの重みの和が1)する
    引数: センサ値、エピソードクラス、パーティクルクラス
    戻り値: particleクラス
    """
    # episode.setsの中のセンサ値集合をまとめる
    sensor_set = []
    if len(episode.sets) == 0: #エピソード集合がまだない場合
        return particle
    else:
        for i in range(len(episode.sets)):
            sensor_set.append(episode.sets[i].sensor)

    likelihood = likelihood_function.func(sensor_val,sensor_set) 
    particle.alpha = 0.0

    for i in range(particle.num):
        particle.weight[i] = particle.weight[i] * likelihood[ particle.distribution[i] ]
        particle.alpha += particle.weight[i]

    if particle.alpha != 0.0:
        for i in range(particle.num):
            particle.weight[i] = particle.weight[i] / particle.alpha
        particle.alpha /= particle.num
    else:
        for i in range(particle.num):
            particle.weight[i] = 1.0 / particle.num
    return particle

def retrospective_resetting()
    """
    self.alphaがself.resetting_thresholdより小さく、かつ
    self.episodeの数が充分存在している場合に
    回想に基づくリセッティングを行う
    """
    if self.alpha < self.resetting_threshold and len(self.episode) > self.resetting_step:
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
        for i in range( len(self.episode) ):
            for ii in range(1,self.resetting_step):
                try:
                    weight_of_episode[-(i+1)] *= likelihood[ii][-(i+1) - ii]
                except:
                    weight_of_episode[-(i+1)] *= 0 

        # パーティクルをランダムにリサンプリング
        # 重みはweight_of_episodeで更新
        s = 0.0
        for i in range(self.particle_num):
            self.particle_distribution[i] = random.randint(0,len(self.episode) - 1)
            self.particle_weight[i] = weight_of_episode[ self.particle_distribution[i] ]
            s += weight_of_episode[ self.particle_distribution[i] ]
        # 重みを正規化
        if s != 0.0:
            self.particle_weight = [ self.particle_weight[i] / s for i in range(self.particle_num) ]
        else:
            self.particle_weight = [ 1.0 / self.particle_num for i in range(self.particle_num) ]
