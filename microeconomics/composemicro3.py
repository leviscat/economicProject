# 由于执行状态被重置，我们需要重新导入库并运行全部代码

import numpy as np
import matplotlib.pyplot as plt

# 定义需求、边际收益、边际成本、供给函数
def price(Q):
    return 50 - 0.5 * Q  # 需求函数 P(Q)

def marginal_revenue(Q):
    return 50 - Q  # 边际收益 MR

def marginal_cost(Q):
    return 20 + 0.1 * Q  # 非线性边际成本 MC(Q)

def demand(P):
    return 100 - 2 * P  # 反函数：根据价格求需求量 Qd

def supply(P):
    return max((P - 10) * 2, 0)  # 假设供给起点为P=10，供给斜率为2（简化模型）

# 定义税收和补贴影响
tax = 5      # 每单位商品征收5元税
subsidy = 4  # 每单位商品补贴4元

# 求最优点
Q_range = np.linspace(0, 80, 400)
P_range = price(Q_range)
MR_range = marginal_revenue(Q_range)
MC_range = marginal_cost(Q_range)

# 政府干预价格
price_ceiling = 25
price_floor = 35

# 上限与下限对应供需
Qd_ceiling = demand(price_ceiling)
Qs_ceiling = supply(price_ceiling)

Qd_floor = demand(price_floor)
Qs_floor = supply(price_floor)

# 考虑税收后的边际成本（抬高）
MC_tax = marginal_cost(Q_range) + tax

# 考虑补贴后的边际成本（降低）
MC_subsidy = marginal_cost(Q_range) - subsidy

# 画图
plt.figure(figsize=(12, 7))
plt.plot(Q_range, P_range, label='需求曲线 (P=50-0.5Q)', color='green')
plt.plot(Q_range, MR_range, '--', label='边际收益 MR', color='blue')
plt.plot(Q_range, MC_range, label='边际成本 MC', color='red')
plt.plot(Q_range, MC_tax, label='征税后 MC+tax', linestyle='--', color='brown')
plt.plot(Q_range, MC_subsidy, label='补贴后 MC-subsidy', linestyle='--', color='purple')

# 垂线表示供需差异
plt.axhline(price_ceiling, color='orange', linestyle='-', label=f'价格上限 = ¥{price_ceiling}')
plt.scatter([Qd_ceiling], [price_ceiling], color='orange', label='上限下需求 Qd')
plt.scatter([Qs_ceiling], [price_ceiling], color='darkorange', label='上限下供给 Qs')
plt.fill_betweenx([0, price_ceiling], Qs_ceiling, Qd_ceiling, color='orange', alpha=0.3, label='短缺 Shortage')

plt.axhline(price_floor, color='purple', linestyle='-', label=f'价格下限 = ¥{price_floor}')
plt.scatter([Qd_floor], [price_floor], color='purple', label='下限下需求 Qd')
plt.scatter([Qs_floor], [price_floor], color='mediumpurple', label='下限下供给 Qs')
plt.fill_betweenx([0, price_floor], Qd_floor, Qs_floor, color='purple', alpha=0.3, label='过剩 Surplus')

plt.title("政府干预市场：价格上限、下限、税收与补贴影响", fontsize=14)
plt.xlabel("Q（产量）", fontsize=12)
plt.ylabel("价格", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True)
plt.tight_layout()
plt.show()


# 1. 绿色实线：需求曲线
# P = 50 - 0.5Q
# 表示每多生产一单位商品，消费者愿意支付的价格会降低（即边际效用递减）。
#
# 2. 蓝色虚线：边际收益（MR）
# MR = 50 - Q
# 在垄断市场中，边际收益曲线比需求曲线更陡，且总是在其下方。
# 表示卖出一单位商品所增加的总收益。
#
# 3. 红色实线：边际成本（MC）
# MC = 20 + 0.1Q
# 边际成本递增，即生产越多，每多生产一单位的成本越高。
#
# 4. 棕色虚线：征税后的边际成本
# MC + tax
# 当每件商品征税5元时，企业的每单位边际成本上升5元，曲线整体向上平移。
# 意义：
# 税收会减少生产数量、提高市场价格（对消费者不利）。
# 社会福利损失会增加。
#
# 5. 紫色虚线：补贴后的边际成本
# MC - subsidy
# 当政府补贴每件商品4元时，企业的边际成本下降，曲线整体下移。
# 意义：
# 鼓励企业多生产，消费者以更低价格买到更多商品。
# 补贴有助于正外部性商品的推广（比如疫苗、教育等）。
#
# 6. 橙色线段 & 区域：价格上限（Price Ceiling） = ¥25
# 横线代表政府规定的最高价格。
# 在上限下：
# 需求量 Qd 增加
# 供给量 Qs 减少
# 出现供不应求（Shortage，图中填充的橙色区域）
# 意义：
# 常用于控制租金、药品等基本生活品价格。
# 可能导致黑市、配给制等现象。
#
# 7. 紫色线段 & 区域：价格下限（Price Floor） = ¥35
# 横线代表政府规定的最低价格。
# 在下限下：
# 供给量 Qs 增加
# 需求量 Qd 减少
# 出现供过于求（Surplus，图中紫色区域）
# 意义：
# 常用于保护农民、最低工资等。
# 可能造成剩余产品积压、资源浪费。
#
# 总结：政府干预的四种方式影响
# 类型       效果            社会后果
# 价格上限   抑制价格上涨    短缺、黑市风险
# 价格下限   提高收入底线    过剩、资源浪费
# 税收       降低供给        减少交易、效率损失
# 补贴       增加供给        提高生产、财政压力

