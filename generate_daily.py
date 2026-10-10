from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from random import randint

now = datetime.now(ZoneInfo("Asia/Almaty"))
count = randint(1, 15)

folder = Path("daily") / now.strftime("%Y-%m-%d") / now.strftime("%H%M%S")
folder.mkdir(parents=True, exist_ok=True)

for i in range(1, count + 1):
    file_path = folder / f"update_{i:02}.md"

    content = f"""# Daily update {i}

Дата: {now.strftime("%Y-%m-%d")}
Номер изменения: {i}
Всего изменений за запуск: {count}
Время создания: {now.strftime("%H:%M:%S")}

Автоматически созданный файл.
"""

    file_path.write_text(content, encoding="utf-8")

print(f"Создано файлов и запланировано коммитов: {count}")
