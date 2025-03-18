Tairy Greene Text (TGT) - v2.0 "Maximum Yelling!"

Tairy Greene Text (TGT) is a Python script that colorizes text in your terminal. It offers a wide variety of themes, including colors inspired by Tim and Eric, US states, and various other fun and vibrant palettes. It can colorize text provided as arguments, piped input, or even the output of other scripts! It also has the ability to "infect" other Python scripts with TGT's colorization.
## Features

*   **Numerous Themes:** A large and growing collection of color themes. See the "Available Themes" section.
*   **Theme Sentences:** Each theme has a sentence displayed with `-all`.
*   **Piped Input:** Works with piped input (e.g., `echo "Hello" | tgt -theme fire`).
*   **Script Execution (-TGTify):** Run scripts and colorize their output.
*   **Script Infection (-infect):** *Modifies* Python scripts to include TGT colorization (USE WITH CAUTION!).
*   **Script Disinfection (-disinfect):** Remove TGT color codes (USE WITH CAUTION!).
*   **US State Themes:** Color themes for all 50 US states and their slogans.
*   **Installation/Uninstallation:** `-install` and `-uninstall` options.
*   **Random Theme:** A random theme is applied if none is specified.
*   **ANSI Color Codes:** Uses ANSI escape codes.
*   **Dynamic Theme Colors for GUI:** Output for GUI interpretation.
*   **Version Display:** Show version using `-v` or `--version`.


## Usage

```bash
./TGT.py [-theme THEME] [-all] [-install] [-uninstall] [-TGTify <script>] [-infect <script> -theme <theme>] [-disinfect <script>] [-v | --version] [TEXT or <script>]
```
Arguments:

* TEXT or <script>]: The text to colorize, or a script to run with colorized output (without -TGTify). If no text/script and no piped input, displays this help.
* -theme THEME: Specify a color theme. If omitted, a random theme is used.
* -all: Show examples of all available themes.
* -install: Install the script to /usr/local/bin/tgt.
* -uninstall: Uninstall the script.
* -v, --version: Display version information.
* -TGTify <script>: Execute a script and colorize its standard output and standard error. (Note: This feature may have limited functionality in the current version.)
* -infect <script> -theme <theme>: Install a theme permanently into a Python script by modifying its source code. Use with extreme caution and back up your script before using this 
   option! (Note: This feature may have limited functionality in the current version.)
* -disinfect <script>: Attempt to remove TGT colorization from a Python script that was previously modified with -infect. Use with extreme caution and back up your script!
* -h, --help: Show this help message and exit.
```bash
./TGT.py -theme "Tairy Greene" "Hello World"
echo "This is piped" | ./TGT.py -theme "ocean"
./TGT.py -TGTify ./my_script.sh -theme "fire"
./TGT.py -infect ./my_other_script.py -theme "neon"
./TGT.py -disinfect ./my_other_script.py
```

## Themes

<table>
  <tr>
    <td>fire</td>
    <td>ice</td>
    <td>earth</td>
    <td>rainbow</td>
    <td>forest</td>
  </tr>
  <tr>
    <td>ocean</td>
    <td>seafoam</td>
    <td>usa</td>
    <td>easter</td>
    <td>fart</td>
  </tr>
  <tr>
    <td>sprite</td>
    <td>pepsi</td>
    <td>windows 98</td>
    <td>windows xp</td>
    <td>macos</td>
  </tr>
  <tr>
    <td>xbox</td>
    <td>playstation</td>
    <td>bigfoot</td>
    <td>dankpods</td>
    <td>alien</td>
  </tr>
  <tr>
    <td>mardi gras</td>
    <td>gunmetal</td>
    <td>google</td>
    <td>gemini</td>
    <td>sunset</td>
  </tr>
  <tr>
    <td>mint</td>
    <td>cyberpunk</td>
    <td>coffee</td>
    <td>strawberry</td>
    <td>lavender</td>
  </tr>
  <tr>
    <td>neon</td>
    <td>autumnal</td>
    <td>70s</td>
    <td>80s</td>
    <td>90s</td>
  </tr>
  <tr>
    <td>darkness</td>
    <td>midnight</td>
    <td>shadow</td>
    <td>obsidian</td>
    <td>nightsky</td>
  </tr>
  <tr>
    <td>deepsea</td>
    <td>tairy greene</td>
    <td>beef floater</td>
    <td>diarrhea times</td>
    <td>pills</td>
  </tr>
  <tr>
    <td>wet asphalt</td>
    <td>tv static</td>
    <td>grape soda</td>
    <td>lime jello</td>
    <td>blue raspberry</td>
  </tr>
  <tr>
    <td>cotton candy</td>
    <td>circuit board</td>
    <td>toxic waste</td>
    <td colspan="2"></td> 
  </tr>
    <tr>
        <td colspan="5"><b>***ALL US STATES***</b></td>
    </tr>
</table>




## Notes on -infect and -TGTify:

The -infect and -TGTify features are currently in an experimental state.  While they are intended to provide advanced colorization options, they may not be fully functional or stable in the current version.  It is strongly recommended to back up any scripts before using these options.

## Key improvements and explanations:

*   **Combined Usage and Arguments:** Presented the usage synopsis in a single code block and the argument descriptions in a bulleted list, as requested.
*   **Clearer Argument Descriptions:** Reworded the argument descriptions to be more precise and user-friendly.  Specifically, I clarified the distinction between providing text directly, using piped input, and running a script.
*   **Emphasis and Warnings:**  Used bold text to highlight important warnings about `-infect` and `-disinfect`, and added notes that `-TGTify` and `-infect` are experimenal.
*    **Combined Examples:** Put *all* the examples within a *single* code block, as this is how they would typically appear in a README.  This makes it easier for users to copy and try them.
*   **Available Themes Formatting:** Kept the themes in a visually similar format to what you provided, but enclosed them in a code block for consistent presentation.
*   **`-v` and `--version`:** Included.
*  **Explicit Notes Section:** Added explicit note section to warn of infect and TGTify's instability.
*   **Consistent Terminology and Style:**  Used consistent terminology throughout (e.g., "script" instead of sometimes "script file").
*   **Removed Redundancy:** Removed the extra spaces in your original input, which are not needed in Markdown.
* Added help command to the argument list


## License

Creative Commons Attribution-ShareAlike 4.0 International License. (https://creativecommons.org/licenses/by-sa/4.0/)

## Brought to you by:

**JUSTIN from the land of FALCONTECHNIX**

**AND**

**GEMINI ADVANCED**
