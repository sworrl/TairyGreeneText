#!/bin/bash

# Clear the screen at the start
clear

script_name="TGT"
install_path="/usr/local/bin/$script_name"
github_repo_url="YOUR_GITHUB_RAW_URL_HERE" # Placeholder for the GitHub raw URL

is_steamos() {
  if [[ -f "/etc/os-release" ]]; then
    if grep -q "SteamOS" "/etc/os-release"; then
      return 0 # It's SteamOS
    fi
  fi
  return 1 # It's not SteamOS
}

unlock_readonly() {
  if is_steamos; then
    echo "Attempting to unlock read-only filesystem on SteamOS..."
    sudo steamos-readonly disable
    if [[ $? -ne 0 ]]; then
      echo "Error: Failed to unlock read-only filesystem. Please try running the install/update command again with sudo."
      return 1
    fi
  fi
  return 0
}

relock_readonly() {
  if is_steamos; then
    echo "Relocking read-only filesystem on SteamOS..."
    sudo steamos-readonly enable
    if [[ $? -ne 0 ]]; then
      echo "Error: Failed to relock read-only filesystem. This might require a reboot."
      return 1
    fi
  fi
  return 0
}

TGT() {
  local text="$1"
  local theme="${2:-}"
  local n=${#text}
  local spread=2 # Default spread
  if [[ "$text" == "$theme" ]]; then
    spread=1 # Reduce spread to 1 when coloring theme names in help
  fi
  local colors=()
  local reset=$(echo -e "\e[0m")

  local lower_theme="${theme,,}" # Convert theme to lowercase

  case "$lower_theme" in
    "fire")
      colors=($(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;202m") $(echo -e "\e[38;5;208m") $(echo -e "\e[38;5;214m") $(echo -e "\e[38;5;220m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;232m")) # Red, Dark Orange, Orange, Light Orange, Yellow, Bright Yellow, White
      ;;
    "ice")
      colors=($(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;87m") $(echo -e "\e[38;5;111m") $(echo -e "\e[38;5;117m") $(echo -e "\e[38;5;153m") $(echo -e "\e[38;5;159m") $(echo -e "\e[38;5;231m")) # Light Blue, Sky Blue, Medium Blue, Steel Blue, Light Cyan, White, Bright White
      ;;
    "earth")
      colors=($(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;34m") $(echo -e "\e[38;5;40m") $(echo -e "\e[38;5;100m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;136m") $(echo -e "\e[38;5;172m")) # Forest Green, Dark Olive Green, Olive, Brown, Sienna, Tan, Sandy Brown
      ;;
    "rainbow")
      colors=($(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;208m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;93m") $(echo -e "\e[38;5;99m")) # Red, Orange, Yellow, Green, Blue, Indigo, Violet
      ;;
    "forest")
      colors=($(echo -e "\e[38;5;22m") $(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;34m") $(echo -e "\e[38;5;40m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;76m") $(echo -e "\e[38;5;118m")) # Dark Green, Forest Green, Dark Olive, Olive, Light Green, Sea Green, Lime
      ;;
    "ocean")
      colors=($(echo -e "\e[38;5;27m") $(echo -e "\e[38;5;33m") $(echo -e "\e[38;5;39m") $(echo -e "\e[38;5;63m") $(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;86m") $(echo -e "\e[38;5;117m")) # Dark Blue, Blue, Light Blue, Deep Sky Blue, Light Cyan, Turquoise, Steel Blue
      ;;
    "seafoam")
      colors=($(echo -e "\e[38;5;120m") $(echo -e "\e[38;5;87m") $(echo -e "\e[38;5;159m") $(echo -e "\e[38;5;153m") $(echo -e "\e[38;5;117m") $(echo -e "\e[38;5;231m")) # Light Green, Sky Blue, White, Light Cyan, Steel Blue, Bright White
      ;;
    "usa")
      colors=($(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;197m") $(echo -e "\e[38;5;231m") $(echo -e "\e[38;5;199m")) # Red, White, Blue, Bright Red, Bright White, Bright Blue
      ;;
    "easter")
      colors=($(echo -e "\e[38;5;213m") $(echo -e "\e[38;5;195m") $(echo -e "\e[38;5;223m") $(echo -e "\e[38;5;111m") $(echo -e "\e[38;5;229m") $(echo -e "\e[38;5;217m")) # Light Pink, Lavender, Light Yellow, Light Blue, Mint Green, Pink
      ;;
    "fart")
      colors=($(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;106m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;101m") $(echo -e "\e[38;5;178m") $(echo -e "\e[38;5;136m")) # Brown, Lime Green, Yellow, Yellow Green, Light Brown, Tan
      ;;
    "sprite")
      colors=($(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;121m") $(echo -e "\e[38;5;119m") $(echo -e "\e[38;5;229m")) # Lime Green, White, Light Green, Chartreuse, Spring Green, Mint Green
      ;;
    "pepsi")
      colors=($(echo -e "\e[38;5;4m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;9m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;4m") $(echo -e "\e[38;5;9m")) # Dark Blue, White, Red, White, Dark Blue, Red
      ;;
    "windows 98")
      colors=($(echo -e "\e[38;5;39m") $(echo -e "\e[38;5;7m") $(echo -e "\e[38;5;17m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;33m") $(echo -e "\e[38;5;51m") $(echo -e "\e[38;5;45m")) # Light Blue, Light Gray, Medium Blue, White, Blue, Cyan, Steel Blue 1
      ;;
    "windows xp")
      colors=($(echo -e "\e[38;5;27m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;39m")) # Dark Blue, White, Light Green, Blue, Light Blue, Lime Green, Light Blue 1
      ;;
    "macos")
      colors=($(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;8m") $(echo -e "\e[38;5;7m") $(echo -e "\e[38;5;109m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;248m") $(echo -e "\e[38;5;109m")) # White, Gray, Light Gray, Light Blue, White, Light Gray, Light Blue 1
      ;;
    "xbox")
      colors=($(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;0m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;76m")) # Light Green, Black, White, Forest Green, Light Green, Lime Green, Sea Green
      ;;
    "playstation")
      colors=($(echo -e "\e[38;5;4m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;6m") $(echo -e "\e[38;5;12m") $(echo -e "\e[38;5;4m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;6m")) # Dark Blue, White, Purple, Red, Dark Blue, White, Purple
      ;;
    "bigfoot")
      colors=($(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;22m") $(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;59m") $(echo -e "\e[38;5;94m") $(echo -e "\e[38;5;130m")) # Brown, Dark Green, Forest Green, Dark Olive, Dark Olive Green, Brown
      ;;
    "dankpods")
      colors=($(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;106m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;130m")) # Light Green, Brown, Lime Green, Lime Green, Light Green, Brown
      ;;
    "alien")
      colors=($(echo -e "\e[38;5;78m") $(echo -e "\e[38;5;135m") $(echo -e "\e[38;5;85m") $(echo -e "\e[38;5;123m") $(echo -e "\e[38;5;78m") $(echo -e "\e[38;5;135m")) # Dark Sea Green, Medium Purple, Light Blue, Light Steel Blue, Dark Sea Green, Medium Purple
      ;;
    "mardi gras")
      colors=($(echo -e "\e[38;5;93m") $(echo -e "\e[38;5;34m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;93m") $(echo -e "\e[38;5;34m") $(echo -e "\e[38;5;226m")) # Purple, Green, Gold, Purple, Green, Gold
      ;;
    "gunmetal")
      colors=($(echo -e "\e[38;5;244m") $(echo -e "\e[38;5;240m") $(echo -e "\e[38;5;248m") $(echo -e "\e[38;5;244m") $(echo -e "\e[38;5;240m") $(echo -e "\e[38;5;248m")) # Dark Gray, Medium Gray, Light Gray, Dark Gray, Medium Gray, Light Gray
      ;;
    "google")
      colors=($(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;226m")) # Blue, Red, Yellow, Green, Blue, Red, Yellow
      ;;
    "gemini")
      colors=($(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;177m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;177m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;105m")) # Light Blue, Light Purple, White, Light Blue, Light Purple, White, Medium Purple
      ;;
    "sunset")
      colors=($(echo -e "\e[38;5;208m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;93m") $(echo -e "\e[38;5;19m") $(echo -e "\e[38;5;202m") $(echo -e "\e[38;5;166m") $(echo -e "\e[38;5;124m")) # Orange, Red, Purple, Dark Blue, Dark Orange, Salmon, Light Salmon
      ;;
    "mint")
      colors=($(echo -e "\e[38;5;120m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;120m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;15m")) # Light Green, White, Light Green, White, Lime Green, White
      ;;
    "cyberpunk")
      colors=($(echo -e "\e[38;5;51m") $(echo -e "\e[38;5;201m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;51m") $(echo -e "\e[38;5;201m") $(echo -e "\e[38;5;226m")) # Cyan, Magenta, Yellow, Cyan, Magenta, Yellow
      ;;
    "coffee")
      colors=($(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;230m") $(echo -e "\e[38;5;52m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;230m") $(echo -e "\e[38;5;52m")) # Brown, Beige, Dark Brown, Brown, Beige, Dark Brown
      ;;
    "strawberry")
      colors=($(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;217m") $(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;217m") $(echo -e "\e[38;5;28m")) # Red, Pink, Green, Red, Pink, Green
      ;;
    "lavender")
      colors=($(echo -e "\e[38;5;219m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;219m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;201m") $(echo -e "\e[38;5;15m")) # Light Purple, White, Light Purple, White, Magenta, White
      ;;
    "neon")
      colors=($(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;207m") $(echo -e "\e[38;5;51m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;207m") $(echo -e "\e[38;5;51m")) # Bright Yellow, Bright Pink, Bright Cyan, Bright Yellow, Bright Pink, Bright Cyan
      ;;
    "oceanic")
      colors=($(echo -e "\e[38;5;38m") $(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;38m") $(echo -e "\e[38;5;81m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;117m")) # Teal, Light Blue, White, Teal, Light Blue, White, Steel Blue
      ;;
    "70s")
      colors=($(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;166m") $(echo -e "\e[38;5;214m") $(echo -e "\e[38;5;106m") $(echo -e "\e[38;5;136m") $(echo -e "\e[38;5;230m") $(echo -e "\e[38;5;178m")) # Brown, Sandy Brown, Light Orange, Lime Green, Tan, Beige, Light Brown
      ;;
    "80s")
      colors=($(echo -e "\e[38;5;201m") $(echo -e "\e[38;5;51m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;207m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;198m")) # Magenta, Cyan, Yellow, Lime Green, Bright Pink, White, Hot Pink
      ;;
    "90s")
      colors=($(echo -e "\e[38;5;88m") $(echo -e "\e[38;5;91m") $(echo -e "\e[38;5;64m") $(echo -e "\e[38;5;103m") $(echo -e "\e[38;5;139m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;58m")) # Medium Purple, Dark Magenta, Green Yellow, Medium Spring Green, Light Slate Blue, White, Dark Cyan
      ;;
    "darkness")
      colors=($(echo -e "\e[38;5;0m") $(echo -e "\e[38;5;8m") $(echo -e "\e[38;5;244m")) # Black, Dark Gray, Medium Gray
      ;;
    "midnight")
      colors=($(echo -e "\e[38;5;17m") $(echo -e "\e[38;5;0m") $(echo -e "\e[38;5;54m")) # Dark Blue, Black, Dark Purple
      ;;
    "shadow")
      colors=($(echo -e "\e[38;5;232m") $(echo -e "\e[38;5;0m") $(echo -e "\e[38;5;240m")) # Black, Dark Gray, Slightly lighter gray
      ;;
    "obsidian")
      colors=($(echo -e "\e[38;5;0m") $(echo -e "\e[38;5;16m") $(echo -e "\e[38;5;238m")) # Black, Very dark blue, Very dark gray
      ;;
    "nightsky")
      colors=($(echo -e "\e[38;5;17m") $(echo -e "\e[38;5;54m") $(echo -e "\e[38;5;232m")) # Dark Blue, Dark Purple, Black
      ;;
    "deepsea")
      colors=($(echo -e "\e[38;5;16m") $(echo -e "\e[38;5;23m") $(echo -e "\e[38;5;29m")) # Very dark blue, Dark teal, Dark green
      ;;
    "tairy greene")
      colors=($(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;28m") $(echo -e "\e[38;5;118m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;28m")) # Forest Green, Lime Green, Forest Green, Lime Green, White, Forest Green
      ;;
    "beef floater")
      colors=($(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;15m")) # Brown, Red, Brown, Red, White
      ;;
    "diarrhea times")
      colors=($(echo -e "\e[38;5;106m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;106m") $(echo -e "\e[38;5;130m") $(echo -e "\e[38;5;226m")) # Lime Green, Brown, Lime Green, Brown, Yellow
      ;;
    "pills")
      colors=($(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;220m") $(echo -e "\e[38;5;15m") $(echo -e "\e[38;5;220m") $(echo -e "\e[38;5;196m")) # White, Yellow, White, Yellow, Red
      ;;
    *)
      if [[ -n "$theme" ]]; then
        echo "Error: Theme '$theme' not recognized." >&2
      fi
      colors=($(echo -e "\e[38;5;196m") $(echo -e "\e[38;5;208m") $(echo -e "\e[38;5;226m") $(echo -e "\e[38;5;46m") $(echo -e "\e[38;5;21m") $(echo -e "\e[38;5;93m") $(echo -e "\e[38;5;99m")) # Default to rainbow
      ;;
  esac

  local color_count=${#colors[@]}

  if [[ "$color_count" -gt 0 ]]; then
    for ((i=0; i<n; i++)); do
      local char="${text:i:1}"
      local color_index=$(( (i / spread) % color_count ))
      printf "%s%s%s" "${colors[$color_index]}" "$char" "$reset"
    done
    echo # Add a newline at the end
  else
    if [[ -n "$theme" ]]; then
      echo "Error: No colors defined for the theme '$theme'." >&2
    fi
  fi
}

show_theme_example() {
  local text="$1"
  local theme="$2"
  echo -n "$theme: "
  TGT "$text" "$theme"
}

install() {
  if [[ "$(id -u)" -ne 0 ]]; then
    echo "This script needs to be run with sudo to install."
    echo "Please run: sudo $0 -install"
    return 1
  fi

  if unlock_readonly; then
    echo "Installing '$script_name' to '$install_path'..."
    cp "$0" "$install_path"
    local install_result=$?
    if [[ "$install_result" -ne 0 ]]; then
      echo "Error: Failed to copy the script to '$install_path'."
    else
      echo "Making '$install_path' executable..."
      chmod +x "$install_path"
      if [[ $? -ne 0 ]]; then
        echo "Error: Failed to make the script executable."
      fi
    fi
    relock_readonly
    if [[ "$install_result" -eq 0 ]]; then
      echo "Installation successful!"
      echo "You should now be able to run '$script_name' from any terminal."
      echo "You might need to close and reopen your terminal for the changes to take effect."
    fi
  else
    echo "Could not unlock the read-only filesystem. Installation failed."
  fi
}

uninstall() {
  if [[ "$(id -u)" -ne 0 ]]; then
    echo "This script needs to be run with sudo to uninstall."
    echo "Please run: sudo $0 -uninstall"
    return 1
  fi

  if [[ ! -f "$install_path" ]]; then
    echo "Error: '$script_name' is not installed in '$install_path'."
    return 1
  fi

  read -p "Are you sure you want to uninstall '$script_name' from '$install_path'? (y/N): " -n 1 -r
  echo
  if [[ ! "$REPLY" =~ ^[Yy]$ ]]; then
    echo "Uninstallation cancelled."
    return 0
  fi

  if unlock_readonly; then
    echo "Uninstalling '$script_name' from '$install_path'..."
    rm "$install_path"
    local uninstall_result=$?
    relock_readonly
    if [[ "$uninstall_result" -ne 0 ]]; then
      echo "Error: Failed to remove '$script_name' from '$install_path'."
    else
      echo "Uninstallation successful!"
    fi
  else
    echo "Could not unlock the read-only filesystem. Uninstallation might have failed."
  fi
}

update() {
  echo "Checking for updates for $script_name..."
  if ! command -v curl &> /dev/null; then
    echo "Error: curl is not installed. Please install curl to update." >&2
    return 1
  fi

  if [[ -z "$github_repo_url" ]]; then
    echo "Error: GitHub repository URL is not set." >&2
    return 1
  fi

  local latest_version_path="/tmp/${script_name}_latest"
  curl -s "$github_repo_url" -o "$latest_version_path"

  if [[ $? -ne 0 ]]; then
    echo "Error: Failed to download the latest version." >&2
    rm -f "$latest_version_path"
    return 1
  fi

  if cmp -s "$install_path" "$latest_version_path"; then
    echo "$script_name is already up to date."
    rm -f "$latest_version_path"
  else
    echo "A new version is available. Do you want to update? (y/N)"
    read -n 1 -r
    echo
    if [[ "$REPLY" =~ ^[Yy]$ ]]; then
      if unlock_readonly; then
        echo "Updating $script_name..."
        sudo cp "$latest_version_path" "$install_path"
        local update_result=$?
        if [[ "$update_result" -ne 0 ]]; then
          echo "Error: Failed to update the script. Please try again with sudo." >&2
        else
          echo "Successfully updated $script_name. You might need to close and reopen your terminal."
        fi
        relock_readonly
      else
        echo "Could not unlock the read-only filesystem. Update failed."
      fi
    fi
    rm -f "$latest_version_path"
  fi
}

show_help() {
  local themes=("Fire" "Ice" "Earth" "Rainbow" "Forest" "Ocean" "Seafoam" "USA" "Easter" "Fart" "Sprite" "Pepsi" "Windows 98" "Windows XP" "macOS" "Xbox" "PlayStation" "Bigfoot" "Dankpods" "Alien" "Mardi Gras" "Gunmetal" "Google" "Gemini" "Sunset" "Mint" "Cyberpunk" "Coffee" "Strawberry" "Lavender" "Neon" "Oceanic" "70s" "80s" "90s" "Darkness" "Midnight" "Shadow" "Obsidian" "Nightsky" "Deepsea" "Tairy Greene" "Beef Floater" "Diarrhea Times" "Pills")
  local help_theme="$1"
  local random_theme
  if [[ -z "$help_theme" ]]; then
    local random_index=$((RANDOM % ${#themes[@]}))
    random_theme="${themes[$random_index]}"
  else
    random_theme="$help_theme"
  fi

  local banner_theme="lavender" # Set the banner theme to lavender

  # Tim and Eric Style Banner (Colored)
  TGT "**************************************************" "$banner_theme"
  TGT "* *" "$banner_theme"
  TGT "* TGT (TAIRY GREENE TEXT)             *" "$banner_theme"
  TGT "* BROUGHT TO YOU BY: JUSTIN @ FALCONTECHNIX   *" "$banner_theme"
  TGT "* AND GEMINI!                  *" "$banner_theme"
  TGT "* *" "$banner_theme"
  TGT "**************************************************" "$banner_theme"
  echo ""
  echo "This work is licensed under a Creative Commons"
  echo "Attribution-ShareAlike 4.0 International License."
  echo "(https://creativecommons.org/licenses/by-sa/4.0/)"
  echo ""

  local max_theme_length=0
  for theme in "${themes[@]}"; do
    if [[ ${#theme} -gt "$max_theme_length" ]]; then
      max_theme_length=${#theme}
    fi
  done

  local colored_themes_array=()
  local reset=$(echo -e "\e[0m")
  for theme in "${themes[@]}"; do
    local first_color=""
    local lower_theme="${theme,,}"
    case "$lower_theme" in
      "fire") first_color=$(echo -e "\e[38;5;196m"); ;;
      "ice") first_color=$(echo -e "\e[38;5;81m"); ;;
      "earth") first_color=$(echo -e "\e[38;5;28m"); ;;
      "rainbow") first_color=$(echo -e "\e[38;5;196m"); ;;
      "forest") first_color=$(echo -e "\e[38;5;22m"); ;;
      "ocean") first_color=$(echo -e "\e[38;5;27m"); ;;
      "seafoam") first_color=$(echo -e "\e[38;5;120m"); ;;
      "usa") first_color=$(echo -e "\e[38;5;196m"); ;;
      "easter") first_color=$(echo -e "\e[38;5;213m"); ;;
      "fart") first_color=$(echo -e "\e[38;5;130m"); ;;
      "sprite") first_color=$(echo -e "\e[38;5;118m"); ;;
      "pepsi") first_color=$(echo -e "\e[38;5;4m"); ;;
      "windows 98") first_color=$(echo -e "\e[38;5;39m"); ;;
      "windows xp") first_color=$(echo -e "\e[38;5;27m"); ;;
      "macos") first_color=$(echo -e "\e[38;5;15m"); ;;
      "xbox") first_color=$(echo -e "\e[38;5;46m"); ;;
      "playstation") first_color=$(echo -e "\e[38;5;4m"); ;;
      "bigfoot") first_color=$(echo -e "\e[38;5;130m"); ;;
      "dankpods") first_color=$(echo -e "\e[38;5;46m"); ;;
      "alien") first_color=$(echo -e "\e[38;5;78m"); ;;
      "mardi gras") first_color=$(echo -e "\e[38;5;93m"); ;;
      "gunmetal") first_color=$(echo -e "\e[38;5;244m"); ;;
      "google") first_color=$(echo -e "\e[38;5;21m"); ;;
      "gemini") first_color=$(echo -e "\e[38;5;81m"); ;;
      "sunset") first_color=$(echo -e "\e[38;5;208m"); ;;
      "mint") first_color=$(echo -e "\e[38;5;120m"); ;;
      "cyberpunk") first_color=$(echo -e "\e[38;5;51m"); ;;
      "coffee") first_color=$(echo -e "\e[38;5;130m"); ;;
      "strawberry") first_color=$(echo -e "\e[38;5;196m"); ;;
      "lavender") first_color=$(echo -e "\e[38;5;219m"); ;;
      "neon") first_color=$(echo -e "\e[38;5;226m"); ;;
      "oceanic") first_color=$(echo -e "\e[38;5;38m"); ;;
      "70s") first_color=$(echo -e "\e[38;5;130m"); ;;
      "80s") first_color=$(echo -e "\e[38;5;201m"); ;;
      "90s") first_color=$(echo -e "\e[38;5;88m"); ;;
      "darkness") first_color=$(echo -e "\e[38;5;0m"); ;;
      "midnight") first_color=$(echo -e "\e[38;5;17m"); ;;
      "shadow") first_color=$(echo -e "\e[38;5;232m"); ;;
      "obsidian") first_color=$(echo -e "\e[38;5;0m"); ;;
      "nightsky") first_color=$(echo -e "\e[38;5;17m"); ;;
      "deepsea") first_color=$(echo -e "\e[38;5;16m"); ;;
      "tairy greene") first_color=$(echo -e "\e[38;5;28m"); ;;
      "beef floater") first_color=$(echo -e "\e[38;5;130m"); ;;
      "diarrhea times") first_color=$(echo -e "\e[38;5;106m"); ;;
      "pills") first_color=$(echo -e "\e[38;5;15m"); ;;
      *) first_color=$(echo -e "\e[38;5;196m"); ;; # Default
    esac
    local padded_theme="$first_color$theme$reset"
    local spaces=$((max_theme_length - ${#theme}))
    for ((k=0; k<spaces; k++)); do
      padded_theme+=" "
    done
    colored_themes_array+=("$padded_theme")
  done

  local num_themes=${#colored_themes_array[@]}
  local cols=3 # Number of columns
  local rows=$(( (num_themes + cols - 1) / cols ))

  echo "Available themes:"
  for ((i=0; i<rows; i++)); do
    for ((j=0; j<cols; j++)); do
      local index=$(( i + j * rows ))
      if [[ "$index" -lt "$num_themes" ]]; then
        printf "%s\t" "${colored_themes_array[$index]}"
      fi
    done
    echo ""
  done
  echo ""


  local help_message="Usage: ./$script_name [TEXT] [-theme THEME | -all | -install | -uninstall | -update]

  [TEXT]        The text you want to Tairy Greene-ify.
  -theme THEME  Specify a color theme to use.
                Example: ./$script_name \"Hello\" -theme \"Tairy Greene\"
  -all          Show this message with all available themes.
  -install      Install this script to '/usr/local/bin' so you can run it from anywhere.
  -uninstall    Uninstall this script from '/usr/local/bin'.
  -update       Check for and install the latest version from GitHub.

If no arguments are provided, a random theme will be chosen for the help message."

  if [[ -n "$help_theme" ]]; then
    echo "$help_message" | while IFS= read -r line; do
      TGT "$line" "$help_theme"
    done
  else
    echo "$help_message"
  fi
}

show_all_themes() {
  themes=("Fire" "Ice" "Earth" "Rainbow" "Forest" "Ocean" "Seafoam" "USA" "Easter" "Fart" "Sprite" "Pepsi" "Windows 98" "Windows XP" "macOS" "Xbox" "PlayStation" "Bigfoot" "Dankpods" "Alien" "Mardi Gras" "Gunmetal" "Google" "Gemini" "Sunset" "Mint" "Cyberpunk" "Coffee" "Strawberry" "Lavender" "Neon" "Oceanic" "70s" "80s" "90s" "Darkness" "Midnight" "Shadow" "Obsidian" "Nightsky" "Deepsea" "Tairy Greene" "Beef Floater" "Diarrhea Times" "Pills")
  theme_texts=(
    "Feeling hot, hot, hot!"
    "Brrr, so cool."
    "Down to earth vibes."
    "A spectrum of delight!"
    "Lost in the greenery."
    "Just keep swimming..."
    "Like a gentle wave."
    "Red, white, and blue, through and through!"
    "Happy Easter!"
    "Phew, that was stinky."
    "So crisp and clean."
    "Have a refreshing burst!"
    "The good old days of dial-up... and Clippy."
    "Embracing the bliss."
    "An apple a day..."
    "It's all about the game... and Master Chief."
    "Ready to play?"
    "Did you hear that?"
    "Check out these freakish ears on a stand!"
    "Greetings from another world... take me to your leader (who has better snacks)."
    "Laissez les bons temps rouler!"
    "Solid and strong."
    "Searching the web..."
    "Did you mean: 'What is the meaning of life?' Just kidding... mostly. (Probably 42.)"
    "Chasing the setting sun."
    "Fresh and cool sensation."
    "Living in a digital world."
    "A warm and comforting brew."
    "Sweet and juicy delight."
    "Calm and fragrant fields."
    "Bright lights in the city."
    "Deep and mysterious waters."
    "Groovy, baby!"
    "Totally tubular!"
    "Wassup, dude!"
    "Embrace the void."
    "Silent and deep."
    "Hidden in plain sight."
    "A glassy, dark surface."
    "Stars peeking through."
    "Mysteries below the surface."
    "It's Tairy Greene!"
    "Is that a beef floater?"
    "Uh oh, diarrhea times..."
    "Take your vitamins!"
  )

  for i in "${!themes[@]}"; do
    show_theme_example "${theme_texts[$i]}" "${themes[$i]}"
  done
  echo "" # Add a newline before the color bar
  show_color_bar
}

show_color_bar() {
  echo -e "Color Bar (All 256 Colors - Organized):"
  for i in $(seq 16 255); do # Start from 16
    printf "\e[38;5;${i}m\u2588\e[0m"
    if [[ $(( (i - 16 + 1) % 16 )) -eq 0 ]]; then # Newline after every 16 colors
      echo ""
    fi
  done
  echo ""
}

# Main logic
if [[ $# -eq 0 ]]; then
  themes=("Fire" "Ice" "Earth" "Rainbow" "Forest" "Ocean" "Seafoam" "USA" "Easter" "Fart" "Sprite" "Pepsi" "Windows 98" "Windows XP" "macOS" "Xbox" "PlayStation" "Bigfoot" "Dankpods" "Alien" "Mardi Gras" "Gunmetal" "Google" "Gemini" "Sunset" "Mint" "Cyberpunk" "Coffee" "Strawberry" "Lavender" "Neon" "Oceanic" "70s" "80s" "90s" "Darkness" "Midnight" "Shadow" "Obsidian" "Nightsky" "Deepsea" "Tairy Greene" "Beef Floater" "Diarrhea Times" "Pills")
  random_index=$((RANDOM % ${#themes[@]}))
  random_theme="${themes[$random_index]}"
  themes=("$themes[@]")
  random_index="$random_index"
  random_theme="$random_theme"
  echo "Random Theme Example:"
  show_theme_example "This text is using the '$random_theme' theme." "$random_theme"
  echo ""
  show_help "$random_theme" # Pass the random theme to show_help
elif [[ "$1" == "-all" ]]; then
  show_all_themes
elif [[ "$1" == "-install" ]]; then
  install
elif [[ "$1" == "-uninstall" ]]; then
  uninstall
elif [[ "$1" == "-update" ]]; then
  update
elif [[ "$1" == "-theme" ]]; then
  if [[ -z "$2" ]]; then
    echo "Error: Please specify a theme after -theme." >&2
    show_help
    exit 1
  fi
  local text_to_colorize=""
  shift # Remove -theme
  shift # Remove the theme name
  if [[ $# -gt 0 ]]; then
    text_to_colorize="$*"
  else
    echo "Error: Please provide text to Tairy Greene-ify." >&2
    show_help
    exit 1
  fi
  TGT "$text_to_colorize" "$1"
elif [[ -n "$1" ]]; then
  local text_to_colorize="$1"
  local theme_option=""
  local theme_name=""
  if [[ "$2" == "-theme" ]] && [[ -n "$3" ]]; then
    theme_name="$3"
  fi
  TGT "$text_to_colorize" "$theme_name"
else
  show_help
fi
