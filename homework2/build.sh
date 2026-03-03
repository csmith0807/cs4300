#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.filter(username='csmith11').exists() or User.objects.create_superuser('csmith11', 'admin@example.com', 'admin123')" | python manage.py shell