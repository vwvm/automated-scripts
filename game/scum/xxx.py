import numpy as np
import pandas as pd

raw_data = pd.read_csv('./data.csv')
Kobe = raw_data.drop(['game_event_id', 'team_id', 'team_id', 'team_name', 'lon', 'lat', 'matchup'], axis=1)
Kobe['home'] = raw_data.matchup.apply(lambda x: 0 if x[4] == '@' else 1)
Kobe['secondsFromPeriodEnd'] = 60 * raw_data['minutes_remaining'] + raw_data['seconds_remaining']
Kobe['secondsFromPeriodStart'] = 60 * (11 - raw_data['minutes_remaining']) + (60 - raw_data['seconds_remaining'])
Kobe['secondsFromGameStart'] = (raw_data['period'] <= 4).astype(int) * (raw_data['period'] - 1) * 12 * 60 + (
        raw_data['period'] > 4).astype(int) * ((raw_data['period'] - 4) * 5 * 60 + 3 * 12 * 60) + Kobe[
                                   'secondsFromPeriodStart']
Kobe.dropna(inplace=True)
Kobe['game_date'] = Kobe.game_date.apply(lambda x: pd.to_datetime(x))
Kobe.game_date
Kobe.loc[:5, ['home', 'period', 'minutes_remaining', 'seconds_remaining', 'secondsFromGameStart']]
Kobe.info()
Kobe['shot_made_flag'].mean()
Kobe.pivot_table(index='game_id', values=['shot_made_flag'], aggfunc=np.mean)
import matplotlib.pyplot as plt

tmp = Kobe.pivot_table(index='game_id', values=['shot_made_flag'], aggfunc=np.mean)
tmp.index = range(len(tmp))
plt.plot(tmp)
Kobe.pivot_table(index=['season', 'period'], values=['shot_made_flag'], aggfunc=np.mean)
Kobe.pivot_table(index=['period'], values=['shot_made_flag'], aggfunc=np.mean)
p_1 = Kobe[Kobe.period == 1].pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_2 = Kobe[Kobe.period == 2].pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_3 = Kobe[Kobe.period == 3].pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_4 = Kobe[Kobe.period == 4].pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_5 = Kobe[Kobe.period > 4].pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_t = Kobe.pivot_table(index=['season'], values=['shot_made_flag'], aggfunc=np.mean)
p_1.index = p_1.index.map(lambda x: x[:4])
p_2.index = p_2.index.map(lambda x: x[:4])
p_3.index = p_3.index.map(lambda x: x[:4])
p_4.index = p_4.index.map(lambda x: x[:4])
p_5.index = p_5.index.map(lambda x: x[:4])
p_t.index = p_t.index.map(lambda x: int(x[:4]))
plt.plot(p_1)
plt.plot(p_2)
plt.plot(p_3)
plt.plot(p_4)
plt.plot(p_5)
plt.legend(('period1', 'period2', 'period3', 'period4', 'total'))
time_slice = 24
time_bins = np.arange(0, 60 * (4 * 12 + 3 * 5), time_slice) + 0.01
attempt_shot, b = np.histogram(Kobe['secondsFromGameStart'], bins=time_bins)
made_shot, b = np.histogram(Kobe.loc[Kobe['shot_made_flag'] == 1, 'secondsFromGameStart'], bins=time_bins)
attempt_shot
attempt_shot[attempt_shot < 10] = 1
accuracy = made_shot / attempt_shot
accuracy[accuracy >= 1] = 0
height = 1
bar_width = 0.999 * (time_bins[1] - time_bins[0])
plt.xlim((-20, 3200))
plt.ylim((0, height))
plt.ylabel('accuracy')
plt.title('24 second time bins')
plt.vlines(x=[0, 12 * 60, 2 * 12 * 60, 3 * 12 * 60, 4 * 12 * 60, 4 * 12 * 60 + 5 * 60, 4 * 12 * 60 + 2 * 5 * 60,
              4 * 12 * 60 + 3 * 5 * 60], ymin=0, ymax=height, color='r')
plt.bar(time_bins[:-1], accuracy, align='edge', width=bar_width)
time_slices = [24, 12, 6]
plt.rcParams['figure.figsize'] = (16, 16)
plt.rcParams['font.size'] = 16
plt.figure()
for i, time_slice in enumerate(time_slices):
    time_bins = np.arange(0, 60 * (4 * 12 + 3 * 5), time_slice) + 0.01
    attempt_shot, b = np.histogram(Kobe['secondsFromGameStart'], bins=time_bins)
    made_shot, d = np.histogram(Kobe.loc[Kobe['shot_made_flag'] == 1, 'secondsFromGameStart'], bins=time_bins)
    attempt_shot[attempt_shot < 10] = 1
    accuracy = made_shot / attempt_shot
    accuracy[accuracy >= 1] = 0
    plt.subplot(3, 1, i + 1)
    plt.xlim((-20, 3200))
    plt.ylim((0, height))
    plt.ylabel('accuracy')
    plt.title(str(time_slice) + 'second time bins')
    plt.vlines(x=[0, 12 * 60, 2 * 12 * 60, 3 * 12 * 60, 4 * 12 * 60, 4 * 12 * 60 + 5 * 60, 4 * 12 * 60 + 2 * 5 * 60,
                  4 * 12 * 60 + 3 * 5 * 60], ymin=0, ymax=height, colors='r')
    plt.bar(time_bins[:-1], accuracy, align='edge', width=bar_width)
Kobe.pivot_table(index='shot_zone_area', values=['shot_made_flag'], aggfunc=np.mean)
Kobe.pivot_table(index='shot_zone_basic',values=['shot_made_flag'],aggfunc=np.mean)
