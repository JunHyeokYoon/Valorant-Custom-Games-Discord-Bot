import discord
from discord.ext import commands
import random
import time

intents = discord.Intents().default()
intents.members = True
client = commands.Bot(intents=intents, command_prefix = '!')
TOKEN = ""

@client.command(name = "customs")
async def customs(ctx):
    lobbyid = 0
    team1id = 0
    team2id = 0
    players = []
    for x in ctx.guild.voice_channels:
        if x.name.lower() == "lobby":
            lobbyid = x.id
        if x.name.lower() == "team 1":
            team1id = x.id
        if x.name.lower() == "team 2":
            team2id = x.id

    server = client.get_guild(ctx.guild.id)
    lobby = client.get_channel(lobbyid)
    team1 = client.get_channel(team1id)
    team2 = client.get_channel(team2id)

    if lobbyid != 0:
        if team1id != 0:
            if team2id != 0:
                if len(lobby.members)%2 == 1:
                    await ctx.send("There is an uneven amount of teams")
                elif len(lobby.members)%2 == 0 and len(lobby.members) > 0:
                    await ctx.send("Thank you for using Yooniverse's Customs Bot.\nLet the party begin")
                    for x in lobby.members:
                        players.append(x)

                    Team1Players = random.sample(players, int(len(lobby.members)/2))
                    Team2Players = []
                    for x in players:
                        if x not in Team1Players:
                            Team2Players.append(x)
                    await ctx.send("Team 1:")
                    time.sleep(2)

                    for x in Team1Players:
                        await ctx.send(x.name)
                    time.sleep(2)
                    await ctx.send("Team 2:")
                    time.sleep(2)
                    for x in Team2Players:
                        await ctx.send(x.name)
                    time.sleep(2)

                    print(Team1Players)
                    print(Team2Players)

                    await ctx.send("Teams will be split in 5 seconds")
                    for x in range(5):
                        await ctx.send(5 - x)
                        time.sleep(1)

                    # Team 1
                    for x in Team1Players:
                        user = server.get_member(x.id)
                        await user.move_to(team1)

                    # Team 2
                    for x in Team2Players:
                        user = server.get_member(x.id)
                        await user.move_to(team2)


                elif len(lobby.members) == 0:
                    await ctx.send("There is no one in the lobby voice channel")
            else:
                await ctx.send("team 2 voice channel does not exists")
        else:
            await ctx.send("team 1 voice channel does not exist")
    else:
        await ctx.send("Lobby voice channel does not exist")

@client.command(name = "lobby")
async def lobby(ctx):
    lobbyid = 0
    team1id = 0
    team2id = 0
    for x in ctx.guild.voice_channels:
        if x.name.lower() == "lobby":
            lobbyid = x.id
        if x.name.lower() == "team 1":
            team1id = x.id
        if x.name.lower() == "team 2":
            team2id = x.id
    server = client.get_guild(ctx.guild.id)
    lobby = client.get_channel(lobbyid)
    team1 = client.get_channel(team1id)
    team2 = client.get_channel(team2id)

    players = []
    for x in team1.members:
        players.append(x.id)
    for x in team2.members:
        players.append(x.id)

    for x in players:
        user = server.get_member(x)
        await user.move_to(lobby)

@client.command(name = "valmap")
async def valmap(ctx):
    maps = ["Breeze", "Bind", "Haven", "Ascent", "Ice Box", "Split"]
    await ctx.send(random.sample(maps, 1))


client.run(TOKEN)
