import subprocess
import datetime
import os

# Конфигурация
DB_NAME = "fast_api"
DB_USER = "admin"
DB_HOST = "localhost"
BACKUP_DIR = "./backups"

# Убедитесь, что папка для бэкапов существует
os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(BACKUP_DIR, f"backup_{current_time}.sql")

    try:
        # Выполняем команду pg_dump
        subprocess.run(
            [
                "pg_dump",
                "-U", DB_USER,
                "-h", DB_HOST,
                DB_NAME,
                "-f", backup_file
            ],
            check=True
        )
        print(f"Бэкап успешно создан: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при создании бэкапа: {e}")
    except Exception as ex:
        print(f"Непредвиденная ошибка: {ex}")

if __name__ == "__main__":
    create_backup()
