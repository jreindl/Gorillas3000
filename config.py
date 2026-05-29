# ── Gorillas 3000 – Konfiguration ─────────────────────────────────────────────

# Fenster
SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720
FPS           = 60
TITLE         = "Gorillas 3000"

# Physik
GRAVITY       = 9.81          # m/s²
PHYSICS_SCALE = 10            # Pixel pro Meter
TIME_STEP     = 1 / FPS       # Sekunden pro Tick

# Wind (optional)
WIND_ENABLED  = True
WIND_MAX      = 5.0           # maximale Windstärke (m/s), kann negativ sein

# Welt / Skyline
MIN_BUILDINGS   = 8
MAX_BUILDINGS   = 12
MIN_BLDG_WIDTH  = 60
MAX_BLDG_WIDTH  = 110
MIN_BLDG_HEIGHT = 80
MAX_BLDG_HEIGHT = 380
GROUND_Y        = SCREEN_HEIGHT - 40   # Y-Koordinate des Bodens (Pixel)

# Gorilla
GORILLA_WIDTH   = 40
GORILLA_HEIGHT  = 50
GORILLA_RADIUS  = 20          # Kollisionsradius (Pixel)

# Projektil
PROJECTILE_RADIUS = 8

# Farben  (R, G, B)
COLOR_SKY        = (15,  20,  40)
COLOR_GROUND     = (40,  35,  30)
COLOR_BUILDING   = (55,  60,  75)
COLOR_WINDOW_ON  = (255, 240, 150)
COLOR_WINDOW_OFF = (30,  35,  50)
COLOR_GORILLA_1  = (220,  80,  60)
COLOR_GORILLA_2  = (60,  140, 220)
COLOR_PROJECTILE = (255, 200,  50)
COLOR_EXPLOSION  = (255, 120,   0)
COLOR_HUD_BG     = (0,    0,   0, 160)   # RGBA (für Surface mit alpha)
COLOR_HUD_TEXT   = (230, 230, 230)
COLOR_HUD_ACCENT = (255, 200,  50)

# HUD
HUD_FONT_SIZE_LARGE  = 28
HUD_FONT_SIZE_SMALL  = 18

# Spielmodi / Punkte
MAX_ROUNDS = 5                # Runden bis Spielende (0 = unbegrenzt)
