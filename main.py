from aiogram import Bot, Dispatcher, executor

bot = Bot(token='5335720245:AAHOQ2pJ3aStC0_5rIDsdoHRCFT18LTiXcg')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message):
    await bot.send_message(message.chat.id, "Hi, im calculator, enter something")


@dp.message_handler()
async def start_command(message):
    inp = message.text
    try:
        req = inp
        if req == "":
            return
        # волшебная функция калькулятора) - eval

        total = (str(eval(req)))
        await bot.send_message(message.chat.id, total)
    except (KeyboardInterrupt, EOFError, NameError, SyntaxError, TypeError):
        await bot.send_message(message.chat.id, 'Нельзя использовать что-то')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
