# Giftorium Studio Showcase

Django-based website for presenting experiential design case studies, capabilities, and testimonials. The project ships with a single "experiences" app, reusable base template, and starter styling so you can focus on storytelling and assets.

## Requirements

- Python 3.11+
- pip

## Getting Started

```powershell
cd "c:\Users\Amerius\Desktop\Giftorium website"
python -m venv .venv
".venv\Scripts\python" -m pip install -r requirements.txt
```

## Running the site

```powershell
".venv\Scripts\python" manage.py migrate
".venv\Scripts\python" manage.py runserver
```

Visit http://127.0.0.1:8000/ to view the showcase homepage.

## Next Steps

1. Replace placeholder project, service, and testimonial data in `experiences/views.py` with real studio content or pull from a database.
2. Update imagery, fonts, and colors inside `static/css/site.css` to match your visual identity.
3. Add additional pages (case studies, inquiry form) by creating new templates and URL routes in the `experiences` app.
