#!/usr/bin/env python3
"""
Утилита для быстрого тестирования API
"""

import requests
import json

def test_api_endpoint(url, method='GET', headers=None, data=None):
    """Тестирует API endpoint и возвращает результат"""
    
    default_headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'QA-Test-Script/1.0'
    }
    
    if headers:
        default_headers.update(headers)
        
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=default_headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=default_headers, json=data)
        else:
            return {"error": f"Unsupported method: {method}"}
            
        result = {
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "headers": dict(response.headers),
            "data": response.json() if response.content else None
        }
        
        return result
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}

# Пример использования
if __name__ == "__main__":
    # Тестируем публичное API
    result = test_api_endpoint('https://api.github.com/users/octocat')
    print(json.dumps(result, indent=2, ensure_ascii=False))
