# discord_py_pisg
An extension for the discord.py Discord bot allowing exporting logs in pisg mbot format

This extension for Discord.py allows one to write logfiles of Discord channels in the mbot format. 
Resulting logiles can be used as input for pisg (perl irc statistics generator) as follows:
```
pisg -f mbot -o <outputdir>/<filename.html> -ch \#<channelname> -l <logfile>
```
As the extension creates a different logfile per channel (with a channelname after the _ character), one can iterate through the logfiles as follows:
```
#!/bin/bash

INPUTDIR="<logdir>"
OUTPUTDIR="<pisg-output-dir>"

for f in $INPUTDIR/*; do
    channel=$(echo $f | cut -d'_' -f 2)
        pisg -f mbot -o $OUTPUTDIR/$channel.html -ch \#$channel -l $f
done
```
