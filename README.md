# 🖋️ The Polished Ink
**A High-Fidelity, File-Based CMS built with FastAPI & Tailwind CSS.**

A project from [roadmap.sh](https://roadmap.sh/projects/personal-blog)

The Polished Ink is a minimalist personal blog engine designed for developers who value monochromatic aesthetics and architectural simplicity. It bypasses the complexity of traditional databases by using a structured JSON file-system storage, making it incredibly lightweight, fast, and easy to audit.

## ✨ Key Features
* **Full CRUD Logic**: Create, Read, Update, and Delete articles via a dedicated Admin Dashboard.
* **Ink-Ready UI**: A custom "Bento-style" interface inspired by minimalist print design, powered by Tailwind CSS.
* **Secure Admin Wing**: Protected `/admin` routes using HTTP Basic Authentication and `APIRouter` modularization.
* **Persistent Storage**: Articles are stored as human-readable JSON files, ensuring your data is portable and easy to back up.
* **Environment Safety**: Sensitive admin credentials managed via `.env` files for public repository safety.

## 🛠️ Tech Stack
* **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
* **Frontend**: [Jinja2 Templates](https://jinja.palletsprojects.com/) & [Tailwind CSS](https://tailwindcss.com/)
* **Storage**: Local File System (JSON)
* **Dependency Management**: [uv](https://github.com/astral-sh/uv)

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10+ and `uv` installed.

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/tegarsosi/personal-blog.git](https://github.com/tegarsosi/personal-blog.git)
cd personal-blog

# Install dependencies
uv sync