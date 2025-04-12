def price_elasticity():
    print("\n🧮 [价格弹性] Price Elasticity of Demand")
    P1 = float(input("原始价格 P1: "))
    P2 = float(input("新价格 P2: "))
    Q1 = float(input("原始需求量 Q1: "))
    Q2 = float(input("新需求量 Q2: "))

    delta_Q = (Q2 - Q1) / ((Q1 + Q2) / 2)
    delta_P = (P2 - P1) / ((P1 + P2) / 2)
    Ep = delta_Q / delta_P

    print(f"\n📊 价格弹性 Ep = {Ep:.2f}")
    if abs(Ep) > 1:
        print("→ 富有弹性（Elastic）：消费者对价格变化敏感")
    elif abs(Ep) < 1:
        print("→ 缺乏弹性（Inelastic）：消费者对价格变化不敏感")
    else:
        print("→ 单位弹性（Unit Elastic）：价格变化和需求变化幅度一致")

def income_elasticity():
    print("\n🧮 [收入弹性] Income Elasticity of Demand")
    Y1 = float(input("原始收入 Y1: "))
    Y2 = float(input("新收入 Y2: "))
    Q1 = float(input("原始需求量 Q1: "))
    Q2 = float(input("新需求量 Q2: "))

    delta_Q = (Q2 - Q1) / ((Q1 + Q2) / 2)
    delta_Y = (Y2 - Y1) / ((Y1 + Y2) / 2)
    Ey = delta_Q / delta_Y

    print(f"\n📊 收入弹性 Ey = {Ey:.2f}")
    if Ey > 0:
        if Ey > 1:
            print("→ 奢侈品（Luxury Good）")
        else:
            print("→ 必需品（Necessity）")
    else:
        print("→ 劣等品（Inferior Good）")

def cross_price_elasticity():
    print("\n🧮 [交叉价格弹性] Cross-Price Elasticity of Demand")
    Py1 = float(input("商品Y原始价格 Py1: "))
    Py2 = float(input("商品Y新价格 Py2: "))
    Qx1 = float(input("商品X原始需求量 Qx1: "))
    Qx2 = float(input("商品X新需求量 Qx2: "))

    delta_Qx = (Qx2 - Qx1) / ((Qx1 + Qx2) / 2)
    delta_Py = (Py2 - Py1) / ((Py1 + Py2) / 2)
    Ec = delta_Qx / delta_Py

    print(f"\n📊 交叉价格弹性 Ec = {Ec:.2f}")
    if Ec > 0:
        print("→ 替代品（Substitutes）")
    elif Ec < 0:
        print("→ 互补品（Complements）")
    else:
        print("→ 无明显关系")

def main():
    while True:
        print("\n===== 微观经济学弹性计算器 =====")
        print("1️⃣ 价格弹性")
        print("2️⃣ 收入弹性")
        print("3️⃣ 交叉价格弹性")
        print("0️⃣ 退出")
        choice = input("请选择要计算的弹性类型（输入数字）: ")

        if choice == '1':
            price_elasticity()
        elif choice == '2':
            income_elasticity()
        elif choice == '3':
            cross_price_elasticity()
        elif choice == '0':
            print("👋 再见，欢迎下次练习！")
            break
        else:
            print("⚠️ 无效输入，请输入 1, 2, 3 或 0")

# 启动程序
main()
