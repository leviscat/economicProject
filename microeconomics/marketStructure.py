import matplotlib.pyplot as plt

# 市场结构对比表格数据
structures = ['完全竞争', '垄断竞争', '寡头', '垄断']
entry_barriers = [1, 2, 4, 5]       # 市场进入难度（1-5）
product_diff = [1, 3, 4, 5]         # 产品差异化程度（1-5）
price_control = [1, 2, 4, 5]        # 厂商对价格的控制力（1-5）
num_firms = [5, 4, 2, 1]            # 市场中的厂商数量（1-5）

x = range(len(structures))
bar_width = 0.2

plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制柱状图
ax.bar([i - 1.5*bar_width for i in x], entry_barriers, width=bar_width, label='进入壁垒')
ax.bar([i - 0.5*bar_width for i in x], product_diff, width=bar_width, label='产品差异化')
ax.bar([i + 0.5*bar_width for i in x], price_control, width=bar_width, label='价格控制力')
ax.bar([i + 1.5*bar_width for i in x], num_firms, width=bar_width, label='厂商数量（越大越多）')

# 设置图例和标签
ax.set_title("四种市场结构对比图", fontsize=16)
ax.set_ylabel("强度（1=最低，5=最高）", fontsize=12)
ax.set_xticks(list(x))
ax.set_xticklabels(structures, fontsize=12)
ax.legend()
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()