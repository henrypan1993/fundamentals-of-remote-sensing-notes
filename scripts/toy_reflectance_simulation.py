import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ========== 1. 定义简易反射率模拟函数 ==========
def simulate_reflectance(wavelength_nm, material_type):
    """
    A toy reflectance simulator for basic remote sensing understanding.
    wavelength_nm: input wavelength in nm
    material_type: 'vegetation', 'water', or 'soil'
    """
    if material_type == "vegetation":
        # 假设植被在NIR反射强，在Red吸收强
        if 600 <= wavelength_nm <= 700:  # Red
            return 0.1 + 0.05 * np.random.rand()
        elif 750 <= wavelength_nm <= 900:  # NIR
            return 0.5 + 0.2 * np.random.rand()
        else:
            return 0.2 + 0.1 * np.random.rand()

    elif material_type == "water":
        # 水体在所有波段反射率都低
        return 0.02 + 0.01 * np.random.rand()

    elif material_type == "soil":
        # 土壤随波长略微上升
        return 0.1 + (wavelength_nm / 2000) + 0.05 * np.random.rand()

    else:
        return None

# ========== 2. 测试典型波长输出表 ==========
materials = ["vegetation", "water", "soil"]
wavelengths = [650, 850]  # Red & NIR

results = []
for m in materials:
    for w in wavelengths:
        refl = simulate_reflectance(w, m)
        results.append((m, w, round(refl, 3)))

df = pd.DataFrame(results, columns=["Material", "Wavelength (nm)", "Simulated Reflectance"])
print("\nToy Reflectance Simulation Table:\n", df)

# ========== 3. 生成连续波长的光谱曲线 ==========
wavelengths_cont = np.linspace(400, 1000, 200)

def generate_spectrum(material_type):
    return [simulate_reflectance(w, material_type) for w in wavelengths_cont]

# 三类地物光谱
vegetation_spectrum = generate_spectrum("vegetation")
water_spectrum = generate_spectrum("water")
soil_spectrum = generate_spectrum("soil")

# ========== 4. 绘制光谱曲线 ==========
plt.figure(figsize=(8, 5))
plt.plot(wavelengths_cont, vegetation_spectrum, label="Vegetation", color="green", linewidth=2)
plt.plot(wavelengths_cont, water_spectrum, label="Water", color="blue", linewidth=2)
plt.plot(wavelengths_cont, soil_spectrum, label="Soil", color="sienna", linewidth=2)

plt.title("Simulated Reflectance Spectra", fontsize=14, fontweight="bold")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")
plt.ylim(0, 1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
