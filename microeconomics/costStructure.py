import numpy as np
import matplotlib.pyplot as plt

# 参数设置
FC = 500  # 固定成本（元）
wage = 100  # 单位劳动成本（工资）
quantities = np.arange(1, 101)  # 产量范围：1 到 100

# 设置边际产出 MP，使用非线性递减函数
MP = 30 / (1 + 0.1 * quantities)  # MP 永远正数，且递减

# 计算边际成本 MC = w / MP
MC = wage / MP  # MP 越小，MC 越大

# 计算总成本 TC（累加 MC）+ 固定成本
TC = np.cumsum(MC) + FC

# 计算平均成本 AC = TC / Q
AC = TC / quantities

# 绘图
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))

plt.plot(quantities, TC, label='Total Cost (TC)', color='blue', linewidth=2)
plt.plot(quantities, AC, label='Average Cost (AC)', color='green', linewidth=2)
plt.plot(quantities, MC, label='Marginal Cost (MC)', color='red', linewidth=2)

plt.title("📊 成本分析图（边际产出递减）", fontsize=14)
plt.xlabel("产量（单位）", fontsize=12)
plt.ylabel("成本（元）", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 输出最优产量（最低 AC）
min_ac_index = np.argmin(AC)
optimal_quantity = quantities[min_ac_index]
optimal_ac = AC[min_ac_index]

print(f"✅ 最优产量：{optimal_quantity} 单位")
print(f"✅ 此时的平均成本（最低点）：{optimal_ac:.2f} 元")

#图表分析：
#总成本曲线（TC）：随着产量增加，总成本上升。

#平均成本曲线（AC）：一般呈 U 形，先下降后上升。最小值处即为最优产量。

#边际成本曲线（MC）：边际成本曲线通常与平均成本曲线交点处最小，这时的产量就是最优产量。