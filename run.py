import uvicorn
import sys
import os

# Добавляем путь к папке clean_architecture_practice
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("clean_architecture_practice.app.main:app", host="0.0.0.0", port=10000)
