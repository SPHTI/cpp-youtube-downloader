# YouTube Video Downloader (C++ CLI)

![License: MIT](https://img.shields.io/badge/License-PWL-blue.svg)

Консольная утилита для скачивания видео с YouTube. Поддерживает выбор качества и формата.

## 📦 Установка

### Зависимости
- **libcurl**: `sudo apt-get install libcurl4-openssl-dev` (Linux) / [Windows](https://curl.se/windows/)
- **FFmpeg** (для объединения потоков): `sudo apt-get install ffmpeg`

### Сборка
```bash
git clone https://github.com/yourusername/yt-dl-cpp.git
cd yt-dl-cpp
mkdir build && cd build
cmake .. && make
```

## 🚀 Использование
```bash
./yt-dl-cpp [URL] [OPTIONS]
```

**Опции**:  
- `-q, --quality [720p|480p|...]`: Выбор качества видео.  
- `-a, --audio-only`: Скачать только аудио (MP3).  
- `-o, --output [filename]`: Имя выходного файла.  

**Пример**:  
```bash
./yt-dl-cpp "https://youtu.be/example" -q 1080p -o video.mp4
```

## 📂 Структура проекта
```
/../
├── src/             # Исходный код
│   ├── main.cpp
│   └── downloader.cpp
├── include/         # Заголовочные файлы
├── CMakeLists.txt
└── README.md
```

## 🔧 Технологии
- C++17
- libcurl (HTTP-запросы)
- nlohmann/json (парсинг данных YouTube)
- FFmpeg (обработка медиа)
