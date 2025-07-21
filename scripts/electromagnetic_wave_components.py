import numpy as np
import matplotlib.pyplot as plt

# 数据
x = np.linspace(0, 2 * np.pi, 1000)
frequency = 1  # 单个周期
amplitude = 1
y = amplitude * np.sin(x)

# 绘制
plt.figure(figsize=(10, 4))
plt.plot(x, y, color='#007acc', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# 标注振幅（垂直）
plt.annotate("Amplitude (A)", xy=(0, amplitude), xytext=(0.3, 1.2),
             arrowprops=dict(arrowstyle="->", color="#2ecc71", lw=2),
             color="#2ecc71", fontsize=11, fontweight='bold')

# 标注波长（水平方向：两个波峰之间）
plt.annotate("", xy=(0, -1.2), xytext=(2 * np.pi, -1.2),
             arrowprops=dict(arrowstyle="<->", color="#ff4d4d", lw=2))
plt.text(np.pi, -1.4, "Wavelength (λ)", ha='center', color="#ff4d4d", fontsize=11, fontweight='bold')

# 波峰与波谷文字
plt.text(np.pi/2, 1.1, "Crest", ha='center', color="#1f77b4", fontsize=10, fontweight='bold')
plt.text(3*np.pi/2, -1.3, "Trough", ha='center', color="#1f77b4", fontsize=10, fontweight='bold')

# 注释
plt.text(5, 1.0, "Frequency (f): Number of crests per second", fontsize=9, color="#333333")
plt.text(5, 0.7, "Energy ∝ f   |   Intensity ∝ A²", fontsize=9, color="#333333")

plt.title("Electromagnetic Wave Components", fontsize=14, fontweight="bold")
plt.xlabel("Distance / Time")
plt.ylabel("Amplitude")
plt.ylim(-1.6, 1.6)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.tight_layout()
plt.show()
