import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!succ"):
        msg = 'When she succ me'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'https://img.ifcdn.com/images/06a288a21ce16c2affb286c65a579d6960ab8e0b3b672d222b412895ba2211f2_1.jpg'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!orgasm"):
        msg = '!play https://youtu.be/BBXelaY2g7g?t=13'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def cmd_summon(self, channel, author, voice_channel):
        """
        Usage:
            {command_prefix}summon

        Call the bot to the summoner's voice channel.
        """

        if not author.voice_channel:
            raise exceptions.CommandError('You are not in a voice channel!')

        voice_client = self.the_voice_clients.get(channel.server.id, None)
        if voice_client and voice_client.channel.server == author.voice_channel.server:
            await self.move_voice_client(author.voice_channel)
            return

        # move to _verify_vc_perms?
        chperms = author.voice_channel.permissions_for(author.voice_channel.server.me)

        if not chperms.connect:
            self.safe_print("Cannot join channel "%s", no permission." % author.voice_channel.name)
            return Response("" % author.voice_channel.name,
                delete_after=25
            )

        elif not chperms.speak:
            self.safe_print("Will not join channel "%s", no permission to speak." % author.voice_channel.name)
            return Response("" % author.voice_channel.name,
                delete_after=25

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('Mjg0NzAxNTY5NDk5MjY3MDcz.C5Hcsw.NRH8BJArnkAxD7ElmQ8NLWwRuII')
