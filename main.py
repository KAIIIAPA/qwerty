import requests
import logging
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание файловых handlers для каждого типа логов
success_handler = logging.FileHandler('success_responses.log', 'w')
success_handler.setLevel(logging.INFO)
success_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

bad_handler = logging.FileHandler('bad_responses.log', 'w')
bad_handler.setLevel(logging.WARNING)
bad_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

blocked_handler = logging.FileHandler('blocked_responses.log', 'w')
blocked_handler.setLevel(logging.ERROR)
blocked_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

# Добавление handlers к логгеру
logger.addHandler(success_handler)
logger.addHandler(bad_handler)
logger.addHandler(blocked_handler)

# Список сайтов для проверки
sites = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com'
]

for site in sites:
    try:
        # Отправка запроса
        response = requests.get(site)

        # Проверка статуса ответа
        if response.status_code == 200:
            logger.info(f"{site}, response - {response.status_code}")
        else:
            logger.warning(f"{site}, response - {response.status_code}")
    except (ConnectionError, ConnectTimeout, ReadTimeout) as e:
        logger.error(f"{site}, {type(e).__name__}")