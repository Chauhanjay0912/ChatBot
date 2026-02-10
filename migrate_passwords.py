# Run this script to hash existing plain text passwords
# python manage.py shell < migrate_passwords.py

from store.models import user
from django.contrib.auth.hashers import make_password

print("Starting password migration...")

users = user.objects.all()
count = 0

for u in users:
    # Check if password is already hashed (starts with algorithm identifier)
    if not u.password.startswith('pbkdf2_sha256$'):
        u.password = make_password(u.password)
        u.save()
        count += 1
        print(f"Updated password for: {u.email}")

print(f"\nMigration complete! Updated {count} passwords.")
