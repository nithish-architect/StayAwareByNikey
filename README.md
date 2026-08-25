StayAwareByNikey

Cut through modern myths. Know what humans actually need to survive and thrive.

A full-stack web application built on Flask and PostgreSQL, containerized with Docker, covering the 5 human essentials — Food, Body, Environment, Clothing, and Shelter.

What This App Does

Users log in and read evidence-based articles that debunk modern myths about human essentials. Each article presents the myth, the truth, and the full explanation backed by research.

5 Categories
Category	Focus
🍚 Food	Traditional Indian nutrition vs modern processed food myths
💪 Body	Foundational strength, joint health, movement — not bodybuilding
🌿 Environment	Air, water, sunlight — what your body was designed for
👕 Clothing	Natural vs synthetic fabrics and their effect on the body
🏠 Shelter	Ventilation, light, sleep environment — what makes a home healthy
Tech Stack
Layer	Technology
Backend	Python, Flask, SQLAlchemy
Database	PostgreSQL
Auth	Flask-Login, Flask-Bcrypt
Frontend	HTML, CSS (custom dark theme)
Container	Docker, Docker Compose
Project Structure
StayAwareByNikey/
├── app/
│   ├── __init__.py        # App factory
│   ├── models.py          # User, Category, Article models
│   ├── routes.py          # All routes
│   ├── static/css/        # Stylesheet
│   └── templates/         # HTML templates
├── config.py              # Configuration
├── run.py                 # Entry point with DB wait logic
├── seed.py                # Database seeder
├── Dockerfile             # Container definition
├── docker-compose.yml     # Flask + PostgreSQL orchestration
└── requirements.txt       # Python dependencies
How to Run
bash
# Clone the repo
git clone https://github.com/nithish-architect/StayAwareByNikey.git
cd StayAwareByNikey

# Start with Docker
docker compose up --build

# Seed the database (in a second terminal)
docker compose exec web python3 seed.py

# Open browser
# http://localhost:5000
Login Credentials
Email: nithish@stayaware.com
Password: stayaware123
Database Models
User — id, username, email, password_hash, created_at
Category — id, name, icon, description
Article — id, title, myth, truth, content, sources, category_id
Key Features
Login-protected content — no public registration
Myth vs Truth layout on every article
Evidence-based content with cited sources
PostgreSQL with persistent Docker volume
Clean dark UI optimized for reading
Why This Project

India has the highest Type 2 diabetes rate in the world. Most Indians are Vitamin D deficient despite living in sunshine. Traditional clothing wisdom is being replaced by synthetic fabrics. Modern apartments disrupt sleep. This app brings together evidence-based information about what humans actually need — cutting through marketing myths and social media misinformation.

Author

Nithish Raj

GitHub: nithish-architect
Email: nithishraj2106@gmail.com
