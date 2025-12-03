from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

API_TOKEN = "8474331460:AAG7hnxWCnNK-HBFTlQeTe7PHsFTk5KEIMM"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

programs = {
    "программа тренировок вверх низ": "Грудь + Спина\n"
    "1.Жим штанги лёжа в наклоне — 4x6-8\n"
    "2.Тяга т грифа— 4x8\n"
    "3.Жим в тренажёре горизонтальный — 3x10\n"
    "4.Тяга горизонтального блока — 3x10-12\n"
    "5.Гиперэкстензия — 3x12-15\n\n"
    "Плечи + Руки\n"
    "1.Жим гантелей сидя — 3x8-10\n"
    "2.Махи в тренажёре — 3x12-15\n"
    "3.Пек дек на задние дельты — 3x15\n"
    "4.Сгибания рук co штангой — 3x10-12\n"
    "5.Разгибания рук на верхнем блоке — 3x10-12\n"
    "6.Молотковые сгибания — 2x12-15\n\n"
    "Низ\n"
    "1.Гакк присед — 3x8-10\n"
    "2.Разгибания ног — 3x12\n"
    "3.Сгибания ног — 3x12\n"
    "4.Разведения ног — 3x15\n"
    "5.Гиперэкстензия — 3x12-15\n\n"
    "Вверх\n"
    "1.Жим гантелей лёжа (горизонтальная) — 4x8\n"
    "2.Подтягивания/тяга блока — 3xoткaз\n"
    "3.Тяга гантели (одной рукой) — 3x10\n"
    "4.Жим хаммер под углом вверх — 3x10\n"
    "5.Махи гантелей в стороны — 3x12-15\n"
    "7.Сгибания&разгибания рук c канатом-2x12-15\n",
    "программа тренировок сплит": "грудь (тяжёлая) + трицепс\n"
    "1.Жим штанги лёжа/в наклоне- 4x6-8\n"
    "2.Жим гантелей лёжа/в наклоне- 3x8-10\n"
    "3.Брусья- 3x8-12\n"
    "4.Французский жим - 3x10-12\n"
    "5.Разгибания на блоке (канат)-3x12-15\n\n"
    "ноги+плечи\n"
    "1.Приседания - 4x6-8\n"
    "2.Сгибание ног - 3x12\n"
    "3.Жим гантелей  плечи - 3x10\n"
    "4.Махи в стороны - 3x15\n\n"
    "спина + бицепс +лёгкая грудь\n"
    "1.Тяга штанги к поясу - 4x6-8\n"
    "2.Подтягивания/тяга блока - 3x10\n"
    "3.Тяга гантели одной рукой - 3x12\n"
    "4.Сгибания рук(Скотт/гантели)-3x10-12\n"
    "5.Жим гантелей лёжа (лёгкий) - 2x12\n"
    "6.Отжимания (по желанию) - 1-2xмaкc\n",
    "программа тренировок вверх/низ 3 дня": "Спина, Грудь, Бицепс\n"
    "1.Тяга штанги к поясу: 4x6-8\n"
    "2.Подтягивания/тяга верхнего блока: 3x8-10\n"
    "3.Жим гантелей в наклоне: 3x8-10\n"
    "4.Брусья: 3x8-12\n"
    "5.Сгибания рук c гантелями: 3x8-10\n"
    "6.Молотковые сгибания: 3x10-12\n\n"
    "Ноги, Плечи, Трицепс\n"
    "1.Приседания co штангой\n"
    "•Разминка: 2x12-15\n"
    "•Рабочие подходы: 3x6-8\n"
    "2.Сгибание на зпб: 3x10-12\n"
    "3.Жим на передние дельты: 3x10-12\n"
    "4.Махи в стороны c гантелями: 4x12-15\n"
    "5.Французский жим: 2x10-12\n"
    "6.Разгибания на блоке c канатом: 3x12-15\n\n"
    "Грудь, Спина, Руки\n"
    "1.Жим штанги на наклонной: 4x5-8\n"
    "2.Жим гантелей на наклонной: 3x10-12\n"
    "3.Тяга гантели одной рукой: 3x10-12\n"
    "4.Тяга гантелей к поясу на лавке: 3x10-12\n"
    "5.суперсет:\n"
    "•Французский жим: 3x10-12\n"
    "•Сгибания на скамье Скотта: 3x10-12\n"
    "6.суперсет:\n"
    "•Разгибания на блоке: 2x12-15\n"
    "•Молотковые сгибания: 2x12-15\n",
    "программа тренировок вверх/низ 4 дня": "Вверх\n"
    "1.Жим штанги лёжа в наклоне — 3x8\n"
    "2.Тяга гантели в наклоне — 3x10\n"
    "3.Сгибание рук на скамье Скотта — 3x10-12\n"
    "4.Махи на среднюю дельту - 3x12\n"
    "5.Махи на заднюю дельту - 3x15\n\n"
    "Вверх\n"
    "1.Жим штанги лёжа в наклоне - 4x6\n"
    "2.Жим гантелей лёжа в наклоне - 3x8-10\n"
    "3.Подтягивания широким хватом - 3 x отказ\n"
    "4.Тяга гантели в наклоне - 2-3x10\n"
    "5.Французский жим - 3x10-12\n"
    "6.Разгибания на блоке - 2 x отказ\n"
    "7.Сгибание рук на наклонной скамье 2x10-12\n\n"
    "Низ\n"
    "1.Приседания - 4x6-8\n"
    "2.Сгибание ног - 3x12\n"
    "3.Махи в стороны - 3x15\n"
    "4.Жим гантелей  плечи - 3x10\n"
    "5.Молотки - 3x12-15\n"
    "6.Скручивания c весом - 2 x 12\n\n"
    "Вверх\n"
    "1.Тяга штанги к поясу - 4x6-8\n"
    "2.Тяга блока обратным хватом - 2-3x10-12\n"
    "3.Жим гантелей на горизонт.л. - 3x6-8\n"
    "4.Жим гантелей на наклонной.л.-2x10-12\n"
    "5.Брусья- 1 отказ\n"
    "6.Сгибания рук Скотт штангой-2x10-12\n",
}
playlist = {
    "testosterone bust": "https://on.soundcloud.com/dkR06HILCho8TSahkX",
    "real.": "https://on.soundcloud.com/Tfm8o7cXh5oVlhP3to",
    "endless self improvement": "https://on.soundcloud.com/Zh8aDwfrUfQ49nFdfn",
    "для мужчин в качалку": "https://on.soundcloud.com/GqXWeHX0ITK258mDIz",
    "Thoughts kill.": "https://on.soundcloud.com/iKDars517vf65FKdiE",
    "aesthetic": "https://on.soundcloud.com/oYQP6fxD1eJx8sAmr0",
}


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Приветствую, выбери категории ниже")

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="тренировки", callback_data="category_trainings"
                )
            ],
            [InlineKeyboardButton(text="Плейлисты", callback_data="category_playlist")],
        ]
    )

    await message.answer(
        "Выбери что тебе нужно: программы тренировок или плейлисты для зала",
        reply_markup=keyboard,
    )


@dp.callback_query(lambda c: c.data == "category_trainings")
async def show_trainings(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f"prog_{i}")]
            for i, name in enumerate(programs.keys())
        ]
    )
    await callback.message.answer("Выбери программу тренировок:", reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(lambda c: c.data == "category_playlist")
async def show_playlist(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f"pl_{i}")]
            for i, name in enumerate(playlist.keys())
        ]
    )
    await callback.message.answer("Выбери плейлист:", reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(lambda c: c.data.startswith("prog_"))
async def send_program(callback: types.CallbackQuery):
    index = int(callback.data.replace("prog_", ""))
    key = list(programs.keys())[index]
    await callback.message.answer(programs[key])
    await callback.answer()


@dp.callback_query(lambda c: c.data.startswith("pl_"))
async def send_playlist(callback: types.CallbackQuery):
    index = int(callback.data.replace("pl_", ""))
    key = list(playlist.keys())[index]
    await callback.message.answer(playlist[key])
    await callback.answer()


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
