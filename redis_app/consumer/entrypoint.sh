#!/bin/sh

echo "Waiting for Redis..."

# Проверяем доступность порта 6379 (стандартный порт для Redis)
while ! nc -z $REDIS_HOST $REDIS_PORT; do
    echo "waiting for redis..."
    sleep 0.1
done

echo "Redis started"

exec "$@"
 