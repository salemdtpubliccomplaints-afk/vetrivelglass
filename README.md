# Vetrivel Glass – Premium Graphical Flask Website

Production-ready Flask company website for:

**www.vetrivelglass.com**

## Contact information included

- Phone / WhatsApp: +91 73588 17353
- Email: contact@vetrivelglass.com
- Head office: Main Rd, near Jawager Mill, Subramania Nagar, Suramangalam, Salem, Tamil Nadu 636015

## Premium visual upgrades

- Glass-inspired hero overlays and graphical highlights
- Premium navy-and-gold visual system
- Custom CSS line icons
- Animated reveal effects
- Enhanced service cards with imagery
- Graphical windshield inspection section
- Premium process timeline and customer-experience section
- Richer About, Services and Contact pages
- Salem location illustration
- Premium footer and call-to-action areas
- Responsive desktop, tablet and mobile layouts

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Render deployment

Build command:

```text
pip install -r requirements.txt
```

Start command:

```text
gunicorn app:app
```

Add `www.vetrivelglass.com` and `vetrivelglass.com` as custom domains in your hosting service and configure the DNS records supplied by the host.

## Production database note

The included enquiry database uses SQLite. For permanent cloud storage, connect PostgreSQL or Supabase before accepting live customer enquiries on hosting platforms with temporary filesystems.
