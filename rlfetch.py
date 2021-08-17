# READ THE DESC. IM A BEGGINER PROGRAMMER, TWENTY DAYS OF PRACTICE; AND THIS CODE PROBABLY ISN'T WELL TYPED. BUT IM CURRENTLY IMPROVING IT.

# Cooming soon: cli command, custom distros, custom icons, custom colors, config file, more personalization, uility and so much more!, Rl 08/17/21, GNU PUBLIC LICENSE v3.0

# Info module

import platform

# Ansi codes

red = "\033[0;31m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
green = "\033[0;32m"
magenta = "\033[0;35m"
gray = "\033[0;37m"
empty = "\033[0;30m"

# Miscellaneous

error = "\033[1;31m"
end = "\033[0m"

# Logos

tux01 = f"             {empty}.888888:.{end}"
tux02 = f"             {empty}88888.888.{end}"
tux03 = f"            {empty}.8888888888{end}"
tux04 = f"            {empty}8'{end} {empty}`88'{end} {empty}`888{end}"
tux05 = f"            {empty}8{end} {blue}8{end} {empty}88{end} {blue}8{end} {empty}888{end}"
tux06 = f"            {empty}8:.{end}{yellow},::,{end}{empty}.:888{end}"
tux07 = f"           {empty}.8{end}{yellow}`::::::{end}{empty}'888{end}"
tux08 = f"           {empty}88{end}  {yellow}`::'  {empty}888{end}"
tux09 = f"          {empty}.88{end}        {empty}`888.{end}"
tux10 = f"        {empty}.88'{end}   .::.  {empty}.:8888.{end}"
tux11 = f"        {empty}888.'{end}  red :'     {empty}`'88:88.{end}"
tux12 = f"      {empty}.8888'{end}    '        {empty}88:88.{end}"
tux13 = f"      {empty}.8888'{end}    '        {empty}88:88.{end}"
tux14 = f"     {empty}.8888'{end}     .        {empty}88:888{end}"
tux15 = f"     {empty}.8888'{end}     .        {empty}88:888{end}"
tux16 = f"     {empty}`88888{end}     :        {empty}8:888'{end}"
tux17 = f"      {empty}`{end}{yellow}.:.{end}{empty}88{end}    .      {yellow}.::{end}{empty}888'{end}"
tux18 = f"     {yellow}.:::::{end}{empty}88{end}   `      {yellow}.:::::::.{end}"
tux19 = f"     {yellow}.:::::{end}{empty}88{end}   `      {yellow}.:::::::.{end}"
tux20 = f"    {yellow}.::::::.{end}{empty}8{end}         {yellow}.:::::::::{end}"
tux21 = f"    {yellow}:::::::::..{end}     {yellow}.:::::::::'{end}"
tux22 = f"     {yellow}`:::::::::{end}{empty}88888{yellow}:::::::'{end}"
tux23 = f"          {yellow}`:::'{end}       {yellow}`:'{end}"

# Lets go

preference = input("Select the color in which you want the information to be displayed: ")

if preference == "red":
    preference = red

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

elif preference == "yellow":
    preference = yellow

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

elif preference == "blue":
    preference = blue

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

elif preference == "green":
    preference = green

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

elif preference == "magenta":
    preference = magenta

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),
elif preference == "gray":
    preference = gray

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

elif preference == "jeb_":

    print(tux01),
    print(tux02),
    print(tux03),
    print(tux04),
    print(tux05),
    print(tux06),
    print(tux07),
    print(tux08),
    print(tux09),
    print(tux10),
    print(tux11, preference, 'Platform processor:', end, platform.processor()),
    print(tux12, preference, 'Platform architecture:', end, platform.architecture()),
    print(tux13, preference, 'Machine type:', end, platform.machine()),
    print(tux14, preference, 'Network name:', end, platform.node()),
    print(tux15, preference, 'Platform information:', end, platform.platform()),
    print(tux16, preference, 'Operating system:', end, platform.system()),
    print(tux17),
    print(tux18),
    print(tux19),
    print(tux20),
    print(tux21),
    print(tux22),
    print(tux23),

else:

    print(error, "Oops! invalid syntax.")
