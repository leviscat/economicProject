import numpy as np
import matplotlib.pyplot as plt

# 定义基本函数
def price(Q):
    return 50 - 0.5 * Q  # P(Q)

def total_revenue(Q):
    return price(Q) * Q

def marginal_revenue(Q):
    return 50 - Q

def total_cost(Q):
    return 20 * Q

def marginal_cost(Q):
    return 20

# 求解利润最大化点（MR = MC）
optimal_Q = 30
optimal_P = price(optimal_Q)
optimal_TR = total_revenue(optimal_Q)
optimal_TC = total_cost(optimal_Q)
optimal_profit = optimal_TR - optimal_TC

# 完全竞争条件下的均衡产量
competitive_Q = 60  # 因为 P = MC => 50 - 0.5Q = 20 => Q = 60
competitive_P = price(competitive_Q)

# 消费者剩余（三角形面积）：0.5 * (最高愿付价格 - 实际价格) * 数量
CS = 0.5 * (50 - optimal_P) * optimal_Q

# 社会福利损失（DWL）：0.5 * (Q竞争 - Q垄断) * (P垄断 - MC)
DWL = 0.5 * (competitive_Q - optimal_Q) * (optimal_P - 20)

# 输出结果
print("利润最大化产量 Q* =", optimal_Q)
print("利润最大化价格 P* =", optimal_P)
print("利润 =", optimal_profit)
print("消费者剩余 CS =", CS)
print("社会福利损失 DWL =", DWL)

# 可视化
Q_range = np.linspace(0, 65, 300)
TR = total_revenue(Q_range)
MR = marginal_revenue(Q_range)
TC = total_cost(Q_range)
MC = [marginal_cost(q) for q in Q_range]
P_range = price(Q_range)
plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
plt.figure(figsize=(10,6))
plt.plot(Q_range, P_range, label='Demand Curve (P=50-0.5Q)', color='green')
plt.plot(Q_range, MR, label='MR (Marginal Revenue)', linestyle='--', color='blue')
plt.axhline(y=20, color='red', linestyle='--', label='MC = 20')
plt.axvline(x=optimal_Q, color='gray', linestyle=':', label='Monopoly Q* = 30')
plt.axvline(x=competitive_Q, color='gray', linestyle=':', label='Perfect Competition Q = 60')

# 填充 CS 区域（绿色）
plt.fill_between(Q_range, price(Q_range), optimal_P, where=(Q_range <= optimal_Q),
                 color='green', alpha=0.3, label='Consumer Surplus')

# 填充 DWL 区域（橙色）
plt.fill_between(Q_range, 20, price(Q_range), where=(Q_range >= optimal_Q) & (Q_range <= competitive_Q),
                 color='orange', alpha=0.5, label='Deadweight Loss')

plt.title("垄断下的利润最大化、消费者剩余与社会福利损失")
plt.xlabel("Q（产量）")
plt.ylabel("价格 / 收益 / 成本")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 想象一个面包店：
#
# 完全竞争：面包成本 20 元，卖 20 元，60 个人买到，满足所有需求。
# 垄断：成本仍是 20 元，但卖 35 元，只卖 30 个，30 个愿意付 20-35 元的人没买到。
# 损失：30 个面包未生产，消费者少享受，面包店少赚，社会整体“亏”了。
#  图形解释：
# 绿色填充：消费者剩余（CS）
#
# 橙色填充：社会福利损失（DWL）
#
# 灰线：表示垄断产量 vs 完全竞争产量的差异
#
# 红线 MC 与 蓝线 MR 交点：垄断利润最大化点
# 垄断市场分析：利润最大化与社会福利效率损失
#
# ---
#
# 1. 写出总收入 TR(Q) 和边际收入 MR(Q)
#
# (1) 总收入 TR(Q)
# 需求函数：Q = 100 - 2P
# 反解价格函数：
# Q = 100 - 2P => 2P = 100 - Q => P = (100 - Q) / 2 = 50 - Q/2
# 总收入 TR(Q) = P × Q：
# TR(Q) = (50 - Q/2) × Q = 50Q - Q^2 / 2
#
# (2) 边际收入 MR(Q)
# 边际收入是总收入对产量的导数：
# TR(Q) = 50Q - Q^2 / 2
# MR(Q) = dTR/dQ = 50 - Q
# 验证：MR 曲线斜率是 -1，需求曲线斜率是 dP/dQ = -1/2，MR 斜率是需求曲线的两倍，符合垄断市场规律。
#
# ---
#
# 2. 写出总成本 TC(Q) 和边际成本 MC(Q)
#
# (1) 总成本 TC(Q)
# 已知：TC(Q) = 20Q
#
# (2) 边际成本 MC(Q)
# 边际成本是总成本对产量的导数：
# TC(Q) = 20Q
# MC(Q) = dTC/dQ = 20
# 这表明边际成本是常数 20 元/单位。
#
# ---
#
# 3. 求利润最大化的产量 Q* 和价格 P*
#
# 利润最大化条件：在垄断市场中，利润最大化发生在 MR = MC。
# 已知：
# MR(Q) = 50 - Q
# MC(Q) = 20
# 令 MR = MC：
# 50 - Q = 20
# Q = 50 - 20 = 30
# 最优产量：Q* = 30
#
# 最优价格：代入需求函数 P = 50 - Q/2：
# P* = 50 - 30/2 = 50 - 15 = 35
# 结果：Q* = 30，P* = 35
#
# ---
#
# 4. 计算此时的利润
#
# 利润公式：π = TR - TC
# 计算总收入：
# TR(Q*) = P* × Q* = 35 × 30 = 1050
# 计算总成本：
# TC(Q*) = 20 × 30 = 600
# 计算利润：
# π = TR - TC = 1050 - 600 = 450
# 结果：利润 = 450 元
#
# ---
#
# 5. 判断市场是否有效率损失（社会福利角度）
#
# 效率损失（死重损失，Deadweight Loss, DWL）是垄断市场与完全竞争市场相比，因产量低于社会最优水平而损失的社会福利。
#
# (1) 完全竞争市场的均衡
# 在完全竞争市场，价格等于边际成本：P = MC。
# 已知 MC = 20，所以：
# P = 20
# 代入需求函数 Q = 100 - 2P：
# Q = 100 - 2 × 20 = 100 - 40 = 60
# 完全竞争结果：P_c = 20，Q_c = 60
#
# (2) 社会福利分析
# 社会福利 = 消费者剩余 (CS) + 生产者剩余 (PS)。
#
# 完全竞争市场：
# 需求曲线：P = 50 - Q/2，当 Q = 0，P = 50。
# 消费者剩余：需求曲线下的面积（三角形），从 P = 20 到 P = 50，Q = 60：
# CS_c = 1/2 × (50 - 20) × 60 = 1/2 × 30 × 60 = 900
# 生产者剩余：MC 以上、P 以下的面积。由于 MC = 20 = P，生产者剩余为 0（长期均衡）。
# 总福利：900 + 0 = 900
#
# 垄断市场：
# 产量 Q* = 30，价格 P* = 35。
# 消费者剩余：从 P = 35 到 P = 50，Q = 30：
# CS_m = 1/2 × (50 - 35) × 30 = 1/2 × 15 × 30 = 225
# 生产者剩余：利润（P - MC）× Q：
# PS_m = (35 - 20) × 30 = 15 × 30 = 450
# 总福利：225 + 450 = 675
#
# (3) 效率损失（死重损失）
# 死重损失是完全竞争福利与垄断福利的差：
# DWL = 900 - 675 = 225
#
# 图示解释：
# 死重损失是需求曲线和 MC 曲线之间的三角形区域，从 Q = 30 到 Q = 60。
# 高度：P = 35（垄断）到 P = 20（MC），差 = 15。
# 底边：Q = 60 - 30 = 30。
# 面积：DWL = 1/2 × (35 - 20) × (60 - 30) = 1/2 × 15 × 30 = 225
#
# (4) 结论
# 存在效率损失：垄断市场产量 Q* = 30 < Q_c = 60，价格 P* = 35 > P_c = 20，导致社会福利减少 225 元。
# 原因：垄断者限制产量以抬高价格，减少了本可实现的交易（从 30 到 60 单位），造成死重损失。
#
# ---
#
# 最终结果：
# 1. TR(Q) = 50Q - Q^2 / 2, MR(Q) = 50 - Q
# 2. TC(Q) = 20Q, MC(Q) = 20
# 3. Q* = 30, P* = 35
# 4. 利润 = 450 元
# 5. 存在效率损失，死重损失 = 225 元