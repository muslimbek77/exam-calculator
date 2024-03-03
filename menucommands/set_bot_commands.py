from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/sardor", description="Botni ishga tushirish"),
        BotCommand(command="/uka", description="Yordam"),
        BotCommand(command="/qaleysan", description="Nima gap, hay"),

    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())