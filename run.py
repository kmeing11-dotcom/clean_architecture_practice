import uvicorn
import sys
import os

# Добавляем путь к папке clean_architecture_practice в sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'clean_architecture_practice'))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=10000)
