---
title: Remote Sensing Fundamentals Notes
---

# Remote Sensing Fundamentals: Study Notes & Interactive Satellite Band Tools

This repository is a comprehensive resource for learning the fundamentals of remote sensing, combining detailed study notes with interactive and static visualization tools. It is designed for students, educators, and enthusiasts in remote sensing, earth observation, and geoscience.

---

## 🌟 Key Resources

- **📖 Online Study Notes (Highly Recommended)**  
  👉 [https://henrypan1993.github.io/fundamentals-of-remote-sensing-notes/](https://henrypan1993.github.io/fundamentals-of-remote-sensing-notes/)  
  A systematic and richly illustrated guide covering the electromagnetic spectrum, satellite sensors, atmospheric effects, and classic remote sensing cases.

- **📝 Local Study Materials**  
  See the `assets/` directory for all images and diagrams, or visit the online notes above for the best reading experience.

---

## 🌐 Interactive Online Demo

- **🛰️ Try the Interactive Dashboard Online:**  
  👉 [https://fundamentals-of-remote-sensing-notes.onrender.com/](https://fundamentals-of-remote-sensing-notes.onrender.com/)  
  Explore and compare Landsat 9 and Sentinel-2 spectral bands with atmospheric transmission windows directly in your browser.  
  **Features:**
  - Select different satellites to view their spectral bands and atmospheric windows
  - Hover over colored bands for detailed information
  - Works on both desktop and mobile browsers
  - No installation required

> Note: The free Render instance may take a few seconds to wake up if idle.

---

## 📁 Project Structure

```plaintext
/
├── README.md                # Project documentation (this file)
├── requirements.txt         # Python dependencies
├── app.py                   # Main entry point (if used)
├── assets/                  # All image and diagram resources
├── scripts/                 # Interactive and static visualization scripts
│   ├── landsat_sentinel_interactive.py      # Interactive Landsat/Sentinel band explorer (Plotly Dash)
│   ├── landsat_sentinel_static.py           # Static Landsat/Sentinel band comparison
│   ├── ahi_scanning_rhythm.py               # AHI scanning rhythm and imaging principle
│   ├── polarization_vector_projection.py    # Polarization vector projection demo
│   ├── toy_reflectance_simulation.py        # Simple reflectance simulation
│   └── electromagnetic_wave_components.py   # Electromagnetic wave component visualization
└── Procfile                  # Deployment configuration (for cloud platforms)
```

---

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the interactive dashboard locally:**
   ```bash
   python scripts/landsat_sentinel_interactive.py
   ```
   Then open [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser.

3. **Or try the online demo:**
   - Visit [https://fundamentals-of-remote-sensing-notes.onrender.com/](https://fundamentals-of-remote-sensing-notes.onrender.com/)

4. **Browse the study notes:**
   - For the best experience, visit the [Online Study Notes](https://henrypan1993.github.io/fundamentals-of-remote-sensing-notes/)
   - Or explore the images in the `assets/` directory

---

## 🛰️ Main Script Descriptions

- `landsat_sentinel_interactive.py`  
  Interactive visualization of Landsat 9 and Sentinel-2 bands and atmospheric windows (built with Plotly Dash).
- `landsat_sentinel_static.py`  
  Generates static comparison plots of Landsat/Sentinel bands and atmospheric windows.
- `ahi_scanning_rhythm.py`  
  Demonstrates the scanning rhythm and imaging principle of the Advanced Himawari Imager (AHI).
- `polarization_vector_projection.py`  
  Visualizes spatial projection of polarization vectors.
- `toy_reflectance_simulation.py`  
  Simple simulation of surface reflectance.
- `electromagnetic_wave_components.py`  
  Visualizes components of electromagnetic waves.

---

## 👥 Who Is This For?

- Students and educators in remote sensing, earth observation, and geoscience
- Anyone interested in satellite data, the electromagnetic spectrum, and atmospheric science
- Self-learners seeking both theoretical knowledge and practical visualization tools

---

## 🤝 Contributing & Feedback

Contributions, corrections, and suggestions are welcome!
- Please open an Issue or Pull Request for any feedback or improvements.
- You can also leave comments via the [Online Study Notes](https://henrypan1993.github.io/fundamentals-of-remote-sensing-notes/) page.

---

## 📄 License

[MIT License](LICENSE)  
If the LICENSE file is missing, please add or specify your preferred license.

---

**Enjoy exploring the world of remote sensing!** 