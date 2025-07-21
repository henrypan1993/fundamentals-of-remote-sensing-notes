# Remote Sensing Fundamentals: Learning Notes & Interactive Satellite Explorer

This repository is a comprehensive resource for learning the fundamentals of remote sensing, combining detailed study notes with interactive satellite band visualization tools.

---

## Project Structure

```plaintext
/
├── README.md
├── requirements.txt
├── notes/
│   └── Fundamentals_of_Remote_Sensing.md
├── scripts/
│   ├── landsat_sentinel_interactive.py
│   ├── landsat_sentinel_static.py
│   ├── ahi_scanning_rhythm.py
│   ├── polarization_vector_projection.py
│   ├── toy_reflectance_simulation.py
│   └── electromagnetic_wave_components.py
└── Learning Notes Fundamentals of Remote Sensing.assets/
    └── ... (all image assets)
```

---

## Highlights

- **📝 In-depth Learning Notes:**  
  - `notes/Fundamentals_of_Remote_Sensing.md`  
  - Covers electromagnetic spectrum, satellite sensors, atmospheric effects, and more.
  - Richly illustrated with custom diagrams and annotated images.

- **🛰️ Interactive Satellite Band Explorer:**  
  - `scripts/landsat_sentinel_interactive.py`  
  - Visualizes and compares Landsat 9 & Sentinel-2 spectral bands with atmospheric transmission windows.
  - Built with Plotly Dash for browser-based interactivity.

- **🛠️ Additional Scripts:**  
  - Static visualizations, polarization simulation, reflectance modeling, and more for hands-on learning.

---

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the interactive dashboard:**
   ```bash
   python scripts/landsat_sentinel_interactive.py
   ```
   Then open [http://127.0.0.1:8050](http://127.0.0.1:8050) in your browser.

3. **Browse the learning notes:**
   - Open `notes/Fundamentals_of_Remote_Sensing.md` with any Markdown reader.

---

## Who is this for?

- Students and educators in remote sensing, earth observation, and geoscience.
- Anyone interested in satellite data, electromagnetic spectrum, and atmospheric science.
- Learners seeking both theoretical knowledge and practical, visual tools.

---

## Contributing

Contributions, corrections, and suggestions are welcome!  
Feel free to open issues or submit pull requests.

---

## License

[MIT License](LICENSE) (or specify your license here)

---

**Enjoy exploring the world of remote sensing!** 