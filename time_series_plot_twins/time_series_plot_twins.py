#-------------------------------------------------- 
# 横軸時間, 縦軸data2, data3としてline plotするプログラム(y軸を2軸plot)
#-------------------------------------------------- 

#-------------------------------------------------- 
# moduleのimport
#-------------------------------------------------- 
from cProfile import label
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# デフォルトの設定ファイルがあるディレクトリのPath
print(mpl.matplotlib_fname())
# 設定ファイルを置くディレクトリのPath
print(mpl.get_configdir())
# 使用可能なスタイルの一覧
print(plt.style.available)

#-------------------------------------------------- 
# rcParamsの設定を切り替え
#-------------------------------------------------- 
plt.style.use("thesis_time_series_plot")

#-------------------------------------------------- 
# データの読み込み
#-------------------------------------------------- 
# data1, data2 = np.loadtxt(fname = '????', comments = '!', unpack = True)
data1_name = 'time'
data2_name = 'data2'
data3_name = 'data3'

# 仮のデータ
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([1, 3, 2, 4, 0])
data3 = np.array([2, 1, 4, 3, 5])

#-------------------------------------------------- 
# グラフを描画
#-------------------------------------------------- 
# 図の詳細設定
fig, ax1 = plt.subplots(1, 1)  # デフォルトサイズはfigsize = (5.5, 5)
ax2 = ax1.twinx()   # x軸を2軸plot
ax1.set_xlabel(r'$t$')  # x軸ラベル
ax1.set_ylabel(r'$data2$')  # y軸ラベル
ax2.set_ylabel(r'$data3$')  # y軸ラベル
# ax.xaxis.label.set_size(30)   # x軸ラベルのフォントサイズ，デフォルトは30
# ax.yaxis.label.set_size(30)   # y軸ラベルのフォントサイズ，デフォルトは30
# ax.set_xscale('log')    # x軸に対数プロットを適用
# ax.set_yscale('log')    # y軸に対数プロットを適用
# ax.set_xlim(0, 6)   # x軸のプロット範囲
# ax.set_ylim(0, 6)   # y軸のプロット範囲
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6])  # x軸の目盛りを打つ場所を手動で設定
# ax.set_yticks([0, 1, 2, 3, 4, 5, 6])  # y軸の目盛りを打つ場所を手動で設定
# ax.set_xticklabels(["0", "1", "2", "3", "4", "5", "6"])   # x軸の目盛りの表記を手動で設定
# ax.set_yticklabels(["0", "1", "2", "3", "4", "5", "6"])   # y軸の目盛りの表記を手動で設定
# ax.tick_params(labelsize = 16)    # 目盛りのフォントサイズ, デフォルトは16

# データをプロット
ax1.plot(data1, data2, color = 'red', label = data2_name)
ax2.plot(data1, data3, color = 'blue', label = data3_name)


# 回帰直線をプロット
# x = np.linspace(0.0, 6.0, 1000)
# line_name = 'regression line'

# 凡例
handler1, label1 = ax1.get_legend_handles_labels()
handler2, label2 = ax2.get_legend_handles_labels()
ax1.legend(handler1 + handler2, label1 + label2, bbox_to_anchor = (1.10, 1.0), loc = 'upper left')    # 凡例
# fig.savefig('./scatter_1data.png', bbox_inches = 'tight')
plt.show()