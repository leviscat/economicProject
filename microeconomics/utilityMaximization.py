import matplotlib.pyplot as plt
import numpy as np

def optimal_combination(budget, apple_price, banana_price, apple_mu, banana_mu):
    max_utility = 0
    best_combination = (0, 0)
    combinations = []
    utilities = []

    # 遍历所有可行的苹果和香蕉数量组合
    for apples in range(len(apple_mu) + 1):      # 包括0个
        for bananas in range(len(banana_mu) + 1):
            total_cost = apples * apple_price + bananas * banana_price
            if total_cost <= budget:
                # 总效用 = 购买数量以内的所有边际效用之和
                total_utility = sum(apple_mu[:apples]) + sum(banana_mu[:bananas])
                combinations.append((apples, bananas))
                utilities.append(total_utility)

                # 判断是否为当前最大效用
                if total_utility > max_utility:
                    max_utility = total_utility
                    best_combination = (apples, bananas)

    return best_combination, max_utility, combinations, utilities


def plot_utility_space(combinations, utilities, best_combination):
    plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
    fig, ax = plt.subplots(figsize=(10, 6))
    max_index = combinations.index(best_combination)

    # 画所有组合的点
    for i, ((x, y), u) in enumerate(zip(combinations, utilities)):
        color = 'red' if (x, y) == best_combination else 'blue'
        ax.scatter(x, y, s=u*5, color=color, alpha=0.6)
        ax.text(x + 0.1, y + 0.1, f'{u}', fontsize=9)

    # 设置图形信息
    ax.set_title("不同苹果和香蕉组合下的总效用", fontsize=14)
    ax.set_xlabel("苹果数量", fontsize=12)
    ax.set_ylabel("香蕉数量", fontsize=12)
    ax.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 初始化参数
    budget = 10
    apple_price = 2
    banana_price = 1

    # 边际效用表（最多买5个）
    apple_mu = [20, 16, 12, 8, 4]
    banana_mu = [12, 10, 8, 6, 4]

    # 找最优组合
    best_combination, max_utility, combinations, utilities = optimal_combination(
        budget, apple_price, banana_price, apple_mu, banana_mu)

    # 输出结果
    print(f"💡 最优购买组合：苹果 {best_combination[0]} 个，香蕉 {best_combination[1]} 个")
    print(f"📈 最大总效用：{max_utility}")

    # 可视化所有组合
    plot_utility_space(combinations, utilities, best_combination)
