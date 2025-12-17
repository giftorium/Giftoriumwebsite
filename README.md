# Giftorium Showcase

Django-based website for presenting experiential design case studies, capabilities, and testimonials for Giftorium (gogiftorium.com). The project ships with a single "experiences" app, reusable base template, and starter styling so you can focus on storytelling and assets.

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

1. Add real projects, services, testimonials, and portfolio entries through the Django admin.
2. Upload your logo + hero copy inside **Studio settings**, then add portraits in **Team members** so the `/team/` page stays current.
3. Tweak imagery, fonts, and colors inside `static/css/site.css` to match your visual identity.

## Managing the portfolio

1. Run migrations and create an admin user:
	```powershell
	".venv\Scripts\python" manage.py migrate
	".venv\Scripts\python" manage.py createsuperuser
	```
2. Visit `/admin/` to add Portfolio Items, Projects, Services, and Testimonials. Upload hero and gallery images per entry.
3. Uploaded media is stored in the `media/` directory locally. In production, set an environment variable `MEDIA_ROOT` that points to your Render disk mount path (e.g., `/var/media`) so uploads persist across deploys.

## Collaboration inquiries

1. The contact form on the homepage stores submissions in the **Inquiries** admin section and emails your team.
2. Configure outbound email via environment variables:
	- `DEFAULT_FROM_EMAIL` – address used for the outgoing message header (defaults to `hello@gogiftorium.com`).
	- `INQUIRY_RECIPIENTS` – comma-separated inboxes that receive new requests (defaults to `hello@gogiftorium.com, amir@gogiftorium.com`).
3. Ensure Render has a working email backend (e.g., SMTP credentials) if you want live notifications; stored entries remain accessible in the admin regardless.
