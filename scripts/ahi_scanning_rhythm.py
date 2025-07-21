import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制Full Disk观测（用大圆表示地球）
full_disk = patches.Circle((0.5, 0.5), 0.45, edgecolor="blue", facecolor="lightblue", alpha=0.3, label="Full Disk Scan")
ax.add_patch(full_disk)

# 绘制Target Area 1 & 2（用方形表示高频区域）
target1 = patches.Rectangle((0.65, 0.65), 0.1, 0.1, edgecolor="red", facecolor="orange", alpha=0.6, label="Target Area 1")
target2 = patches.Rectangle((0.25, 0.55), 0.08, 0.08, edgecolor="darkred", facecolor="yellow", alpha=0.6, label="Target Area 2")
ax.add_patch(target1)
ax.add_patch(target2)

# 添加箭头表示扫描跳跃
ax.annotate("", xy=(0.7, 0.7), xytext=(0.5, 0.5),
            arrowprops=dict(arrowstyle="->", color="red", lw=2))
ax.annotate("", xy=(0.3, 0.6), xytext=(0.5, 0.5),
            arrowprops=dict(arrowstyle="->", color="red", lw=2))

# 添加文本说明
ax.text(0.5, 0.05, "AHI Scanning Cycle:\nFull Disk every 10 min\n+ Target Areas every 2.5 min", 
        ha="center", fontsize=10, color="black", bbox=dict(facecolor="white", alpha=0.7))

# 调整图形显示范围与样式
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis("off")
plt.legend(loc="upper left")
plt.title("Advanced Himawari Imager (AHI) Scanning Pattern", fontsize=12)

plt.show()
