import matplotlib.pyplot as plt

# 坐标
plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# 电场矢量
plt.arrow(0, 0, 2, 3, head_width=0.1, head_length=0.15, fc='red', ec='red', linewidth=2)
plt.text(2.1, 3.1, "E (Electric field)", color='red', fontsize=10, fontweight='bold')

# 水平(H)投影
plt.arrow(0, 0, 2, 0, head_width=0.08, head_length=0.1, fc='blue', ec='blue', linestyle='--', linewidth=2)
plt.text(2.1, -0.2, "H-component", color='blue', fontsize=10)

# 垂直(V)投影
plt.arrow(0, 0, 0, 3, head_width=0.08, head_length=0.1, fc='green', ec='green', linestyle='--', linewidth=2)
plt.text(0.1, 3.1, "V-component", color='green', fontsize=10)

# 辅助线
plt.plot([2, 2], [0, 3], color='gray', linestyle=':', linewidth=1)
plt.plot([0, 2], [3, 3], color='gray', linestyle=':', linewidth=1)

plt.title("Polarization = Vector Projection", fontsize=14, fontweight='bold')
plt.xlim(-0.5, 3)
plt.ylim(-0.5, 3.5)
plt.xlabel("Horizontal (H) direction")
plt.ylabel("Vertical (V) direction")
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()
