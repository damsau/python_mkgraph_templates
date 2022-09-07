#-------------------------------------------------- 
# 横軸data1, 縦軸data2としてscatter plotするプログラム
#-------------------------------------------------- 

#-------------------------------------------------- 
# moduleのimport
#-------------------------------------------------- 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# デフォルトの設定ファイルがあるディレクトリのPath
# print(mpl.matplotlib_fname())
# 設定ファイルを置くディレクトリのPath
# print(mpl.get_configdir())
# 使用可能なスタイルの一覧
# print(plt.style.available)

#-------------------------------------------------- 
# rcParamsの設定を切り替え
#-------------------------------------------------- 
plt.style.use("thesis_scatter")

#-------------------------------------------------- 
# よく使うmodule
#-------------------------------------------------- 
# 線形回帰分析(y = ax + b)を実行する関数
def do_linear_regression(x, y):
    # 最小2乗線形回帰モデルの定義
    linear_model = LinearRegression()

    # 各データを2次元配列に変換
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # 回帰分析を実行
    linear_model.fit(x, y)

    # 結果の出力
    print('モデル関数の回帰係数 a : %.3f' %linear_model.coef_)
    print('モデル関数の切片 b : %.3f' %linear_model.intercept_)
    print('data1 = %.3fdata2 + %.3f' % (linear_model.coef_ , linear_model.intercept_))
    print('決定係数 R^2： ', linear_model.score(x, y))
    return linear_model.coef_, linear_model.intercept_

# 線形回帰分析(ln(y) = aln(x) + b -> y = e^b x^a)を実行する関数
def do_linear_regression_lnxy(x, y):
    # 最小2乗線形回帰モデルの定義
    linear_model = LinearRegression()

    # 各データを2次元配列に変換
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # 自然対数を計算
    ln_x = np.log(x)
    ln_y = np.log(y)

    # 回帰分析を実行
    linear_model.fit(ln_x, ln_y)

    # 結果の出力
    print('モデル関数の回帰係数 a : %.3f' %linear_model.coef_)
    print('モデル関数の切片 b : %.3f' %linear_model.intercept_)
    print('data1 = %.3fdata2 + %.3f' % (linear_model.coef_ , linear_model.intercept_))
    print('決定係数 R^2： ', linear_model.score(ln_x, ln_y))
    return linear_model.coef_, linear_model.intercept_

# 線形回帰分析(ln(y) = ax + b -> y = exp(ax+b))を実行する関数
def do_linear_regression_lny(x, y):
    # 最小2乗線形回帰モデルの定義
    linear_model = LinearRegression()

    # 各データを2次元配列に変換
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # 自然対数を計算
    ln_y = np.log(y)

    # 回帰分析を実行
    linear_model.fit(x, ln_y)

    # 結果の出力
    print('モデル関数の回帰係数 a : %.3f' %linear_model.coef_)
    print('モデル関数の切片 b : %.3f' %linear_model.intercept_)
    print('data1 = %.3fdata2 + %.3f' % (linear_model.coef_ , linear_model.intercept_))
    print('決定係数 R^2： ', linear_model.score(x, ln_y))
    return linear_model.coef_, linear_model.intercept_

#-------------------------------------------------- 
# データの読み込み
#-------------------------------------------------- 
# data1, data2 = np.loadtxt(fname = '????', comments = '!', unpack = True)
data1_name = 'data1'
data2_name = 'data2'

# 仮のデータ
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([1, 2, 3, 4, 5])

#-------------------------------------------------- 
# グラフを描画
#-------------------------------------------------- 
# 図の詳細設定
fig, ax = plt.subplots(1, 1)  # デフォルトサイズはfigsize = (5.5, 5)
ax.set_xlabel('$data1$')  # x軸ラベル
ax.set_ylabel('$data2$')  # y軸ラベル
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
ax.scatter(data1, data2, s = 60, facecolor = 'blue', edgecolor = 'blue', linewidths = 2, label = data2_name) 

# 回帰直線をプロット
coef, intercept = do_linear_regression(data1, data2)
x = np.linspace(0.0, 6.0, 1000)
line_name = 'regression line'
# regression_line = np.array(coef*x + intercept)    # 生データのままの時
# regression_line = np.array(np.exp(intercept)*x**coef)     # xy両方を対数変換した時
regression_line = np.array(np.exp(coef*x + intercept))
x = x.reshape(-1)
regression_line = regression_line.reshape(-1)
ax.plot(x, regression_line, color = 'red', label = line_name)

plt.legend(bbox_to_anchor = (1.05, 1.0), loc = 'upper left')    # 凡例
fig.savefig('./scatter_1data.png', bbox_inches = 'tight')
plt.show()
