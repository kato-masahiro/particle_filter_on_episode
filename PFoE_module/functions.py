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
        print len(episode.sets), "個のエピソード"
        for i in range(len(episode.sets)):
            print episode.sets[i].sensor,"を追加しました"
            sensor_set.append(episode.sets[i].sensor)

    print sensor_set

    likelihood = likelihood_function.func(sensor_val,sensor_set) 
    particle.alpha = 0.0

    for i in range(particle.num):
        particle.weight[i] = particle.weight[i] * likelihood[ particle.distribution[i] ]
        particle.alpha += particle.weight[i]

    if particle.alpha != 0.0:
        for i in range(particle.num):
            particle.weight[i] = particle.weight[i] / particle.alpha
    else:
        for i in range(particle.num):
            particle_weight[i] = 1.0 / particle_num
    return particle
