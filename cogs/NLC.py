from discord.ext import commands
import os


class LiveCommand(commands.Cog): 
    def __init__(self,bot):
        self.bot = bot
        print("Command cog initiated")

    @commands.command()
    @commands.has_any_role("Admin","Moderators")
    async def live(self, ctx):
        print(ctx.author.id)
        direc=os.getcwd()
        os.startfile(direc+"\\v2.py")

async def setup(bot):
    await bot.add_cog(LiveCommand(bot))