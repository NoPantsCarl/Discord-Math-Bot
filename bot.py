from config import Config
import discord
from pprint import pprint
from discord.ext import commands
import math

config = Config()
bot = commands.Bot(command_prefix='?', help_command=None)

def calculate_gigas(current_level, level_to_reach):
	if current_level == level_to_reach:
		return 0

	level_data = config.get_config("level_req")
	giga_val = config.get_config("giga_val")

	current_level = str(current_level)
	level_to_reach = str(level_to_reach)

	if not current_level in level_data or not level_to_reach in level_data:
		return None

	return math.ceil((level_data[level_to_reach] - level_data[current_level]) / giga_val)

@bot.command()
async def convert(ctx, current_level : int, level_to_reach : int):
	if not isinstance(ctx.channel, discord.TextChannel):
		return

	if current_level < 1 or current_level > 155:
		raise commands.errors.ArgumentParsingError()
	if level_to_reach < 1 or level_to_reach > 155:
		raise commands.errors.ArgumentParsingError()

	gigas = calculate_gigas(current_level, level_to_reach)
	await ctx.channel.send(config.get_config("giga_format").format(gigas=gigas, mention=ctx.author.mention))

@convert.error
async def convert_error(ctx, error):
	if isinstance(error, commands.errors.MissingRequiredArgument) or isinstance(error, commands.errors.ArgumentParsingError) or isinstance(error, commands.errors.BadArgument):
		await ctx.channel.send(config.get_config("convert_usage").format(mention=ctx.author.mention))
		return

	raise error

def check_admin_perms(member):
	if member.guild_permissions.administrator:
		return True

	role = discord.utils.get(member.roles, name=config.get_config("admin_role"))
	if role:
		if role in member.roles:
			return True

	return False

@bot.command(name="config")
async def set_config(ctx, setting : str, *value : str):
	if not isinstance(ctx.channel, discord.TextChannel):
		return

	if not check_admin_perms(ctx.author):
		return

	if setting == "level_req":
		await ctx.channel.send(config.get_config("config_invalid_setting").format(mention=ctx.author.mention))
		return

	value = ' '.join(value)
	
	if setting == "giga_val":
		try:
			value = int(value)
		except ValueError:
			await ctx.channel.send(config.get_config("config_invalid_setting_giga_val").format(mention=ctx.author.mention))
			return

	is_valid = config.get_config(setting)
	if not is_valid:
		await ctx.channel.send(config.get_config("config_invalid_setting").format(mention=ctx.author.mention))
		return

	config.set_config(setting, value)
	await ctx.channel.send(config.get_config("config_success").format(mention=ctx.author.mention))

@set_config.error
async def config_error(ctx, error):
	if isinstance(error, commands.errors.MissingRequiredArgument):
		await ctx.channel.send(config.get_config("config_usage").format(mention=ctx.author.mention))
		return

	raise error

@bot.event
async def on_command_error(ctx, error):
	if hasattr(ctx.command, 'on_error'):
		return

	if isinstance(error, discord.ext.commands.errors.CommandNotFound):
		return

	raise error

bot.run("xyz") # Bot token