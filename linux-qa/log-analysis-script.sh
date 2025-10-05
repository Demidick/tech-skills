#!/bin/bash
# Скрипт для быстрого анализа логов тестирования

LOG_FILE="${1:-/var/log/application.log}"
REPORT_FILE="log_report_$(date +%Y%m%d_%H%M%S).txt"

echo "=== Анализ логов: $LOG_FILE ===" > "$REPORT_FILE"
echo "Время анализа: $(date)" >> "$REPORT_FILE"
echo "=================================" >> "$REPORT_FILE"

# Статистика по уровням логирования
echo "" >> "$REPORT_FILE"
echo "СТАТИСТИКА УРОВНЕЙ ЛОГИРОВАНИЯ:" >> "$REPORT_FILE"
grep -c "ERROR" "$LOG_FILE" | xargs echo "ERROR: " >> "$REPORT_FILE"
grep -c "WARN" "$LOG_FILE" | xargs echo "WARN:  " >> "$REPORT_FILE"
grep -c "INFO" "$LOG_FILE" | xargs echo "INFO:  " >> "$REPORT_FILE"

# Топ ошибок
echo "" >> "$REPORT_FILE"
echo "ТОП-10 САМЫХ ЧАСТЫХ ОШИБОК:" >> "$REPORT_FILE"
grep "ERROR" "$LOG_FILE" | cut -d' ' -f5- | sort | uniq -c | sort -rn | head -10 >> "$REPORT_FILE"

echo "Отчет сохранен в: $REPORT_FILE"
