# 두 집단(봇과 사람 표준편차 데이터의 분포 비교 시각화
def visualize_by_numpy(dataset):
  # 1. 표준편차 샘풀 추출 (160,)
  std_vals=dataset[:,-2]
  label_vals=dataset[:,-1] # label 샘풀

  # 2.논리인덱싱을 이용하여 그룹 봇과 사람으로 분리
  bot_stds = std_vals[label_vals == 1]
  human_stds = std_vals[label_vals == 0]

  # 4. 시각화 
  plt.figure(figsize=(10, 6))
  plt.hist(bot_stds, bins=20, alpha=0.7, label='봇', color = 'red') #봇 집단 표준편차 히스토그램
  plt.hist(human_stds, bins=30, alpha=0.7, label='사람', color = 'blue', edgecolor='black')
  plt.title("표준편차에 따른 봇과 사람 분포 비교")
  plt.xlabel("표준편차")
  plt.ylabel("빈도")
  plt.grid(True)
  plt.legend()
  plt.show()
