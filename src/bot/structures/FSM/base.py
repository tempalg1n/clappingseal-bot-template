from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    greeting = State()
    