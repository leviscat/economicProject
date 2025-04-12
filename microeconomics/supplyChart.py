import matplotlib.pyplot as plt
import numpy as np

# 创建价格和数量范围
price = np.linspace(4, 12, 100)

# 假设的线性需求函数：价格越低，需求越高
def demand(p):
    return 100 - 5 * p

# 假设的线性供给函数：价格越高，供给越多
def supply(p):
    return -20 + 10 * p

# 计算需求和供给量
demand_qty = demand(price)
supply_qty = supply(price)
plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
# 画图
plt.figure(figsize=(10, 6))
plt.plot(demand_qty, price, label='需求曲线 (Demand)', color='blue')
plt.plot(supply_qty, price, label='供给曲线 (Supply)', color='green')

# 原始均衡点：需求 = 供给
# 解方程：100 - 5P = -20 + 10P => P = 8，Q = 60
plt.scatter(60, 8, color='black')
plt.text(61, 8.1, '原始均衡点 (P=8, Q=60)', fontsize=10)

# 新价格 = 6
# 需求量 = 100 - 5*6 = 70
# 供给量 = -20 + 10*6 = 40
plt.scatter(70, 6, color='red')
plt.scatter(40, 6, color='orange')
plt.plot([40, 70], [6, 6], 'k--', alpha=0.5)
plt.text(71, 6.1, '需求点', color='red')
plt.text(30, 6.1, '供给点', color='orange')

# 图形细节
plt.xlabel('数量 (Q)')
plt.ylabel('价格 (P)')
plt.title('价格下降时的供需变化示意图')
plt.legend()
plt.grid(True)
plt.xlim(20, 100)
plt.ylim(4, 12)


plt.show()
