import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from pycoingecko import CoinGeckoAPI

from py_currency_converter import convert

#Токен
API_TOKEN = 'Токен'

#Логируем бота
logging.basicConfig(level=logging.INFO)

#Определяем бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Определяем биткоин
cg = CoinGeckoAPI()
price = cg.get_price(ids = ['bitcoin','ethereum','litecoin', 'cardano', 'dogecoin', 'solana', 'polkadot', 'iotex'], vs_currencies = ['usd','eur','rub','uah'])

#Клавиатура нижняя
btn1 = KeyboardButton("Курс криптовалют")
btn2 = KeyboardButton("Денежный курс")

markup1 = ReplyKeyboardMarkup().add(btn1).add(btn2)

#Клавиатура текста(Крипта)
inline_btn_1 = InlineKeyboardButton(text='usd', callback_data='cripta_1')
inline_btn_2 = InlineKeyboardButton(text='eur', callback_data='cripta_2')
inline_btn_3 = InlineKeyboardButton(text='rub', callback_data='cripta_3')
inline_btn_4 = InlineKeyboardButton(text='uah', callback_data='cripta_4')

inline_markup_1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3).add(inline_btn_4)

#Клавиатура текста(Деньги)
inline_btn_5 = InlineKeyboardButton(text='USD', callback_data='money1')
inline_btn_6 = InlineKeyboardButton(text='EUR', callback_data='money2')
inline_btn_7 = InlineKeyboardButton(text='RUB', callback_data='money3')
inline_btn_8 = InlineKeyboardButton(text='UAH', callback_data='money4')
inline_markup_2 = InlineKeyboardMarkup().add(inline_btn_5).add(inline_btn_6).add(inline_btn_7).add(inline_btn_8)

#Стартовое приветствие бота
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет. Я бот для отслеживания криптовалюты и курса валют. \n Если хочешь узнать обо мне подробнее,тогда напиши слово помощь.", reply_markup = markup1)

#Криптовалюты
@dp.message_handler(commands=['bit'], commands_prefix='!')
@dp.message_handler(lambda message: message.text == "Курс криптовалют")
async def send_welcome(message: types.Message):
	await message.reply("Выберите валюту",reply_markup = inline_markup_1)

#Конвертация крипты в деньги
@dp.callback_query_handler(text="cripta_1")
async def process_callback_moneys(call: types.CallbackQuery):
		await call.message.answer(f"1 BTC = {price['bitcoin']['usd']:.2f} $" + f"\n1 Ethereum = {price['ethereum']['usd']:.2f} $" + f"\n1 Litecoin = {price['litecoin']['usd']:.2f} $" + f"\n1 Cardano = {price['cardano']['usd']:.2f} $" + f"\n1 Dogecoin = {price['dogecoin']['usd']:.2f} $" + f"\n1 Solana = {price['solana']['usd']:.2f} $" + f"\n1 Polkadot = {price['polkadot']['usd']:.2f} $" + f"\n1 Iotex = {price['iotex']['usd']:.2f} $")
@dp.callback_query_handler(text="cripta_2")
async def process_callback_moneys(call: types.CallbackQuery):
		await call.message.answer(f"1 BTC = {price['bitcoin']['eur']:.2f} EUR" + f"\n1 Ethereum = {price['ethereum']['eur']:.2f} EUR" + f"\n1 Litecoin = {price['litecoin']['eur']:.2f} EUR" + f"\n1 Cardano = {price['cardano']['eur']:.2f} EUR" + f"\n1 Dogecoin = {price['dogecoin']['eur']:.2f} EUR" + f"\n1 Solana = {price['solana']['eur']:.2f} EUR" + f"\n1 Polkadot = {price['polkadot']['eur']:.2f} EUR" + f"\n1 Iotex = {price['iotex']['eur']:.2f} EUR")
@dp.callback_query_handler(text="cripta_3")
async def process_callback_moneys(call: types.CallbackQuery):
		await call.message.answer(f"1 BTC = {price['bitcoin']['rub']:.2f} RUB" + f"\n1 Ethereum = {price['ethereum']['rub']:.2f} RUB" + f"\n1 Litecoin = {price['litecoin']['rub']:.2f} RUB" + f"\n1 Cardano = {price['cardano']['rub']:.2f} RUB" + f"\n1 Dogecoin = {price['dogecoin']['rub']:.2f} RUB" + f"\n1 Solana = {price['solana']['rub']:.2f} RUB" + f"\n1 Polkadot = {price['polkadot']['rub']:.2f} RUB" + f"\n1 Iotex = {price['iotex']['rub']:.2f} RUB")
@dp.callback_query_handler(text="cripta_4")
async def process_callback_moneys(call: types.CallbackQuery):
		await call.message.answer(f"1 BTC = {price['bitcoin']['uah']:.2f} UAH" + f"\n1 Ethereum = {price['ethereum']['uah']:.2f} UAH" + f"\n1 Litecoin = {price['litecoin']['uah']:.2f} UAH" + f"\n1 Cardano = {price['cardano']['uah']:.2f} UAH" + f"\n1 Dogecoin = {price['dogecoin']['uah']:.2f} UAH" + f"\n1 Solana = {price['solana']['uah']:.2f} UAH" + f"\n1 Polkadot = {price['polkadot']['uah']:.2f} UAH" + f"\n1 Iotex = {price['iotex']['uah']:.2f} UAH")

#Валюты
@dp.message_handler(commands=['conv'], commands_prefix='!')
@dp.message_handler(lambda message: message.text == "Денежный курс")
async def send_welcome(message: types.Message):
	cource = convert(base=['RUB','EUR','UAH','USD'],amount=1, to=['RUB','EUR','UAH','USD'])
	await message.reply("Выберите валюту",reply_markup = inline_markup_2)

#Денежный перевод
@dp.callback_query_handler(text="money1")
async def process_callback_moneys(call: types.CallbackQuery):
		cource = convert(base='USD',amount=1, to=['RUB','EUR','UAH','USD'])
		await call.message.answer(f"1 USD = {cource['RUB']} RUB" + f"\n 1 USD = {cource['EUR']} EUR" + f"\n 1 USD = {cource['UAH']} UAH")
@dp.callback_query_handler(text="money2")
async def process_callback_moneys(call: types.CallbackQuery):
		cource = convert(base='EUR',amount=1, to=['RUB','EUR','UAH','USD'])
		await call.message.answer(f"1 EUR = {cource['RUB']} RUB" + f"\n 1 EUR = {cource['USD']} USD" + f"\n 1 EUR = {cource['UAH']} UAH")
@dp.callback_query_handler(text="money3")
async def process_callback_moneys(call: types.CallbackQuery):
		cource = convert(base='RUB',amount=1, to=['RUB','EUR','UAH','USD'])
		await call.message.answer(f"1 RUB = {cource['USD']} USD" + f"\n 1 RUB = {cource['EUR']} EUR" + f"\n 1 RUB = {cource['UAH']} UAH")
@dp.callback_query_handler(text="money4")
async def process_callback_moneys(call: types.CallbackQuery):
		cource = convert(base='UAH',amount=1, to=['RUB','EUR','UAH','USD'])
		await call.message.answer(f"1 UAH = {cource['RUB']} RUB" + f"\n 1 UAH = {cource['EUR']} EUR" + f"\n 1 UAH = {cource['USD']} USD")

#Помощь
@dp.message_handler()
async def help(message: types.Message):
	if 'помощь' in message.text.lower():
		await message.answer("---Помощь--- \n \nЕсли тебе нужно узнать курс криптовалюты,тогда нажми на \"Курс криптовалют\" или напиши команду !bit . \n А если тебе нужно узнать валютный курс,тогда нажми на \"Денежный курс\" или напиши команду !conv \n \n Отслеживается всего 4 валюты: Доллар, Евро, Гривны, Рубли. \n \n Отслеживается всего 8 видов криптовалют : Bitcoin, Ethereum, Litecoin, Cardano, Dogecoin, Solana, Polkadot, Iotex.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)