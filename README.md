# USA Restaurants Bot | Бот-каталог ресторанов США

**EN:** Telegram bot for browsing restaurants by US state, searching listings and filtering delivery options. Includes an administrator interface to add, edit and remove restaurants.

**RU:** Telegram-бот для просмотра ресторанов по штатам США, поиска и фильтрации доставки. Администратор может добавлять, редактировать и удалять рестораны.

## Features / Возможности

- Browse by state / Просмотр по штатам
- Restaurant details and maps / Карточки ресторанов и карты
- Delivery filter and search / Фильтр доставки и поиск
- Admin CRUD with FSM / Управление каталогом через FSM
- JSON persistence with atomic writes / Сохранение JSON с атомарной записью
- Admin-only callbacks and messages / Проверка прав для административных действий

## Setup / Установка

Requires Python 3.12+ / Требуется Python 3.12+.

```bash
git clone https://github.com/parviz-rahmonov/Usa_restaurants_Bot.git
cd Usa_restaurants_Bot
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `BOT_TOKEN` and comma-separated `ADMIN_IDS`. Never commit `.env`.

Скопируйте `.env.example` в `.env` и заполните `BOT_TOKEN` и `ADMIN_IDS` (ID через запятую). Не публикуйте `.env`.

```bash
python bot.py
```

## Data and limitations / Данные и ограничения

The initial catalog is bundled in `data/restaurants.py`; admin changes are saved to `data/db.json` (excluded from Git). **Back up this file**. FSM uses in-memory storage, so unfinished admin forms are lost on restart. This is a portfolio/demo project, not a production-grade multi-instance database service. Restaurant details are example data and may be outdated; verify before relying on them.

Начальный каталог находится в `data/restaurants.py`; изменения сохраняются в `data/db.json` (исключён из Git). **Создавайте резервные копии**. FSM хранится в памяти, поэтому незавершённые формы теряются при перезапуске. Это демонстрационный проект, не готовая многосерверная система. Сведения о ресторанах могут устареть.

## Security / Безопасность

Administrative message and callback handlers require an allowlisted Telegram user ID. Do not publish tokens or real customer data.

Административные обработчики сообщений и callback защищены списком разрешённых Telegram ID. Не публикуйте токены и персональные данные клиентов.

## Tests / Тесты

```bash
python -m unittest discover -s tests -v
```

Tests cover JSON persistence and source-level checks. Telegram end-to-end testing requires a configured bot and has not been performed here.

Тесты проверяют сохранение JSON и базовые свойства исходников. Полное тестирование через Telegram здесь не проводилось.
