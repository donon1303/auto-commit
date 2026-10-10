from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# Текущая дата в часовом поясе UTC+5
today = datetime.now(ZoneInfo("Asia/Almaty")).date()

# Папка для ежедневных файлов
folder = Path("daily")
folder.mkdir(exist_ok=True)

# Новый файл для каждого дня
file_path = folder / f"{today}.md"

# Содержимое файла
content = f"""# Daily update — {today}

Автоматически созданный ежедневный файл.

Дата: {today}
Статус: создано автоматически.
"""

# Не перезаписываем файл, если он уже существует
if not file_path.exists():
    file_path.write_text(content, encoding="utf-8")
    print(f"Создан файл: {file_path}")
else:
    print(f"Файл уже существует: {file_path}")
