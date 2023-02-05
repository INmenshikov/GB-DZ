from loader import dp, bot
from aiogram import types

general_candies = 150

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n '
                         f'Я скучал!\n'
                         f'Давай разделим наши конфеты в игровой форме!\n'
                         f'Напиши"/set (число конфет)" чтобы уточнить их общее количество.\n'
                         f'Но не меньше 100')

@dp.message_handler(commands=['set'])
async def mes_sef(message: types.Message):
    global general_candies
    try:
        count = message.text.split()[1]
        general_candies = int(count)
        if general_candies < 100:
            general_candies = 100
        await message.answer(f"Приступим. У нас {general_candies} конфет. \n Правила:\n"
                            f"За один ход можно забрать не более чем 28 конфет.\n "
                            f"Все конфеты оппонента достаются сделавшему последний ход.\n"
                            f"Сколько конфет ты берешь? ")
    except:
        await message.answer(f'Если у нас не будет кофет мы не сможем поиграть\n'
                             f'Напиши"/set (число конфет)" чтобы уточнить их общее количество.')

@dp.message_handler(commands=['OOP'])
async def mes_oop(message: types.Message):
    await message.answer('Да что выговорите')

@dp.message_handler(text=['лох', 'Лох', 'ЛОХ'])
async def mes_loh(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(f'Сам такой!')

@dp.message_handler()
async def mes_all(message: types.Message):
    global general_candies
    if message.text.isdigit():
        if general_candies > 56:
            if int(message.text) > 28:
                await message.answer("Не больше 28 конфет за раз. Не хорошо нарушать правила.\n"
                                     "будем считать что ты взял 28")
                message.text = 28
            general_candies -= int(message.text)
            await bot.send_message(message.from_user.id, f'Конфет осталось {general_candies}')
            c = int(general_candies / 28)
            if general_candies > c * 28:
                number_candies = (general_candies - (c * 28)) - 1
                if number_candies == 0:
                    number_candies = 28
                general_candies -= number_candies
            else:
                number_candies = 28
                general_candies -= number_candies
            await bot.send_message(message.from_user.id, f'Я взял {number_candies} конфет.\n'
                                                         f'Конфет осталось {general_candies}')
        else:
            await bot.send_message(message.from_user.id, f"Это была хорошая игра\n"
                                                         f"Так как конфеты я не ем! Они все достаются тебе!")

    else:
        await bot.send_message(message.from_user.id, f'Введие число или Напиши"/start" чтобы прочитать правила.')










