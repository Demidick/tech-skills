-- Сценарии для тестирования данных в приложении

-- Проверка корректности цен (не должны быть отрицательными)
SELECT product_id, price 
FROM products 
WHERE price < 0;

-- Поиск битых ссылок на изображения
SELECT product_id, image_url 
FROM products 
WHERE image_url IS NULL OR image_url = '';

-- Валидация email адресов
SELECT user_id, email 
FROM users 
WHERE email NOT LIKE '%@%.%';
