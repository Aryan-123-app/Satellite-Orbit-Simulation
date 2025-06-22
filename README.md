# 🚀 SATELLITE ORBIT SIMULATION DASHBOARD

![Dashboard Preview](satellite_dashboard.gif)

---

## 🌌 Overview

**Satellite Orbit Simulation Dashboard** is a cinematic, physics-accurate 3D visualization built using **Python**, **Matplotlib**, and **NumPy**.  
It simulates the motion of a satellite around Earth while dynamically displaying its:
- **3D orbit path**
- **Altitude and speed over time**
- **Telemetry dials (altitude, speed, clock)**
- **Real-time dashboard UI with LED-style fonts**

Ideal for:

✅ Educational demonstrations  
✅ Physics/astronomy learning  
✅ Visual storytelling and creative coding  

---

## ✨ Features

- 🌍 **3D Earth model with orbit path**
- 🛰 **Satellite trail & velocity vector**
- 📈 **Live graphs: Altitude (km) + Speed (km/s)**
- ⏱ **Rotating clock dial for elapsed time**
- 📊 **Polar-style dials for altitude + speed**
- 💾 **Automatic MP4 + GIF export of animation**
- 🎨 **Dark mode cinematic look with LED-style text (DS-Digital font)**

---

## 🛠 Requirements

✅ **Python 3.x**  
✅ **Libraries:**
```bash
pip install matplotlib numpy pillow
```
✅ **ffmpeg (for MP4 export)**  

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```
**Windows (with Chocolatey):**
```bash
choco install ffmpeg
```
✅ (Optional) **DS-Digital font file** (e.g., DS-DIGI.TTF) for LED-style text Download DS-Digital font

# ⚙️ How to Run
1️⃣ Place DS-DIGI.TTF in the project directory (or modify path in code).

2️⃣ Run the simulation:
```bash
python main.py
```
3️⃣ Watch the animation and check the generated files:

- satellite_dashboard.mp4
- satellite_dashboard.gif

# 📂 Project Structure
```graphql
satellite-orbit-simulator/
├── main.py                 # Main simulation code
├── DS-DIGI.TTF             # Font file (optional, for LED text style)
├── satellite_dashboard.mp4  # Example saved animation (MP4)
├── satellite_dashboard.gif  # Example saved animation (GIF)
└── README.md                # Project documentation
```
# 🎥 Example Preview
![Dashboard Preview](Figure1.png)

# 🔧 Customization
✅ Change simulation parameters in main.py:

```python
altitude = 500e3           # Initial altitude (meters)
eccentricity = 0.1         # Orbital eccentricity
inclination = 30           # Inclination (degrees)
mass_satellite = 1000      # Satellite mass (kg)
```
✅ Modify colors, dials, or graph properties to your taste!

✅ Adjust resolution / FPS of export:

```python
ani.save("satellite_dashboard.mp4", writer='ffmpeg', fps=30, dpi=150)
```

# 📌 Notes
**⚡ Performance:** Optimized for displays of 1920x1080 or higher.

**⚡ Export:** MP4 preferred for smoother output. GIFs may be large or lower FPS.

**⚡ Font:** If DS-Digital font is missing, code will default to system font.

# 💡 Credits
Developed by Aryan Patade

Made with ❤️ using Python, Matplotlib, NumPy
Font: DS-Digital

# 📬 Contact
**📧 Email:** aryanpatade8@gmail.com

**🌐 Website / Profile:** [your-website-or-profile-link]

# ⚡ Future Ideas
🚀 Add multiple satellites

🌑 Include lunar or planetary objects

🌠 Starfield with parallax

📊 Interactive controls (e.g., via ipywidgets or PyQt)

### Thanks for reading this file ! 




