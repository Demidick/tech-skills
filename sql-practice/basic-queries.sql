-- Примеры запросов для тестирования данных

-- Проверка уникальности пользователей
SELECT email, COUNT(*) as count 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Поиск неактивированных аккаунтов старше 7 дней
SELECT user_id, created_at 
FROM users 
WHERE activated = false 
AND created_at < NOW() - INTERVAL '7 days';

-- Проверка целостности заказов (есть ли заказы без пользователей)
SELECT o.order_id, o.user_id 
FROM orders o 
LEFT JOIN users u ON o.user_id = u.user_id 
WHERE u.user_id IS NULL;
