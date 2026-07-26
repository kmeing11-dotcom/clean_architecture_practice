import uvicorn
import sys
import os

# Добавляем корневую папку в путь, чтобы Python видел модуль app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)