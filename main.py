from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import os
from dotenv import load_dotenv

from data.programs import programs
from data.playlist import playlist

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    print("ОШИБКА: He найден BOT_TOKEN в .env файле!")
    print("Создай файл .env в той же папке и добавь туда: BOT_TOKEN=твoй_тoкeн")
    exit(1)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Программы тренировок")],
        [KeyboardButton(text="Плейлисты для зала")],
        [KeyboardButton(text="О боте")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери действие",
)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "Добро пожаловать в бота для тренировок\n" "Выбери нужный раздел в меню ниже:"
    )
    await message.answer(welcome_text, reply_markup=main_menu)


def get_programs_keyboard():
    buttons = []
    for name in programs.keys():
        buttons.append([KeyboardButton(text=name)])

    buttons.append([KeyboardButton(text="Назад в меню")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выбери программу тренировок",
    )


def get_playlists_keyboard():
    buttons = []
    for name in playlist.keys():
        buttons.append([KeyboardButton(text=name)])

    buttons.append([KeyboardButton(text="Назад в меню")])

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выбери плейлист",
    )


back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад в меню", callback_data="back_to_main")]
    ]
)


@dp.message(lambda message: message.text == "Программы тренировок")
async def show_programs_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f"prog_{i}")]
            for i, name in enumerate(programs.keys())
        ]
    )
    await message.answer(
        "Выбери программу тренировок:", reply_markup=get_programs_keyboard()
    )


@dp.message(lambda message: message.text == "Плейлисты для зала")
async def show_playlists_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=name, callback_data=f"pl_{i}")]
            for i, name in enumerate(playlist.keys())
        ]
    )
    await message.answer("Выбери плейлист:", reply_markup=get_playlists_keyboard())


@dp.message(lambda message: message.text == "О боте")
async def about_bot(message: types.Message):
    about_text = (
        "О боте:\n"
        "Этот бот создан для помощи в тренировках\n"
        "Здесь ты найдешь:\n\n"
        "1. Программы тренировок\n"
        "2. Плейлисты для зала\n\n"
        "Используй меню для навигации по боту\n\n"
        "Для возврата в главное меню используй команду:  /start"
    )
    await message.answer(about_text)


@dp.message(lambda message: message.text in programs.keys())
async def send_program_message(message: types.Message):
    program_text = programs[message.text]
    await message.answer(program_text, reply_markup=get_programs_keyboard())


@dp.message(lambda message: message.text in playlist.keys())
async def send_playlist_message(message: types.Message):
    playlist_link = playlist[message.text]
    await message.answer(playlist_link, reply_markup=get_playlists_keyboard())


@dp.message(lambda message: message.text == "Назад в меню")
async def back_to_main_menu(message: types.Message):
    await message.answer("Возврат в главное меню:", reply_markup=main_menu)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
