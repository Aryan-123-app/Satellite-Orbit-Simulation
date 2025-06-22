import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

# 🌍 Constants
G = 6.67430e-11
M = 5.972e24
R_earth = 6371000
mass_satellite = 1000

# 🛰 Simulation parameters
altitude = 500e3
eccentricity = 0.1
inclination = 30
dt = 10.0
num_steps = 1500

r0 = R_earth + altitude
a = r0 / (1 - eccentricity)
v0 = np.sqrt(G * M * (2 / r0 - 1 / a))

inc_rad = np.radians(inclination)
pos = np.array([r0 * np.cos(inc_rad), 0, r0 * np.sin(inc_rad)])
vel = np.array([0, v0, 0])

# Load DS-Digital font
led_font = font_manager.FontProperties(fname='DS-DIGI.TTF')

positions = [pos.copy()]
velocities = [vel.copy()]
times = [0]
altitudes = []
speeds = []
energies = []

def step(pos, vel, dt):
    r = np.linalg.norm(pos)
    acc = -G * M / r**3 * pos
    vel += acc * dt
    pos += vel * dt
    return pos, vel

for i in range(num_steps):
    pos, vel = step(pos, vel, dt)
    positions.append(pos.copy())
    velocities.append(vel.copy())
    times.append((i+1)*dt)
    r = np.linalg.norm(pos)
    altitudes.append((r - R_earth)/1000)
    speeds.append(np.linalg.norm(vel)/1000)
    KE = 0.5 * mass_satellite * np.linalg.norm(vel)**2
    PE = -G * M * mass_satellite / r
    energies.append(KE + PE)

positions = np.array(positions)
velocities = np.array(velocities)

# 🌌 Plot setup
fig = plt.figure(figsize=(12,8))
fig.patch.set_facecolor('black')
fig.suptitle("Satellite Orbit Simulation Dashboard", color='cyan', fontsize=22 ,fontproperties=led_font)

gs = fig.add_gridspec(2, 2, height_ratios=[2, 1])

# 3D view
ax3d = fig.add_subplot(gs[0,:], projection='3d')
ax3d.set_facecolor('black')
ax3d.set_xticks([])
ax3d.set_yticks([])
ax3d.set_zticks([])

max_extent = np.max(np.abs(positions)) * 1.2
ax3d.set_xlim(-max_extent, max_extent)
ax3d.set_ylim(-max_extent, max_extent)
ax3d.set_zlim(-max_extent, max_extent)
ax3d.set_box_aspect([1,1,1])

ax3d.set_title("Cinematic 3D Satellite Orbit", color='yellow',fontproperties=led_font, fontsize=20)

# Stars
num_stars = 500
stars_x = np.random.uniform(-max_extent, max_extent, num_stars)
stars_y = np.random.uniform(-max_extent, max_extent, num_stars)
stars_z = np.random.uniform(-max_extent, max_extent, num_stars)
ax3d.scatter(stars_x, stars_y, stars_z, color='white', s=0.5, alpha=0.6)

# Earth
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = R_earth * np.cos(u) * np.sin(v)
y = R_earth * np.sin(u) * np.sin(v)
z = R_earth * np.cos(v)
ax3d.plot_surface(x, y, z, color='#1E90FF', alpha=0.3)

# Orbit + satellite
ax3d.plot(positions[:,0], positions[:,1], positions[:,2], color='#FF5733', lw=1)
sat_dot, = ax3d.plot([], [], [], 'o', color='#00FFAA', markersize=6)
trail, = ax3d.plot([], [], [], 'o', color='#00FFAA', alpha=0.5, markersize=3)
velocity_arrow = None

# Clock polar
ax_clock = fig.add_axes([0.4, 0.05, 0.2, 0.2], polar=True, facecolor='black')
clock_hand, = ax_clock.plot([], [], color='cyan', lw=3)
ax_clock.set_xticks([]); ax_clock.set_yticks([]); ax_clock.set_rlim(0,1)

# Altitude dial
ax_alt_dial = fig.add_axes([0.1, 0.05, 0.2, 0.2], polar=True, facecolor='black')
alt_bar = ax_alt_dial.bar(0, 1, width=0.1, color='blue')
ax_alt_dial.set_xticks([]); ax_alt_dial.set_yticks([]); ax_alt_dial.set_rlim(0,1)

# Speed dial
ax_speed_dial = fig.add_axes([0.7, 0.05, 0.2, 0.2], polar=True, facecolor='black')
speed_bar = ax_speed_dial.bar(0, 1, width=0.1, color='orange')
ax_speed_dial.set_xticks([]); ax_speed_dial.set_yticks([]); ax_speed_dial.set_rlim(0,1)


# Altitude graph
ax_alt = fig.add_subplot(gs[1,0])
line_alt, = ax_alt.plot([], [], color='blue', label='Altitude')
ax_alt.set_xlim(0, times[-1]/60)
ax_alt.set_ylim(0, max(altitudes)*1.1)
ax_alt.set_xlabel("Time (minutes)", color='white')
ax_alt.set_ylabel("Altitude (km)", color='white')
ax_alt.set_title("Satellite Altitude Over Time", color='violet',fontproperties=led_font, fontsize=14 )
ax_alt.legend(loc="upper right", facecolor='black', edgecolor='none', labelcolor='white')
ax_alt.tick_params(axis='x', colors='green')
ax_alt.tick_params(axis='y', colors='green')

# Speed graph
ax_speed = fig.add_subplot(gs[1,1])
line_speed, = ax_speed.plot([], [], color='orange', label='Speed')
ax_speed.set_xlim(0, times[-1]/60)
ax_speed.set_ylim(0, max(speeds)*1.1)
ax_speed.set_xlabel("Time (minutes)", color='white')
ax_speed.set_ylabel("Speed (km/s)", color='white')
ax_speed.set_title("Satellite Speed Over Time", color='red', fontproperties=led_font, fontsize=14)
ax_speed.legend(loc="upper right", facecolor='black', edgecolor='none', labelcolor='white')
ax_speed.tick_params(axis='x', colors='orange')
ax_speed.tick_params(axis='y', colors='orange')

# Info overlay
info_text = ax3d.text2D(
    0.05, 0.95, '', transform=ax3d.transAxes, color='lime', fontproperties=led_font,
    bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', boxstyle='round' )
)

# Animation config
frame_skip = 10
trail_len = 50

def update(frame_idx):
    global velocity_arrow
    frame = frame_idx * frame_skip
    if frame >= len(positions):
        frame = len(positions) - 1

    x, y, z = positions[frame]
    vx, vy, vz = velocities[frame]

    sat_dot.set_data([x], [y])
    sat_dot.set_3d_properties([z])

    start = max(0, frame - trail_len)
    trail.set_data(positions[start:frame,0], positions[start:frame,1])
    trail.set_3d_properties(positions[start:frame,2])

    if velocity_arrow:
        velocity_arrow.remove()
    velocity_arrow = ax3d.quiver(x, y, z, vx, vy, vz, length=1000, color='green')

    t_min = np.array(times[:frame+1])/60
    line_alt.set_data(t_min, altitudes[:frame+1])
    line_speed.set_data(t_min, speeds[:frame+1])

    info_text.set_text(f"t={times[frame]/60:.1f} min | Alt={altitudes[frame]:.1f} km | Speed={speeds[frame]:.2f} km/s")

    ax3d.view_init(elev=30, azim=frame_idx * 0.2)

    return sat_dot, trail, velocity_arrow, line_alt, line_speed, info_text

ani = animation.FuncAnimation(
    fig, update,
    frames=range(0, len(positions)//frame_skip),
    interval=10,
    blit=False
)

# Save animation
print("Saving animation...")
try:
    ani.save("satellite_dashboard.mp4", writer='ffmpeg', fps=30, dpi=150)
    print("Saved as satellite_dashboard.mp4")
except Exception as e:
    print("MP4 save failed:", e)
    print("Trying GIF fallback...")
    try:
        ani.save("satellite_dashboard.gif", writer='pillow', fps=20)
        print("Saved as satellite_dashboard.gif")
    except Exception as e2:
        print("GIF save failed:", e2)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
