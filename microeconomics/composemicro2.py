import numpy as np
import matplotlib.pyplot as plt

# 需求函数 P(Q)
def price(Q):
    return 50 - 0.5 * Q

# MR, MC
def marginal_revenue(Q):
    return 50 - Q

def marginal_cost(Q):
    return 20

# 各种数量
Q_range = np.linspace(0, 65, 300)
P_range = price(Q_range)

# 垄断下最优点
Q_monopoly = 30
P_monopoly = price(Q_monopoly)

# 完全竞争下
Q_competition = 60
P_competition = price(Q_competition)

# 政府干预价格
price_ceiling = 25  # 价格上限
price_floor = 35    # 价格下限

# 根据干预价格，重新计算对应的 Qd 和 Qs
# Qd = 100 - 2P
def demand(P): return 100 - 2 * P
def supply(P): return (P - 0)/20 * 60  # 假设 MC=20 为起始，线性从 (0,0) 到 (60, 20)

Qd_ceiling = demand(price_ceiling)
Qs_ceiling = supply(price_ceiling)

Qd_floor = demand(price_floor)
Qs_floor = supply(price_floor)

# 绘图
plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.figure(figsize=(10,6))
plt.plot(Q_range, P_range, label='Demand Curve (P=50-0.5Q)', color='green')
plt.axhline(y=20, color='red', linestyle='--', label='MC = 20')
plt.plot(Q_range, marginal_revenue(Q_range), '--', color='blue', label='MR')

# 垄断点和完全竞争点
plt.axvline(Q_monopoly, linestyle=':', color='gray', label='Monopoly Q = 30')
plt.axvline(Q_competition, linestyle=':', color='lightgray', label='Perfect Competition Q = 60')

# 价格上限
plt.axhline(price_ceiling, color='orange', linestyle='-', label=f'Price Ceiling = {price_ceiling}')
plt.scatter([Qd_ceiling], [price_ceiling], color='orange', label='Demand @ Ceiling')
plt.scatter([Qs_ceiling], [price_ceiling], color='darkorange', label='Supply @ Ceiling')
plt.fill_betweenx([0, price_ceiling], Qs_ceiling, Qd_ceiling, color='orange', alpha=0.3, label='Shortage Area')

# 价格下限
plt.axhline(price_floor, color='purple', linestyle='-', label=f'Price Floor = {price_floor}')
plt.scatter([Qd_floor], [price_floor], color='purple', label='Demand @ Floor')
plt.scatter([Qs_floor], [price_floor], color='mediumpurple', label='Supply @ Floor')
plt.fill_betweenx([0, price_floor], Qd_floor, Qs_floor, color='purple', alpha=0.3, label='Surplus Area')

plt.title("政府干预下的价格机制（上限与下限）")
plt.xlabel("Q（产量）")
plt.ylabel("价格")
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.show()