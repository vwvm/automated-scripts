import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_csv('./data.csv')
Kobe = raw_data.drop(['game_event_id', 'team_id', 'team_id', 'team_name', 'lon', 'lat', 'matchup'], axis=1)
shot_attempt = Kobe.groupby(['combined_shot_type', 'action_type'])['shot_id'].count().to_frame('attempt')
shot_attempt['percentage'] = shot_attempt.attempt / shot_attempt.attempt.sum()
shot_attempt.groupby(level=0, group_keys=False)['percentage'].sum()
tmp = shot_attempt['percentage'].nlargest(9).to_frame()
tmp.index = tmp.index.map(lambda x: x[1])
tmp.loc['rest'] = 1 - tmp['percentage'].sum()

# y = np.array([35, 25, 25, 15])
# print(y)
#
# plt.pie(y,
#         labels=['A','B','C','D'], # 设置饼图标签
#         colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
#         explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
#         autopct='%.2f%%', # 格式化输出百分比
#        )
# plt.title("RUNOOB Pie Test")
# plt.show()

plt.subplot(2, 2, 1)
plt.pie(np.array([i[0] for i in np.array(tmp)]), labels=tmp.index, autopct='%.0f%%')
plt.show()
