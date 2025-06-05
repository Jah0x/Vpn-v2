# 📘 Codex Tasks: VPN v2.1 Backend & Telegram Bot Development

## ❗ Важно

> **⚠️ Codex не должен касаться настройки серверов, деплоя в Kubernetes, написания манифестов, конфигов и прочей инфраструктуры. Всё это уже реализовано вручную.**

---

## 📌 Задачи для Codex

### 🔐 1. Аутентификация и учётные записи

**📚 Библиотека авторизации:**

* Использовать `GLAuth` ([https://github.com/glauth/glauth](https://github.com/glauth/glauth)) как LDAP back-end.

**📋 Требования:**

* Пользователь может зарегистрироваться **без Telegram** и позже привязать Telegram к своему аккаунту.
* Пользователь может авторизоваться **через Telegram WebApp**, если ранее зарегистрирован (или создать аккаунт с Telegram ID + пароль).
* Реализовать эндпоинты:

  * `POST /auth/register` — регистрация с email/паролем.
  * `POST /auth/link-telegram` — привязка Telegram ID к существующему аккаунту.
  * `POST /auth/login` — логин через email+пароль.
  * `POST /auth/login/telegram` — Telegram Web Login.
  * `POST /auth/set-password` — установка пароля (при Telegram-регистрации).
  * `GET /auth/me` — текущий пользователь (JWT).

### 📨 2. Email-уведомления

**Домен:** `zerologsvpn.com`

**📋 Задачи:**

* Настроить отправку email при:

  * Успешной регистрации.
  * Блокировке аккаунта.
  * Привязке Telegram.
* Использовать SMTP (например, mailgun/sendgrid).
* Шаблоны писем должны быть легко настраиваемыми.

### 🧩 3. API для WebApp (Frontend)

**📋 Эндпоинты:**

* `GET /subscription/active` — текущая подписка (если есть).
* `GET /subscription/config/{format}` — вернуть конфиг в формате `vless://`, `vmess://`, `json`, `qr`.
* `POST /subscription/activate` — активация подписки по ключу.
* `GET /user/status` — срок действия подписки, лимиты.

### 🤖 4. Telegram Bot API (для python-telegram-bot)

**📋 Задачи:**

* FSM логика:

  1. Выбор тарифа
  2. Ввод email / логин
  3. Создание подписки (генерация UUID и ключей)
  4. Проверка оплаты (эмуляция или webhook)
  5. Отправка конфигурации
* `POST /bot/user/{telegram_id}/status` — получить статус.
* `POST /bot/user/{telegram_id}/set-password` — установить пароль.

### 🛡️ 5. Защита и безопасность

* Использовать JWT токены (short TTL + refresh).
* Хэширование паролей через bcrypt.
* Проверка CORS и CSRF.
* Ограничение доступа по ролям (`user`, `admin`).

---

## 📁 Структура репозитория (ожидаемая)

```
vpn-v2.1/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── auth/               # Работа с GLAuth, JWT
│   │   ├── models/             # Pydantic / SQLAlchemy
│   │   ├── routes/             # API endpoints
│   │   └── services/           # Бизнес-логика, email, подписки
├── bot/
│   ├── main.py
│   └── handlers/
├── requirements.txt
└── README.md
```

---

## ✅ Ожидаемый результат

* Полностью работающий backend API с авторизацией через GLAuth и Telegram.
* Уведомления на почту при действиях пользователя.
* Telegram-бот с FSM, получающий данные из API.
* Код структурирован, покрыт basic тестами, конфиги — через переменные окружения.
