# SERVER_REBUILD.md

## Project

**Project Name:** EngCalc

**Repository:**
https://github.com/sanchitsharma84/engcalc

**Domain:**
engcalc.in

**Server OS:**
Ubuntu 24.04 LTS

**Deployment Date:**
June 2026

---

# Important Notes

## Python Version

Ubuntu 24.04 ships with Python 3.12.

The project uses:

* Django 3.1.7
* django-crispy-forms 1.11.1

These do not work correctly with Python 3.12 because `distutils` has been removed.

Install and use Python 3.11.

Verify:

```bash
python3.11 --version
```

Expected:

```text
Python 3.11.x
```

---

## Database

Database file: db.sqlite3

Contains:

Django authentication tables
User accounts and permissions
Permissions
Sessions
SmallServoMotor master table (11 servo motor records)

Does NOT contain:

Calculation history
User projects
Engineering reports
Uploaded files

The application is largely stateless and most calculations are performed directly in Python without database storage.

---

# EC2 Instance Creation

Create a new AWS account if free tier is required.

Create EC2 instance:

* Ubuntu 24.04 LTS
* t2.micro or equivalent free tier
* Allow HTTP (80)
* Allow HTTPS (443)
* Allow SSH (22)

---

# Initial Package Installation

```bash
sudo apt update

sudo apt install -y \
git \
python3-pip \
python3-venv \
nginx
```

---

# Install Python 3.11

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

sudo apt install -y \
python3.11 \
python3.11-venv \
python3.11-dev
```

Verify:

```bash
python3.11 --version
```

---

# Clone Project

```bash
cd ~

git clone https://github.com/sanchitsharma84/engcalc.git

cd engcalc
```

Repository is public.

---

# Create Virtual Environment

```bash
python3.11 -m venv env

source env/bin/activate
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.11.x
```

---

# Install Dependencies

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

Important packages:

* Django
* mechpress
* presslink
* numpy
* matplotlib
* xlsxwriter

Verify:

```bash
pip freeze
```

---

# Django Check

```bash
python manage.py check
```

Expected:

```text
System check identified no issues
```

---

# Migrations

```bash
python manage.py migrate
```

---

# Test Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Open:

```text
http://EC2_PUBLIC_IP:8000
```

---

# settings.py

Edit:

```text
cal_proj/settings.py
```

Production settings:

```python
DEBUG = False

ALLOWED_HOSTS = [
    'engcalc.in',
    'www.engcalc.in',
    'localhost',
    '127.0.0.1',
]
```

---

# Gunicorn Installation

```bash
pip install gunicorn
```

Test:

```bash
gunicorn --bind 0.0.0.0:8000 cal_proj.wsgi
```

---

# Gunicorn Service

File:

```text
/etc/systemd/system/gunicorn.service
```

Current working version backed up separately.

---

# Gunicorn Socket

File:

```text
/etc/systemd/system/gunicorn.socket
```

Current working version backed up separately.

---

# Enable Gunicorn

```bash
sudo systemctl daemon-reload

sudo systemctl start gunicorn.socket

sudo systemctl enable gunicorn.socket
```

Verify:

```bash
sudo systemctl status gunicorn.socket

sudo systemctl status gunicorn
```

---

# Nginx Configuration

File:

```text
/etc/nginx/sites-available/engcalc
```

Current working version backed up separately.

Enable:

```bash
sudo ln -s \
/etc/nginx/sites-available/engcalc \
/etc/nginx/sites-enabled
```

Disable default site:

```bash
sudo rm /etc/nginx/sites-enabled/default
```

Test:

```bash
sudo nginx -t
```

Reload:

```bash
sudo systemctl reload nginx
```

---

# Domain Configuration

Registrar:

Namecheap

Domain:

```text
engcalc.in
```

DNS records:

```text
A Record
Host: @
Value: EC2_PUBLIC_IP

A Record
Host: www
Value: EC2_PUBLIC_IP
```

Verify:

```bash
nslookup engcalc.in
```

---

# SSL Certificate

Install:

```bash
sudo apt install -y certbot python3-certbot-nginx
```

Generate certificate:

```bash
sudo certbot --nginx \
-d engcalc.in \
-d www.engcalc.in
```

Choose:

```text
Redirect HTTP to HTTPS
```

Verify:

```text
https://engcalc.in
```

---

# SSL Renewal Test

```bash
sudo certbot renew --dry-run
```

Expected:

```text
Congratulations, all simulated renewals succeeded
```

---

# SSH Access

Public key from Windows PC:

```text
C:\Users\Sanchit_1\.ssh\id_ed25519.pub
```

Add to:

```text
~/.ssh/authorized_keys
```

Connect:

```bash
ssh ubuntu@engcalc.in
```

---

# Final Verification

Verify:

* Homepage loads
* Login works
* Calculators work
* Graph generation works
* Excel export works
* HTTPS works

---

# Backup Files

Keep copies of:

```text
engcalc_nginx.conf
gunicorn.service
gunicorn.socket
settings.py.backup
```

These files are sufficient to rebuild deployment configuration.
