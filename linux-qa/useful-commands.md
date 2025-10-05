# Полезные Linux команды для тестировщика

## Мониторинг системы
```bash
# Просмотр запущенных процессов
ps aux | grep nginx

# Мониторинг ресурсов
htop
free -h
df -h

# Просмотр логов в реальном времени
tail -f /var/log/nginx/access.log


# Поиск ошибок в логах
grep -i "error" /var/log/syslog
grep -c "404" /var/log/nginx/access.log

# Анализ самых частых ошибок
cat /var/log/nginx/access.log | awk '{print $9}' | sort | uniq -c | sort -rn

# Просмотр логов за определенное время
sed -n '/2024-01-15 14:00/,/2024-01-15 15:00/p' /var/log/app.log


# Проверка доступности сервиса
curl -I https://api.example.com
ping google.com

# Проверка открытых портов
netstat -tulpn
ss -tulpn

# Анализ сетевых проблем
traceroute example.com
mtr example.com
