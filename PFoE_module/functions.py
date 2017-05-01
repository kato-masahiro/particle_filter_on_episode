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

def decision_making(episodes,particles,choice):
    """
    処理:パーティクルの分布から行動を決定して返す
         episodesがまだ無い場合には適当なものを返す
    引数: episodesクラス,particlesクラス,選択肢の数
    戻り値: action
    """
    if(len(episodes.events) == 0):
        return random.randint(0,choice - 1)

    vote = [0.0] * particles.num
    for i in range(particles.num):
        distance = 0
        non_zero_reward = 0.0
        for l in range(0, len(episodes.events) - particles.distribution[i]):
            distance += 1
            if episodes.events[particles.distribution[i] +l ].reward != 0:
                non_zero_reward = episodes.events[particles.distribution[i] +l].reward
                break
        if non_zero_reward != 0:
            vote[i] = non_zero_reward / distance
        else:
            vote[i] = 0.0
    print vote

    # 各選択肢に投票させる
    got = [0.0] * choice #各選択肢が持つ得票数
    for p in range(particles.num):
        for g in range( len(got) ):
            if episodes.events[ particles.distribution[p] ].action == g:
                got[g] += vote[p]
                break

    #最大の評価を持つ選択肢を返す
    #最大値を持つ選択肢が複数存在する場合は、その中からランダムに返す
    mx = max(got)
    mx_n = 0 #有効な選択肢が幾つあるか
    mx_list = [0] * choice #有効な選択肢はどれか
    for i in range(choice):
        if got[i] == mx:
            mx_list[mx_n] = i
            mx_n += 1
    seed = random.randint(0,mx_n-1)
    action = mx_list[seed]
    print action
    return action

def set_event(events):
    """
    処理:
        ロボットのエピソード集合に新しいイベントを追加する
        追加した結果、エピソード数の上限に達した場合は最も古いイベントを削除する
    引数: eventクラス,episodesクラス
    戻り値: episodesクラス
    """
    l = []
    l.append(sensor)
    l.append(action)
    l.append(reward)
    if(self.episode[0][1] is None):
        self.episode[0] = l
    else:
        self.episode.append(l)

    if( len(self.episode) == self.limit ):
        del self.episode[0]

def weight_reduce():
    """
    パーティクルが持つ重み(particle_weight[])について、
    そのパーティクルが存在しているエピソードが最新のイベントの行動・報酬と比較して矛盾している場合に
    係数(reduction_rate)を掛けて削減する
    """
    latest = len(self.episode) - 1
    for i in range(self.particle_num):
        if( self.episode[ self.particle_distribution[i] ][1] != self.episode[latest][1] \
            or \
        self.episode[ self.particle_distribution[i] ][2] != self.episode[latest][2] ):
            self.particle_weight[i] *= self.reduction_rate

def slide
    """
    すべてのパーティクルの分布を一つずらす
    """
    for i in range(self.particle_num):
        if self.particle_distribution[i] != (len(self.episode) - 1):
            self.particle_distribution[i] += 1
