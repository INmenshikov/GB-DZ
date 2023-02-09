import game
from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n '
                         f'Я скучал!\n'
                         f'Давай разделим наши конфеты в игровой форме!\n'
                         f'Напиши"/max (число конфет)" чтобы уточнить их общее количество.')


@dp.message_handler(commands=['max'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        try:
            count = int(message.text.split()[1])
            await message.answer(f'{message.from_user.full_name}\nМы начинаем играть . Бери от 1 до 28.\n'
                                 f'У нас {count} конфет\n'
                                 f'Выйграет то кто заберет последнюю конфету.')
            my_game = [message.from_user.id, message.from_user.first_name, count]
            game.total.append(my_game)
        except:
            await message.answer(f'{message.from_user.full_name}\n'
                                 f'Мы начинаем играть . Бери от 1 до 28.\n'
                                 f'У нас 150 конфет\n'
                                 f'Выйграет то кто заберет последнюю конфету.')
            my_game = [message.from_user.id, message.from_user.first_name, 150]
            game.total.append(my_game)
