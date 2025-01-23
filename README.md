# YouTube Downloader

[![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Профессиональное консольное приложение для загрузки медиаконтента с YouTube с поддержкой современных стандартов.

## Содержание
1. [Особенности](#особенности)
2. [Требования](#требования)
3. [Установка и настройка](#установка-и-настройка)
4. [Использование](#использование)
5. [Архитектура](#архитектура)
6. [Обработка ошибок](#обработка-ошибок)
7. [Лицензия](#лицензия)
8. [Благодарности](#благодарности)

## Особенности ✨

- **Мультиформатная поддержка**:
  - Скачивание видео в форматах MP4, WebM, 3GP
  - Экспорт аудио в MP3 с битрейтом до 320kbps
- **Гибкое управление качеством**:
  - Поддержка разрешений до 8K (при доступности)
  - Автовыбор оптимального качества
- **Кроссплатформенность**:
  - Полная поддержка Windows, Linux, macOS
- **Интеллектуальный интерфейс**:
  - Консольный (CLI) и интерактивный режимы
  - Реализация паттерна Command
- **Безопасность**:
  - Валидация URL через регулярные выражения
  - Обработка SSL/TLS сертификатов

## Требования 📋

| Компонент       | Минимальная версия | Рекомендуемая версия |
|-----------------|--------------------|----------------------|
| Python          | 3.7                | 3.10+                |
| yt-dlp          | 2023.07.06         | 2023.11.16           |
| FFmpeg          | 4.3                | 6.0                  |
| Память          | 512 MB             | 2 GB                 |
| Дисковое пространство | 100 MB       | 1 GB                 |

## Установка и настройка ⚙️

### 1. Клонирование репозитория
```bash
git clone https://github.com/yourusername/cpp-youtube-downloader.git
cd cpp-youtube-downloader
```

### 2. Настройка виртуального окружения
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\Activate   # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка FFmpeg
```bash
# Для Windows (используя winget):
winget install Gyan.FFmpeg

# Экспорт пути (временный):
export PATH="$PATH:/path/to/ffmpeg/bin"
```

## Использование 🖥️

### Базовый синтаксис
```bash
python -m youtube_dl.cli [URL] [ОПЦИИ]
```

### Примеры команд
```bash
# Скачать видео в максимальном качестве
python -m youtube_dl.cli "https://youtu.be/dQw4w9WgXcQ" --dir ./videos

# Скачать аудио в формате MP3
python -m youtube_dl.cli "https://youtu.be/dQw4w9WgXcQ" --type audio

# Скачать видео в 1080p
python -m youtube_dl.cli "https://youtu.be/dQw4w9WgXcQ" --quality 1080p
```

### Интерактивный режим
```bash
python -m youtube_dl.cli
```

**Компонентная модель**:
1. **CLI Parser**: Обработка аргументов командной строки
2. **Download Engine**: Ядро загрузки с использованием yt-dlp
3. **Media Processor**: Конвертация форматов через FFmpeg
4. **Error Handler**: Централизованная система обработки исключений

## Обработка ошибок 🚨

| Код ошибки | Причина                     | Решение                      |
|------------|-----------------------------|------------------------------|
| ERR-001    | Недоступность FFmpeg        | Проверить PATH, переустановить |
| ERR-002    | Геоблокировка контента      | Использовать --geo-bypass     |
| ERR-003    | Неподдерживаемый формат     | Проверить доступные форматы   |
| ERR-004    | Ошибка сети                 | Проверить подключение         |
