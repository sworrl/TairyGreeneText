Tairy Greene Text (TGT)


What is Tairy Greene Text?
Tairy Greene Text (or simply TGT) is a fun command-line tool that allows you to colorize text output in your terminal with a variety of vibrant and amusing themes. Inspired by the colorful world of Tim and Eric Awesome Show, Great Job!, TGT brings a touch of psychedelic flair to your everyday command-line experience. Whether you want to make your logs more visually interesting, add some personality to your scripts, or just have a laugh with the "Beef Floater" theme, TGT has you covered.

Script Name (Human): Tairy Greene Text
Script Name (Command): TGT
Version: 2.0
Codename: Maximum Yelling!

Table of Contents
Installation
Usage
Basic Usage
Piped Input
Specifying a Theme
Showing All Themes
Installing the Script
Uninstalling the Script
TGTifying a Script (Caution)
Infecting a Script with a Theme (Caution)
Disinfecting a Script
Showing Version
Help
Available Themes
License
Brought To You By
Installation
To use TGT, you first need to download the script. You can do this by cloning the repository or downloading the TGT.py file directly.

Once you have the script, you can make it executable:

Bash

chmod +x TGT.py
Optional Installation (for system-wide access):

You can install TGT to /usr/local/bin/tgt so that you can run it from anywhere in your terminal without needing to be in the script's directory.

Bash

sudo cp TGT.py /usr/local/bin/tgt
sudo chmod +x /usr/local/bin/tgt
After installation, you can simply use the command tgt followed by the arguments.

To install using the script's built-in option:

Bash

./TGT.py -install
or if installed system-wide:

Bash

tgt -install
Note: The -install and -uninstall features are placeholders in this version and do not currently perform the actual file system operations. You will need to manually copy the script as described above for system-wide installation.

Usage
TGT is a command-line tool that accepts text as input and outputs it with colorful themes. Here are the different ways you can use it:

Basic Usage
To colorize text directly from the command line, simply run the script followed by the text you want to colorize:

Bash

./TGT.py "Hello World!"
or if installed system-wide:

Bash

tgt "Hello World!"
By default, if no theme is specified, a random theme will be applied.

Piped Input
You can also pipe input to TGT from other commands:

Bash

echo "This text is piped" | ./TGT.py
or

Bash

cat my_log_file.txt | tgt
Again, a random theme will be used if you don't specify one.

Specifying a Theme
To use a specific color theme, use the -theme argument followed by the theme name (case-insensitive):

Bash

./TGT.py -theme "fire" "This text is on fire!"
or

Bash

tgt -theme "ocean" "Dive into a sea of colors."
You can find a list of all available themes in the Available Themes section.

Showing All Themes
To see examples of all the available themes with funny themed sentences, use the -all flag:

Bash

./TGT.py -all
or

Bash

tgt -all
This will clear your terminal and display each theme with a sample sentence in its respective colors.

Installing the Script
As mentioned in the Installation section, you can attempt to use the built-in install command:

Bash

./TGT.py -install
or

Bash

tgt -install
Note: This feature is a placeholder and does not currently perform the installation.

Uninstalling the Script
Similarly, there's an uninstall command:

Bash

./TGT.py -uninstall
or

Bash

tgt -uninstall
Note: This feature is also a placeholder and does not currently perform the uninstallation. You would need to manually remove the script if you installed it system-wide.

TGTifying a Script (Caution)
The -TGTify option allows you to execute another script and colorize its output using a specified theme.

Bash

./TGT.py -TGTify ./my_script.sh -theme "fire"
or

Bash

tgt -TGTify ./my_script.sh -theme "neon"
Warning: The -TGTify feature is currently under development and might not work as expected in all scenarios. Use with caution.

Infecting a Script with a Theme (Caution)
The -infect option attempts to modify an existing Python script by replacing placeholder function calls with the actual color codes for a given theme. This is intended for embedding TGT's colorization directly into another script.

Important: This feature modifies the original script file. It is highly recommended to use version control (like Git) before attempting to infect a script.

Usage:

Bash

./TGT.py -infect ./my_other_script.py -theme "neon"
or

Bash

tgt -infect ./my_other_script.py -theme "ocean"
Your target script would need to have placeholder function calls in the format tgt_placeholder("text", "theme") for this feature to work.

Warning: The -infect feature is currently under development and might lead to unexpected behavior or script corruption. Use with extreme caution and ensure you have backups of your scripts.

Disinfecting a Script
The -disinfect option attempts to remove any TGT color codes that were previously injected into a Python script using the -infect option.

Usage:

Bash

./TGT.py -disinfect ./my_infected_script.py
or

Bash

tgt -disinfect ./my_infected_script.py
Warning: This feature modifies the original script file. It is recommended to use version control before disinfecting a script.

Showing Version
To display the script's version and codename, use the -v or --version flag:

Bash

./TGT.py -version
or

Bash

tgt --version
Help
To see the help message with usage instructions and available options, use the -h or --help flag:

Bash

./TGT.py -h
or

Bash

tgt --help
Available Themes
Here is a list of the available color themes in Tairy Greene Text:

fire
ice
earth
rainbow
forest
ocean
seafoam
usa
easter
fart
sprite
pepsi
windows 98
windows xp
macos
xbox
playstation
bigfoot
dankpods
alien
mardi gras
gunmetal
google
gemini
sunset
mint
cyberpunk
coffee
strawberry
lavender
neon
autumnal
70s
80s
90s
darkness
midnight
shadow
obsidian
nightsky
deepsea
tairy greene
beef floater
diarrhea times
pills
wet asphalt
tv static
grape soda
lime jello
blue raspberry
cotton candy
circuit board
toxic waste
ALL US STATES (Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming)   
License
This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. You are free to share and adapt this work as long as you give appropriate credit and distribute your contributions under the same license. For more details, see https://creativecommons.org/licenses/by-sa/4.0/.   

Brought To You By
This awesome script was brought to you by:

JUSTIN FALCONTECHNIX
and
GEMINI ADVANCED
