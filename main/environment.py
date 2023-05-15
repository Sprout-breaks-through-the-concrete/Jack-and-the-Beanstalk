import logging

"""
ENVIRONMENT CONFIG
"""
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600
USE_STROKE = False
LOG_DIR = './log'

"""
MAIN CONFIG
"""
STAR_COLOR = color(255,255,0)

PHASE_1 = 600
PHASE_2 = 700
PHASE_3 = 800

GROW_SPEED = 3

"""
ORDER:
    DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL  
"""
LOG_LEVEL = logging.DEBUG