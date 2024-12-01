#!/bin/bash

# Шаг 1: Запуск процесса ETL
echo "Starting ETL process..."
python3 run_etl.py

# Шаг 2: Запуск экспериментов
echo "Running experiments..."
python3 run_experiments.py
