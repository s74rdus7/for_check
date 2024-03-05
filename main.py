# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import logging
import markups as nav

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from text import *


logging.basicConfig(level = logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
UAN_TO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=4874b8c2ba1eebb0&sxsrf=ACQVn09JeF4tJFkO9cR_BrWQXyERf-YdsQ%3A1708083305338&ei=aUjPZe2ZFPjBp84Pq6eWqA0&udm=&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0&gs_lp=Egxnd3Mtd2l6LXNlcnAiDdC60YPRgNGBINGO0LAqAggAMg8QIxiABBiKBRgnGEYYggIyChAAGIAEGIoFGEMyDRAAGIAEGIoFGEMYsQMyChAAGIAEGBQYhwIyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyGRAAGIAEGIoFGEYYggIYlwUYjAUY3QTYAQFIyg1QsgVY-QdwAXgBkAEAmAGSAaABngKqAQMwLjK4AQPIAQD4AQHCAgoQABhHGNYEGLADwgINEAAYgAQYigUYQxiwA8ICChAjGIAEGIoFGCeIBgGQBgq6BgYIARABGBM&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'}


def get_actual_course(): # Узнать актуальный курс юаня к рублю
	full_page = requests.get(UAN_TO_RUB, headers=headers)
	soup = BeautifulSoup(full_page.content, 'html.parser')
	convert = soup.findAll('span', {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
	return convert[0].text


######################################################################################################################################
# СТАРТОВЫЕ ФУНКЦИИ


@dp.message_handler(commands = ['start']) # Стартовая функция, проверяет, подписан ли человек
async def start(message: types.Message):
	result = await bot.get_chat_member(chat_id='@stop_alenb', user_id=message.from_user.id) # @stop_alenb - адрес канала
	if str(result.status) != 'left':
		await bot.send_message(message.from_user.id, hello_text, reply_markup=nav.inl_btn_main_menu_markup)
	else:
		await bot.send_message(message.from_user.id, 'Вы не подписаны на канал, пожалуйста подпишитесь и проверьте', reply_markup=nav.inl_btn_check_sub_markup)


@dp.callback_query_handler(text="check_sub") # Проверяет, подписан ли человек
async def check_sub(call: types.CallbackQuery):
	result = await bot.get_chat_member(chat_id='@stop_alenb', user_id=call.from_user.id) # @stop_alenb - адрес канала
	if str(result.status) != 'left':
		await bot.send_message(call.from_user.id, hello_text, reply_markup=nav.inl_btn_main_menu_markup)
	else:
		await bot.send_message(call.from_user.id, 'Вы не подписаны на канал, пожалуйста подпишитесь и проверьте', reply_markup=nav.inl_btn_check_sub_markup)


######################################################################################################################################
# КНОПКИ "ГЛАВНОЕ МЕНЮ"		


@dp.callback_query_handler(text=["how_to_use_poizon", "take_price", "actual_course", "answers", "contact_to_manager", "back_to_main"])
async def how_to_use(call: types.CallbackQuery):
	result = await bot.get_chat_member(chat_id='@stop_alenb', user_id=call.from_user.id) # @stop_alenb - адрес канала
	if str(result.status) != 'left':
		await bot.delete_message(call.from_user.id, call.message.message_id)
		if call.data == "back_to_main": # Кнопка назад
			await bot.send_message(call.from_user.id, hello_text, reply_markup=nav.inl_btn_main_menu_markup)
		elif call.data == "how_to_use_poizon": # Как пользоваться
			await bot.send_message(call.from_user.id, how_to_use_poizon, reply_markup=nav.inl_menu_how_to_use)
		elif call.data == "take_price": # Рассчитать стоимость
			await bot.send_message(call.from_user.id, 'Еще не работает', reply_markup=nav.inl_btn_main_menu_markup)
		elif call.data == "actual_course": # Актуальный курс
			await bot.send_message(call.from_user.id, f'Курс на сегодня: \n\n 1¥ = {get_actual_course()}₽', reply_markup=nav.inl_menu_actual_course)
		elif call.data == "answers": # Ответы на вопросы
			await bot.send_message(call.from_user.id, answers, reply_markup=nav.inl_menu_answers)
		# elif call.data == "contact_to_manager": # Связаться с менеджером
		# 	await bot.send_message(call.from_user.id, 'Еще не работает', reply_markup=nav.inl_btn_main_menu_markup)
	else:
		await bot.send_message(call.from_user.id, 'Вы не подписаны на канал, пожалуйста подпишитесь и проверьте', reply_markup=nav.inl_btn_check_sub_markup)


######################################################################################################################################


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)