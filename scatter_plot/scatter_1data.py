#-------------------------------------------------- 
# moduleのimport
#-------------------------------------------------- 
from distutils.command.config import config
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
plt.style.use("thesis_scatter")




# print(plt.rcParams)

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
plt.scatter(x, y)
plt.text(1, 3, "abcde")
plt.plot(x, y)
plt.show()

