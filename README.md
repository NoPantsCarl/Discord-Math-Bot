# Discord-Exp-Math-Bot

This bot was set up for finding out how many "gigas" take to kill to get to max level when i was playing Ark. As i was breeding gigas and had a player shop that would sell an exp services; so this bot allow people to know many gigas to order to kill.

However you can change "gigas" to something else and change the total required exp per level in the config.json

Instructions for usage:
1. Place all the files in the same directory.
2. Get Python3.
3. Run: "python3 -m pip install discord.py" OR "py -m pip install discord.py" (second one if first one gives command not found)
4. Open bot.py and go to the end. Replace the bot token with your own bot token.
5. Head to the directory you have placed the files in. Run "python3 bot.py" OR "py bot.py"
6. Commands:
- ?convert <current level> <final level>
- ?config <setting> <value>

Check config.json for setting names. For e.g, usage could be:

?config giga_val 35035
?config giga_format {mention} You need **{gigas}** gigas.

This can be directly modified into config.json itself as well.
