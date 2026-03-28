import os
from datetime import datetime

BASE_DIR = "."

def count_py_files(folder):
    total = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                total += 1
    return total

topics_data = {}
total_problems = 0

# Get only main topic folders
for item in os.listdir(BASE_DIR):
    if os.path.isdir(item) and item not in [".git", ".github", "__pycache__"]:
        count = count_py_files(item)
        if count > 0:
            topics_data[item] = count
            total_problems += count

# Progress bar generator
def progress_bar(count):
    total_blocks = 10
    filled = min(count, total_blocks)
    return "█" * filled + "░" * (total_blocks - filled)

# Generate README
today = datetime.now().strftime("%d %B %Y")

readme = f"""# 🚀 DSA Progress Tracker  

Hi, I'm Doyel 👋  

---

## 📊 Progress Dashboard  

- ✅ Total Problems Solved: **{total_problems}**  
- 📂 Topics Covered: **{len(topics_data)}**  
- 📅 Last Updated: **{today}**  

---

## 🧠 Topic-wise Progress  

| Topic | Problems | Progress |
|------|--------|----------|
"""

for topic, count in sorted(topics_data.items()):
    bar = progress_bar(count)
    readme += f"| {topic} | {count} | {bar} |\n"

readme += """

---

## ⚡ Repository Structure  

DSA/
├── Topic/
│ ├── Problem/
│ │ └── solution.py


---

## 🎯 Goals  

- [ ] 100+ Problems  
- [ ] Master DSA Patterns  
- [ ] Crack Internship 💼  

---

## 🛠 Tech Stack  

- Python 🐍  

---

## ⚠️ Note  

This repository is for learning purposes.  
Please do not copy solutions directly.

---

⭐ Consistency is the key to mastery.
"""

with open("README.md", "w") as f:
    f.write(readme)
