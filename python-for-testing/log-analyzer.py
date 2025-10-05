#!/usr/bin/env python3
"""
Скрипт для анализа логов приложения
Находит ошибки и формирует отчет
"""

import re
from collections import Counter
from datetime import datetime

def analyze_logs(log_file_path):
    """Анализирует логи и находит частые ошибки"""
    
    error_patterns = {
        'ERROR': r'ERROR.*',
        'HTTP 5xx': r'HTTP 5\d{2}',
        'Timeout': r'TIMEOUT|timeout',
        'NullPointer': r'NullPointerException',
    }
    
    results = {}
    
    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            logs = file.readlines()
            
        for error_type, pattern in error_patterns.items():
            count = len([line for line in logs if re.search(pattern, line, re.IGNORECASE)])
            results[error_type] = count
            
        # Топ частых ошибок
        error_lines = [line for line in logs if 'ERROR' in line]
        top_errors = Counter(error_lines).most_common(5)
        
        print(f"=== Анализ логов {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
        print(f"Проанализировано строк: {len(logs)}")
        print("\nСтатистика ошибок:")
        for error_type, count in results.items():
            print(f"  {error_type}: {count}")
            
        print("\nТоп-5 частых ошибок:")
        for error, count in top_errors:
            print(f"  [{count}] {error.strip()}")
            
    except FileNotFoundError:
        print(f"Файл {log_file_path} не найден")
    except Exception as e:
        print(f"Ошибка при анализе: {e}")

if __name__ == "__main__":
    analyze_logs('sample.log')
