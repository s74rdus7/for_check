from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


inl_btn_check_sub = InlineKeyboardButton(text = "Проверить подписку ✅", callback_data = "check_sub")
inl_btn_check_sub_markup = InlineKeyboardMarkup(row_width=1).insert(inl_btn_check_sub)

######################################################################################################################################
# КНОПКИ "ГЛАВНОГО МЕНЮ"	

inl_btn_how_to_use_poizon = InlineKeyboardButton(text = "👉 Как пользоваться Poizon 👈", callback_data = "how_to_use_poizon")
inl_btn_take_price = InlineKeyboardButton(text = "Рассчитать стоимость 📲", callback_data = "take_price")
inl_btn_actual_question = InlineKeyboardButton(text = "Актуальный курс 📈", callback_data = "actual_course")
inl_btn_answers = InlineKeyboardButton(text = "Ответы на вопросы 💬", callback_data = "answers")
inl_btn_contact_to_manager = InlineKeyboardButton(text = "Связаться с менеджером 👤", url = "https://t.me/mmv_enjoyer")
inl_btn_main_menu_markup = InlineKeyboardMarkup(row_width=1).insert(inl_btn_how_to_use_poizon).insert(inl_btn_take_price).insert(inl_btn_actual_question).insert(inl_btn_answers).insert(inl_btn_contact_to_manager)


######################################################################################################################################
# КНОПКИ "КАК ПОЛЬЗОВАТЬСЯ"	

inl_btn_how_to_use_url_for_ios = InlineKeyboardButton(text = "Ссылка для скачивания | iOS", callback_data = "how_to_use_url_for_ios")
inl_btn_how_to_use_url_for_android = InlineKeyboardButton(text = "Ссылка для скачивания | Android", callback_data = "how_to_use_url_for_android")
inl_btn_how_to_use_register_in_app = InlineKeyboardButton(text = "Регистрация в приложении", callback_data = "how_to_use_register_in_app")
inl_btn_how_to_use_find_by_photo = InlineKeyboardButton(text = "Поиск по фото", callback_data = "how_to_use_find_by_photo")
inl_btn_how_to_use_brand_store = InlineKeyboardButton(text = "Магазин брендов", callback_data = "how_to_use_brand_store")
inl_btn_how_to_use_find_and_filters = InlineKeyboardButton(text = "Поиск и фильтры", callback_data = "how_to_use_find_and_filters")
inl_btn_how_to_use_select_size = InlineKeyboardButton(text = "Как выбрать размер", callback_data = "how_to_use_select_size")
inl_btn_how_to_use_buttons_labeling = InlineKeyboardButton(text = "Обозначения кнопок", callback_data = "how_to_use_buttons_labeling")
inl_btn_how_to_use_qr_code_check = InlineKeyboardButton(text = "Проверка QR-кода", callback_data = "how_to_use_qr_code_check")
inl_btn_how_to_use_back = InlineKeyboardButton(text = "Назад ↩️", callback_data = "back_to_main")
inl_menu_how_to_use = InlineKeyboardMarkup(row_width=1).insert(inl_btn_how_to_use_url_for_ios).insert(inl_btn_how_to_use_url_for_android).insert(inl_btn_how_to_use_register_in_app)
inl_menu_how_to_use.insert(inl_btn_how_to_use_find_by_photo).insert(inl_btn_how_to_use_brand_store).insert(inl_btn_how_to_use_find_and_filters)
inl_menu_how_to_use.insert(inl_btn_how_to_use_select_size).insert(inl_btn_how_to_use_buttons_labeling).insert(inl_btn_how_to_use_qr_code_check).insert(inl_btn_how_to_use_back)

######################################################################################################################################
# КНОПКИ "АКТУАЛЬНЫЙ КУРС"

inl_btn_actual_course_why_so_big = InlineKeyboardButton(text = "Почему курс выше ЦБ? 🤬", callback_data = "actual_course_why_so_big")
inl_btn_how_to_use_back = InlineKeyboardButton(text = "Назад ↩️", callback_data = "back_to_main")
inl_menu_actual_course = InlineKeyboardMarkup(row_width=1).insert(inl_btn_actual_course_why_so_big).insert(inl_btn_how_to_use_back)


######################################################################################################################################
# КНОПКИ "ОТВЕТЫ НА ВОПРОСЫ"

inl_btn_answers_what_is_poizon = InlineKeyboardButton(text = "Что за Poizon?", callback_data = "answers_what_is_poizon")
inl_btn_answers_delivery_time = InlineKeyboardButton(text = "Какие сроки доставки?", callback_data = "answers_delivery_time")
inl_btn_answers_why_us = InlineKeyboardButton(text = "Почему нам можно доверять?", callback_data = "answers_why_us")
inl_btn_answers_can_pay_when_dev = InlineKeyboardButton(text = "Можно ли оплатить при получении?", callback_data = "answers_can_pay_when_dev")
inl_btn_answers_not_my_size = InlineKeyboardButton(text = "Что делать, если не подошел размер", callback_data = "answers_not_my_size")
inl_btn_answers_delivery_for_alot_things = InlineKeyboardButton(text = "Доставка на несколько вещей", callback_data = "answers_delivery_for_alot_things")
inl_menu_answers = InlineKeyboardMarkup(row_width=1).insert(inl_btn_answers_what_is_poizon).insert(inl_btn_answers_delivery_time)
inl_menu_answers.insert(inl_btn_answers_why_us).insert(inl_btn_answers_can_pay_when_dev).insert(inl_btn_answers_not_my_size)
inl_menu_answers.insert(inl_btn_answers_delivery_for_alot_things).insert(inl_btn_how_to_use_back)