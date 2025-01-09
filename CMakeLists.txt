cmake_minimum_required(VERSION 3.15)
project(Course-Work)

set(CMAKE_CXX_STANDARD 17)

# Підключення pybind11
add_subdirectory(pybind11)

# Джерела для модуля Pybind11
set(SOURCES
    src/python/game_module.cpp
    src/game/game.cpp
)

# Додайте директорії заголовкових файлів
include_directories(src/game)

# Створення модуля Pybind11
pybind11_add_module(game_module ${SOURCES})

# Додавання заголовків Pybind11
target_include_directories(game_module PRIVATE ${CMAKE_SOURCE_DIR}/pybind11/include)
