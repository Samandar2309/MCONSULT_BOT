from aiogram.fsm.state import StatesGroup, State

class ContactState(StatesGroup):
    name = State()
    phone = State()
    message = State()
    confirm = State()  # <--- Shu qator borligiga ishonch hosil qiling