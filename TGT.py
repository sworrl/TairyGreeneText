#!/usr/bin/env python3

import sys
import os
import random
import argparse
import time  # For potential banner cycling delay
import subprocess
import re

SCRIPT_NAME_HUMAN = "Tairy Greene Text"
SCRIPT_NAME_COMMAND = "TGT"
INSTALL_PATH = "/usr/local/bin/tgt"
SCRIPT_VERSION = "2.0"
SCRIPT_CODENAME = "Maximum Yelling!"
RESET_COLOR = "\033[0m"

THEMES = {
    "fire": ["\033[38;5;196m", "\033[38;5;202m", "\033[38;5;208m", "\033[38;5;214m", "\033[38;5;220m", "\033[38;5;226m", "\033[38;5;232m"],
    "ice": ["\033[38;5;81m", "\033[38;5;87m", "\033[38;5;111m", "\033[38;5;117m", "\033[38;5;153m", "\033[38;5;159m", "\033[38;5;231m"],
    "earth": ["\033[38;5;28m", "\033[38;5;34m", "\033[38;5;40m", "\033[38;5;100m", "\033[38;5;130m", "\033[38;5;136m", "\033[38;5;172m"],
    "rainbow": ["\033[38;5;196m", "\033[38;5;208m", "\033[38;5;226m", "\033[38;5;46m", "\033[38;5;21m", "\033[38;5;93m", "\033[38;5;99m"],
    "forest": ["\033[38;5;22m", "\033[38;5;28m", "\033[38;5;34m", "\033[38;5;40m", "\033[38;5;46m", "\033[38;5;76m", "\033[38;5;118m"],
    "ocean": ["\033[38;5;27m", "\033[38;5;33m", "\033[38;5;39m", "\033[38;5;63m", "\033[38;5;81m", "\033[38;5;86m", "\033[38;5;117m"],
    "seafoam": ["\033[38;5;120m", "\033[38;5;87m", "\033[38;5;159m", "\033[38;5;153m", "\033[38;5;117m", "\033[38;5;231m"],
    "usa": ["\033[38;5;196m", "\033[38;5;15m", "\033[38;5;21m", "\033[38;5;197m", "\033[38;5;231m", "\033[38;5;199m"],
    "easter": ["\033[38;5;213m", "\033[38;5;195m", "\033[38;5;223m", "\033[38;5;111m", "\033[38;5;229m", "\033[38;5;217m"],
    "fart": ["\033[38;5;130m", "\033[38;5;106m", "\033[38;5;226m", "\033[38;5;101m", "\033[38;5;178m", "\033[38;5;136m"],
    "sprite": ["\033[38;5;118m", "\033[38;5;15m", "\033[38;5;46m", "\033[38;5;121m", "\033[38;5;119m", "\033[38;5;229m"],
    "pepsi": ["\033[38;5;4m", "\033[38;5;15m", "\033[38;5;9m", "\033[38;5;15m", "\033[38;5;4m", "\033[38;5;9m"],
    "windows 98": ["\033[38;5;27m", "\033[38;5;33m", "\033[38;5;39m", "\033[38;5;45m", "\033[38;5;51m", "\033[38;5;57m", "\033[38;5;63m"],
    "windows xp": ["\033[38;5;27m", "\033[38;5;15m", "\033[38;5;46m", "\033[38;5;21m", "\033[38;5;81m", "\033[38;5;118m", "\033[38;5;39m"],
    "macos": ["\033[38;5;15m", "\033[38;5;8m", "\033[38;5;7m", "\033[38;5;109m", "\033[38;5;15m", "\033[38;5;248m", "\033[38;5;109m"],
    "xbox": ["\033[38;5;46m", "\033[38;5;15m", "\033[38;5;28m", "\033[38;5;46m", "\033[38;5;118m", "\033[38;5;76m"],
    "playstation": ["\033[38;5;4m", "\033[38;5;15m", "\033[38;5;6m", "\033[38;5;12m", "\033[38;5;4m", "\033[38;5;15m", "\033[38;5;6m"],
    "bigfoot": ["\033[38;5;130m", "\033[38;5;22m", "\033[38;5;28m", "\033[38;5;59m", "\033[38;5;94m", "\033[38;5;130m"],
    "dankpods": ["\033[38;5;46m", "\033[38;5;130m", "\033[38;5;106m", "\033[38;5;118m", "\033[38;5;46m", "\033[38;5;130m"],
    "alien": ["\033[38;5;78m", "\033[38;5;135m", "\033[38;5;85m", "\033[38;5;123m", "\033[38;5;78m", "\033[38;5;135m"],
    "mardi gras": ["\033[38;5;93m", "\033[38;5;34m", "\033[38;5;226m", "\033[38;5;93m", "\033[38;5;34m", "\033[38;5;226m"],
    "gunmetal": ["\033[38;5;244m", "\033[38;5;240m", "\033[38;5;248m", "\033[38;5;244m", "\033[38;5;240m", "\033[38;5;248m"],
    "google": ["\033[38;5;21m", "\033[38;5;196m", "\033[38;5;226m", "\033[38;5;46m", "\033[38;5;21m", "\033[38;5;196m", "\033[38;5;226m"],
    "gemini": ["\033[38;5;105m", "\033[38;5;141m", "\033[38;5;183m", "\033[38;5;229m", "\033[38;5;39m", "\033[38;5;87m", "\033[38;5;123m"],
    "sunset": ["\033[38;5;208m", "\033[38;5;196m", "\033[38;5;93m", "\033[38;5;19m", "\033[38;5;202m", "\033[38;5;166m", "\033[38;5;124m"],
    "mint": ["\033[38;5;120m", "\033[38;5;15m", "\033[38;5;120m", "\033[38;5;15m", "\033[38;5;118m", "\033[38;5;15m"],
    "cyberpunk": ["\033[38;5;51m", "\033[38;5;201m", "\033[38;5;226m", "\033[38;5;51m", "\033[38;5;201m", "\033[38;5;226m"],
    "coffee": ["\033[38;5;130m", "\033[38;5;230m", "\033[38;5;52m", "\033[38;5;130m", "\033[38;5;230m", "\033[38;5;52m"],
    "strawberry": ["\033[38;5;196m", "\033[38;5;217m", "\033[38;5;28m", "\033[38;5;196m", "\033[38;5;217m", "\033[38;5;28m"],
    "lavender": ["\033[38;5;219m", "\033[38;5;15m", "\033[38;5;219m", "\033[38;5;15m", "\033[38;5;201m", "\033[38;5;15m"],
    "neon": ["\033[38;5;226m", "\033[38;5;207m", "\033[38;5;51m", "\033[38;5;226m", "\033[38;5;207m", "\033[38;5;51m"],
    "autumnal": ["\033[38;5;172m", "\033[38;5;208m", "\033[38;5;166m", "\033[38;5;202m", "\033[38;5;130m", "\033[38;5;136m", "\033[38;5;178m"],
    "70s": ["\033[38;5;130m", "\033[38;5;166m", "\033[38;5;214m", "\033[38;5;106m", "\033[38;5;136m", "\033[38;5;230m", "\033[38;5;178m"],
    "80s": ["\033[38;5;201m", "\033[38;5;51m", "\033[38;5;226m", "\033[38;5;118m", "\033[38;5;207m", "\033[38;5;15m", "\033[38;5;198m"],
    "90s": ["\033[38;5;88m", "\033[38;5;91m", "\033[38;5;64m", "\033[38;5;103m", "\033[38;5;139m", "\033[38;5;15m", "\033[38;5;58m"],
    "darkness": ["\033[38;5;8m", "\033[38;5;16m", "\033[38;5;238m", "\033[38;5;52m", "\033[38;5;244m"],
    "midnight": ["\033[38;5;17m", "\033[38;5;23m", "\033[38;5;29m", "\033[38;5;54m", "\033[38;5;60m"],
    "shadow": ["\033[38;5;232m", "\033[38;5;238m", "\033[38;5;244m", "\033[38;5;250m", "\033[38;5;254m"],
    "obsidian": ["\033[38;5;16m", "\033[38;5;23m", "\033[38;5;29m", "\033[38;5;52m", "\033[38;5;58m"],
    "nightsky": ["\033[38;5;17m", "\033[38;5;54m", "\033[38;5;60m", "\033[38;5;96m", "\033[38;5;102m"],
    "deepsea": ["\033[38;5;16m", "\033[38;5;23m", "\033[38;5;29m", "\033[38;5;35m", "\033[38;5;39m"],
    "tairy greene": ["\033[38;5;226m", "\033[38;5;190m", "\033[38;5;154m", "\033[38;5;118m", "\033[38;5;82m", "\033[38;5;46m"],
    "beef floater": ["\033[38;5;130m", "\033[38;5;196m", "\033[38;5;130m", "\033[38;5;196m", "\033[38;5;15m"],
    "diarrhea times": ["\033[38;5;106m", "\033[38;5;130m", "\033[38;5;106m", "\033[38;5;130m", "\033[38;5;226m"],
    "pills": ["\033[38;5;15m", "\033[38;5;220m", "\033[38;5;15m", "\033[38;5;220m", "\033[38;5;196m"],
    "wet asphalt": ["\033[38;5;8m", "\033[38;5;236m", "\033[38;5;244m"],
    "tv static": ["\033[38;5;255m", "\033[38;5;231m", "\033[38;5;255m", "\033[38;5;231m", "\033[38;5;255m"],
    "grape soda": ["\033[38;5;93m", "\033[38;5;141m", "\033[38;5;93m", "\033[38;5;141m"],
    "lime jello": ["\033[38;5;118m", "\033[38;5;154m", "\033[38;5;118m", "\033[38;5;154m"],
    "blue raspberry": ["\033[38;5;27m", "\033[38;5;69m", "\033[38;5;117m"],
    "cotton candy": ["\033[38;5;219m", "\033[38;5;213m", "\033[38;5;195m"],
    "circuit board": ["\033[38;5;28m", "\033[38;5;46m", "\033[38;5;118m"],
    "toxic waste": ["\033[38;5;118m", "\033[38;5;46m", "\033[38;5;118m"],
}

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == "THEME_COLORS_GUI":
    theme_name = sys.argv[1]
    if theme_name in THEMES:
        theme_colors = THEMES[theme_name]
        print(f"background={theme_colors[0]}") # Example: Use first color for background
        print(f"foreground={theme_colors[-1]}") # Example: Use last color for foreground
        print(f"menu_bg={theme_colors[1]}") # Example: Use second color for menu background
        print(f"menu_fg={theme_colors[-2]}") # Example: Use second to last for menu foreground
    sys.exit(0)

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == "THEME_COLORS_GUI":
    theme_name = sys.argv[1]
    if theme_name in THEMES:
        theme_colors = THEMES[theme_name]
        print(f"background={theme_colors[0]}") # Example: Use first color for background
        print(f"foreground={theme_colors[-1]}") # Example: Use last color for foreground
        print(f"menu_bg={theme_colors[1]}") # Example: Use second color for menu background
        print(f"menu_fg={theme_colors[-2]}") # Example: Use second to last for menu foreground
    sys.exit(0)

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[2] == "THEME_COLORS_GUI":
    theme_name = sys.argv[1]
    if theme_name in THEMES:
        theme_colors = THEMES[theme_name]
        print(f"background={theme_colors[0]}") # Example: Use first color for background
        print(f"foreground={theme_colors[-1]}") # Example: Use last color for foreground
        print(f"menu_bg={theme_colors[1]}") # Example: Use second color for menu background
        print(f"menu_fg={theme_colors[-2]}") # Example: Use second to last for menu foreground
    sys.exit(0)

DARK_THEMES = ["darkness", "midnight", "shadow", "obsidian", "nightsky", "deepsea"]

for theme, colors in THEMES.items():
    if theme not in DARK_THEMES:
        THEMES[theme] = [color for color in colors if color != "\033[38;5;0m"]

THEME_SENTENCES = {
    "fire": "This text is on FIRE!",
    "ice": "Chillin' with this icy text.",
    "earth": "Down to earth and colorful.",
    "rainbow": "A spectrum of sensational colors!",
    "forest": "Lost in the colorful woods.",
    "ocean": "Dive into a sea of colors.",
    "seafoam": "Light and bubbly colors.",
    "usa": "Red, white, and blue-tiful!",
    "easter": "Egg-cellent colors for spring!",
    "fart": "Smells like colorful text.",
    "sprite": "Crisp and refreshing colors.",
    "pepsi": "The choice of a new generation of colors.",
    "windows 98": "Bringing back the colorful memories.",
    "windows xp": "Blissfully colorful.",
    "macos": "Think different... colors.",
    "xbox": "Unleash the colorful power.",
    "playstation": "For the colorful players.",
    "bigfoot": "Legendarily colorful.",
    "dankpods": "These colors are pretty good, not gonna lie.",
    "alien": "Out of this world colors!",
    "mardi gras": "Laissez les bons temps colorer!",
    "gunmetal": "Solid and steely colors.",
    "google": "Searching for the best colors.",
    "gemini": "Dual-toned and dazzling.",
    "sunset": "Painting the sky with these colors.",
    "mint": "Fresh and cool colors.",
    "cyberpunk": "High-tech and vibrant.",
    "coffee": "Brewing up some colorful text.",
    "strawberry": "Sweet and colorful.",
    "lavender": "Calming and aromatic colors.",
    "neon": "Bright and electrifying!",
    "autumnal": "The warm hues of falling leaves.",
    "70s": "Groovy and colorful, man!",
    "80s": "Totally radical colors!",
    "90s": "Everything's all that and a bag of colorful chips!",
    "darkness": "Embrace the absence of bright colors.",
    "midnight": "The deep hues of night.",
    "shadow": "Subtly shaded colors.",
    "obsidian": "Dark and glassy colors.",
    "nightsky": "A colorful canopy of stars.",
    "deepsea": "Mysteries in the colorful depths.",
    "tairy greene": "It's Tairy... and it's Yellowish-Greene... and colorful!",
    "beef floater": "Float on in a sea of color.",
    "diarrhea times": "Runny with color.",
    "pills": "A colorful dose of text.",
    "wet asphalt": "The shimmering colors of the street.",
    "tv static": "A colorful buzz of nothing.",
    "grape soda": "Sweet and purple-licious colors.",
    "lime jello": "Wiggly and colorful!",
    "blue raspberry": "A blast of blue color!",
    "cotton candy": "Sweet and fluffy colors.",
    "circuit board": "Electrifyingly colorful connections.",
    "toxic waste": "Dangerously colorful!",
}

TIM_ERIC_THEMES = list(THEMES.keys())

# Add US State Themes
state_themes = {
    "Alabama": ["\033[38;5;160m", "\033[38;5;161m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Crimson and White
    "Alaska": ["\033[38;5;33m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;226m", "\033[38;5;178m"],  # Deeper Blue, White, Gold
    "Arizona": ["\033[38;5;196m", "\033[38;5;202m", "\033[38;5;255m", "\033[38;5;214m", "\033[38;5;22m"],  # Red, White, Copper, Blue
    "Arkansas": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Red and White
    "California": ["\033[38;5;255m", "\033[38;5;249m", "\033[38;5;196m", "\033[38;5;226m", "\033[38;5;178m"],  # White, Red, Gold
    "Colorado": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;226m", "\033[38;5;166m"],  # Blue, White, Gold, Red
    "Connecticut": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Blue and White
    "Delaware": ["\033[38;5;100m", "\033[38;5;106m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Buff, Colonial Blue, White
    "Florida": ["\033[38;5;208m", "\033[38;5;202m", "\033[38;5;166m", "\033[38;5;220m", "\033[38;5;214m"],  # Shades of Orange
    "Georgia": ["\033[38;5;216m", "\033[38;5;217m", "\033[38;5;218m", "\033[38;5;223m", "\033[38;5;15m"],  # Shades of Peach and White
    "Hawaii": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;231m", "\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m"],  # Red, White, Blue, Gold
    "Idaho": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;196m"],  # Blue, Gold, Red
    "Illinois": ["\033[38;5;21m", "\033[38;5;27m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Darker Blue, White
    "Indiana": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;196m"],  # Blue, Gold, Red
    "Iowa": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;196m"],  # Blue, White, Red, Gold
    "Kansas": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;196m"],  # Blue, Gold, Red
    "Kentucky": ["\033[38;5;33m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Darker Blue, Gold, White
    "Louisiana": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, Gold, White
    "Maine": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;196m"],  # Blue, White, Red
    "Maryland": ["\033[38;5;255m", "\033[38;5;249m", "\033[38;5;166m", "\033[38;5;172m", "\033[38;5;208m"],  # White, Gold, variations
    "Massachusetts": ["\033[38;5;21m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Darker Blue, White
    "Michigan": ["\033[38;5;33m", "\033[38;5;45m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Darker Blue, Distinct Gold, White
    "Minnesota": ["\033[38;5;21m", "\033[38;5;45m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Darker Blue, Distinct Gold, White
    "Mississippi": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Red, Gold, White
    "Missouri": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;27m"],  # Red, White, Blue, Gold
    "Montana": ["\033[38;5;226m", "\033[38;5;178m", "\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m"],  # Gold, Blue, White
    "Nebraska": ["\033[38;5;226m", "\033[38;5;178m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Gold and White
    "Nevada": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;196m"],  # Blue, White, Red
    "New Hampshire": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Blue and White
    "New Jersey": ["\033[38;5;160m", "\033[38;5;167m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;184m"],  # Buff and Jersey Blue
    "New Mexico": ["\033[38;5;220m", "\033[38;5;214m", "\033[38;5;196m", "\033[38;5;203m", "\033[38;5;166m"],  # Yellow and Red
    "New York": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, Gold, White
    "North Carolina": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;27m"],  # Red, White, Blue
    "North Dakota": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;196m"],  # Blue, Gold, Red
    "Ohio": ["\033[38;5;160m", "\033[38;5;167m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;27m"],  # Scarlet, White, Blue
    "Oklahoma": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;196m"],  # Blue, White, Red
    "Oregon": ["\033[38;5;24m", "\033[38;5;30m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Navy Blue, Gold, White
    "Pennsylvania": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, Gold, White
    "Rhode Island": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;220m", "\033[38;5;214m", "\033[38;5;178m"],  # Blue and Gold
    "South Carolina": ["\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;160m", "\033[38;5;161m"],  # White and Indigo Blue
    "South Dakota": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, Gold, White
    "Tennessee": ["\033[38;5;160m", "\033[38;5;161m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;27m"],  # Crimson, White, Blue
    "Texas": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;196m"],  # Blue, White, Red
    "Utah": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;178m", "\033[38;5;196m", "\033[38;5;231m"],  # Blue, Gold, Red, White
    "Vermont": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, Gold, White
    "Virginia": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;220m", "\033[38;5;214m", "\033[38;5;178m"],  # Blue and Gold
    "Washington": ["\033[38;5;22m", "\033[38;5;28m", "\033[38;5;34m", "\033[38;5;40m", "\033[38;5;231m", "\033[38;5;249m"],  # Dark Green and White
    "West Virginia": ["\033[38;5;27m", "\033[38;5;39m", "\033[38;5;226m", "\033[38;5;231m", "\033[38;5;255m"],  # Blue, White, Gold
    "Wisconsin": ["\033[38;5;160m", "\033[38;5;161m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m"],  # Red and White
    "Wyoming": ["\033[38;5;196m", "\033[38;5;203m", "\033[38;5;231m", "\033[38;5;249m", "\033[38;5;255m", "\033[38;5;27m"],  # Red, White, Blue, Gold
}

state_slogans = {
    "Alabama": "We Dare Defend Our Rights",
    "Alaska": "North to the Future",
    "Arizona": "Ditat Deus (God Enriches)",
    "Arkansas": "Regnat Populus (The People Rule)",
    "California": "Eureka (I Have Found It)",
    "Colorado": "Nil Sine Numine (Nothing Without Providence)",
    "Connecticut": "Qui Transtulit Sustinet (He Who Transplanted Still Sustains)",
    "Delaware": "Liberty and Independence",
    "Florida": "In God We Trust",
    "Georgia": "Wisdom, Justice, Moderation",
    "Hawaii": "Ua Mau ke Ea o ka ʻĀina i ka Pono (The Life of the Land Is Perpetuated in Righteousness)",
    "Idaho": "Esto Perpetua (May It Be Perpetual)",
    "Illinois": "State Sovereignty, National Union",
    "Indiana": "The Crossroads of America",
    "Iowa": "Our Liberties We Prize and Our Rights We Will Maintain",
    "Kansas": "Ad Astra Per Aspera (To the Stars Through Difficulties)",
    "Kentucky": "Deo Gratiam Habeamus (Let Us Be Grateful to God)",
    "Louisiana": "Union, Justice, Confidence",
    "Maine": "Dirigo (I Lead)",
    "Maryland": "Fatti Maschii, Parole Femine (Manly Deeds, Womanly Words)",
    "Massachusetts": "Ense petit placidam sub libertate quietem (By the Sword We Seek Peace, But Peace Only Under Liberty)",
    "Michigan": "Si Quaeris Peninsulam Amoenam Circumspice (If You Seek a Pleasant Peninsula, Look About You)",
    "Minnesota": "L'Étoile du Nord (The Star of the North)",
    "Mississippi": "Virtute et Armis (By Valor and Arms)",
    "Missouri": "Salus Populi Suprema Lex Esto (The Welfare of the People Shall Be the Supreme Law)",
    "Montana": "Oro y Plata (Gold and Silver)",
    "Nebraska": "Equality Before the Law",
    "Nevada": "All for Our Country",
    "New Hampshire": "Live Free or Die",
    "New Jersey": "Liberty and Prosperity",
    "New Mexico": "Crescit Eundo (It Grows as It Goes)",
    "New York": "Excelsior (Ever Upward)",
    "North Carolina": "Esse Quam Videri (To Be Rather Than to Seem)",
    "North Dakota": "Liberty and Union, Now and Forever, One and Inseparable",
    "Ohio": "With God, All Things Are Possible",
    "Oklahoma": "Labor Omnia Vincit (Labor Conquers All)",
    "Oregon": "Alis Volat Propriis (She Flies With Her Own Wings)",
    "Pennsylvania": "Virtue, Liberty, and Independence",
    "Rhode Island": "Hope",
    "South Carolina": "Dum Spiro Spero (While I Breathe, I Hope) and Animis Opibusque Parati (Prepared in Mind and Resources)",
    "South Dakota": "Under God the People Rule",
    "Tennessee": "Agriculture and Commerce",
    "Texas": "Friendship",
    "Utah": "Industry",
    "Vermont": "Freedom and Unity",
    "Virginia": "Sic Semper Tyrannis (Thus Always to Tyrants)",
    "Washington": "Alki (By and By)",
    "West Virginia": "Montani Semper Liberi (Mountaineers Are Always Free)",
    "Wisconsin": "Forward",
    "Wyoming": "Equal Rights",
}

THEMES.update(state_themes)
THEME_SENTENCES.update({state: slogan for state, slogan in state_slogans.items()})
TIM_ERIC_THEMES = list(THEMES.keys())


def colorize_text(text, theme):
    """Colorizes the input text with the colors from the specified theme."""
    if theme in THEMES:
        colors = THEMES[theme]
        colored_text = ""
        for i, char in enumerate(text):
            color_code = colors[i % len(colors)]
            colored_text += f"{color_code}{char}{RESET_COLOR}"
        return colored_text
    else:
        return f"\033[31mError: Theme '{theme}' not found.{RESET_COLOR}"

def get_flag_art():
    """Returns a more correctly shaped ASCII art for the American flag with a random theme."""
    flag = [
        " * * * * * * }OOOOOOOO0OOOOOOOOOOOOOOOOOOOOOOOO}",
        "  * * * * *  }=================================}",
        " * * * * * * }OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO}",
        "  * * * * *  }=================================}",
        " * * * * * * }OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO}",
        "  * * * * *  }=================================}",
        " * * * * * * }OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO}",
        "===============================================}",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0OOOOOOOO}",
        "===============================================}",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0OOOOOOO}",
        "===============================================}",
        "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0OOOOOO}",
    ]
    theme = random.choice(TIM_ERIC_THEMES)
    colored_flag = [colorize_text(line, theme) for line in flag]
    return colored_flag

def show_all_themes():
    """Shows examples of all available themes with funny themed sentences."""
    os.system('clear')
    print("Examples of all themes:\n")
    for theme in TIM_ERIC_THEMES:
        colored_theme_name = colorize_text(theme.title().ljust(15), theme)
        funny_sentence = THEME_SENTENCES.get(theme, f"This text is using the '{theme}' theme.")
        colored_sentence = colorize_text(funny_sentence, theme)
        print(f"{colored_theme_name}: {colored_sentence}")
    print("\n")

def show_help():
    """Displays the help message with a themed banner, license box, and footer."""
    os.system('clear')
    flag_art = get_flag_art()

    for line in flag_art:
        print(line)

    theme_version = random.choice(TIM_ERIC_THEMES)
    theme_justin = random.choice(TIM_ERIC_THEMES)

    footer = [
        "------------------------------------------------------------",
        f"| {colorize_text(f'{SCRIPT_NAME_HUMAN} version {SCRIPT_VERSION} ({SCRIPT_CODENAME})', theme_version).ljust(58)} |",
        f"| {'BROUGHT TO YOU BY: '.ljust(24)}{colorize_text('JUSTIN FALCONTECHNIX', theme_justin).ljust(31)} |",
        f"| {'AND '.ljust(24)}{colorize_text('GEMINI ADVANCED', 'gemini').ljust(31)} |",
        "------------------------------------------------------------",
        "| This work is licensed under a Creative Commons           |",
        "| Attribution-ShareAlike 4.0 International License.      |",
        "| (https://creativecommons.org/licenses/by-sa/4.0/)      |",
        "------------------------------------------------------------"
    ]

    for line in footer:
        print(line)

    print("\n")

    random_theme = random.choice(TIM_ERIC_THEMES)
    print("Random Theme Example:")
    example_text = f"This text is using the '{random_theme}' theme."
    print(f"{colorize_text(random_theme.title(), random_theme)}: {colorize_text(example_text, random_theme)}")

    installed = os.path.exists(INSTALL_PATH) and os.access(INSTALL_PATH, os.X_OK)

    usage_command = SCRIPT_NAME_COMMAND if installed else f"./{SCRIPT_NAME_COMMAND}.py" # Adjust if you renamed the file

    print(f"\nUsage: {usage_command} [-theme THEME] [-all] [-install] [-uninstall] [-TGTify <script>] [-infect <script> -theme <theme>] [-disinfect <script>] [TEXT or <script>]")
    print(f"\nArguments:")
    print(f"    [TEXT or <script>]".ljust(60) + "The text to colorize or the script to TGTify.")
    print(f"    -theme THEME".ljust(60) + "Specify a color theme.")
    print(f"    -all".ljust(60) + "Show examples of all themes.")
    print(f"    -install".ljust(60) + f"Install the script to {INSTALL_PATH}.")
    print(f"    -uninstall".ljust(60) + f"Uninstall the script from {INSTALL_PATH}.")
    print(f"    -TGTify <script>".ljust(60) + "Execute a script file and colorize its output.")
    print(f"    -infect <script> -theme <theme>".ljust(60) + "Install a theme into a Python script.")
    print(f"    -disinfect <script>".ljust(60) + "Uninstall themes from a Python script.")
    print(f"    -h, --help".ljust(60) + "Show this help message and exit.")
    print(f"\nExample: {usage_command} -theme \"Tairy Greene\" \"Hello World\"")
    print(f"Example (piped): echo \"This is piped\" | {usage_command} -theme \"ocean\"")
    print(f"Example (TGTify script): {usage_command} -TGTify ./my_script.sh -theme \"fire\"")
    print(f"Example (infect): {usage_command} -infect ./my_other_script.py -theme \"neon\"")
    print(f"Example (disinfect): {usage_command} -disinfect ./my_other_script.py")

    print(f"\nAvailable themes:")
    themes_per_line = 5
    available_themes = [theme for theme in TIM_ERIC_THEMES if theme not in state_themes]
    for i, theme in enumerate(available_themes):
        colored_theme = colorize_text(theme.ljust(15), theme)
        print(f"{colored_theme}", end="")
        if (i + 1) % themes_per_line == 0:
            print()
    if len(available_themes) % themes_per_line != 0:
        print()
    if state_themes:
        print(colorize_text("***ALL US STATES***".ljust(15), "usa"))

def install_script():
    """Placeholder function for installing the script."""
    print("Installing script...")

def uninstall_script():
    """Placeholder function for uninstalling the script."""
    print("Uninstalling script...")

def run_and_tgtify(script_path, theme):
    """Runs the given script and colorizes its output line by line."""
    try:
        process = subprocess.Popen(
            [script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if process.stdout:
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                print(colorize_text(line.strip(), theme))

        # Optionally handle stderr as well (could be colored differently)
        if process.stderr:
            for line in process.stderr:
                print(f"\033[31m{colorize_text(line.strip(), theme)}{RESET_COLOR}")

        process.wait() # Wait for the script to finish

    except FileNotFoundError:
        print(f"\033[31mError: Script file not found or not executable: {script_path}{RESET_COLOR}")
    except Exception as e:
        print(f"\033[31mError executing script: {e}{RESET_COLOR}")

def infect_script(script_path, theme_name):
    """Installs a theme into a Python script by replacing placeholder function calls."""
    if not os.path.exists(script_path):
        print(f"\033[31mError: Script not found: {script_path}{RESET_COLOR}")
        return
    if theme_name not in THEMES:
        print(f"\033[31mError: Theme not found: {theme_name}{RESET_COLOR}")
        return

    try:
        with open(script_path, 'r') as f:
            script_content = f.read()

        # Define the placeholder function pattern: tgt_placeholder("text", "theme")
        placeholder_pattern = r'tgt_placeholder\("([^"]*)",\s*"([^"]*)"\)'

        def replace_placeholder(match):
            text_to_colorize = match.group(1)
            theme_to_use = match.group(2)
            if theme_to_use == theme_name:
                return colorize_text(text_to_colorize, theme_name)
            else:
                return match.group(0) # Keep the original if the theme doesn't match

        modified_content = re.sub(placeholder_pattern, replace_placeholder, script_content)

        with open(script_path, 'w') as f:
            f.write(modified_content)

        print(f"\033[32mSuccessfully infected '{script_path}' with the '{theme_name}' theme.\033[0m")
        print("\033[33mWarning: This modifies the original script. Consider using version control.\033[0m")

    except Exception as e:
        print(f"\033[31mError infecting script: {e}{RESET_COLOR}")

def disinfect_script(script_path):
    """Uninstalls themes from a Python script by removing TGT's color codes."""
    if not os.path.exists(script_path):
        print(f"\033[31mError: Script not found: {script_path}{RESET_COLOR}")
        return

    try:
        with open(script_path, 'r') as f:
            script_content = f.read()

        # Define the pattern for TGT's ANSI color codes
        ansi_code_pattern = r'\033\[38;5;\d+m'

        modified_content = re.sub(ansi_code_pattern, '', script_content)

        with open(script_path, 'w') as f:
            f.write(modified_content)

        print(f"\033[32mSuccessfully disinfected '{script_path}'. TGT color codes have been removed.\033[0m")
        print("\033[33mWarning: This modifies the original script. Consider using version control.\033[0m")

    except Exception as e:
        print(f"\033[31mError disinfecting script: {e}{RESET_COLOR}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{SCRIPT_NAME_HUMAN} - Colorize text with various themes.")
    parser.add_argument("input", nargs="?", help="The text to colorize or the script to TGTify.")
    parser.add_argument("-theme", help="Specify a color theme.")
    parser.add_argument("-all", action="store_true", help="Show examples of all themes.")
    parser.add_argument("-install", action="store_true", help="Install the script.")
    parser.add_argument("-uninstall", action="store_true", help="Uninstall the script.")
    parser.add_argument("-v", "--version", action="store_true", help="Show version and exit.")
    parser.add_argument("-TGTify", help="Execute a script file and colorize its output. Provide the script path.")
    parser.add_argument("-infect", nargs='?', help="Install a theme into a Python script. Specify the script path.")
    parser.add_argument("-disinfect", nargs='?', help="Uninstall themes from a Python script. Specify the script path.")
    args = parser.parse_args()

    if args.version:
        print(f"{SCRIPT_NAME_HUMAN} version {SCRIPT_VERSION} ({SCRIPT_CODENAME})")
        sys.exit(0)

    if args.all:
        show_all_themes()
        sys.exit(0)
    elif args.install:
        install_script()
    elif args.uninstall:
        uninstall_script()
    elif args.TGTify:
        script_path = args.TGTify
        theme = args.theme if args.theme else random.choice(TIM_ERIC_THEMES)
        run_and_tgtify(script_path, theme)
    elif args.infect:
        if args.theme:
            infect_script(args.infect, args.theme)
        else:
            print("\033[31mError: Please specify a theme to infect with using -theme.\033[0m")
            sys.exit(1)
    elif args.disinfect:
        disinfect_script(args.disinfect)
    elif args.input:
        if os.path.exists(args.input):
            try:
                with open(args.input, 'r') as f:
                    script_content = f.read()
                    theme = args.theme if args.theme else random.choice(TIM_ERIC_THEMES)
                    for line in script_content.splitlines():
                        print(colorize_text(line, theme))
            except Exception as e:
                print(f"\033[31mError reading script file: {e}{RESET_COLOR}")
        else:
            theme = args.theme if args.theme else random.choice(TIM_ERIC_THEMES)
            print(colorize_text(args.input, theme))
    elif not sys.stdin.isatty(): # Handle piped input if no other arguments
        theme = args.theme if args.theme else random.choice(TIM_ERIC_THEMES)
        for line in sys.stdin:
            print(colorize_text(line.strip(), theme))
    else:
        show_help()
        sys.exit(0)
