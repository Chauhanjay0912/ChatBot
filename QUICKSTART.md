# Quick Start Guide

## For New Developers

### 1. Clone & Setup (5 minutes)
```bash
# Clone repository
git clone <repository-url>
cd EC-Chatbot

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment (2 minutes)
```bash
# Copy environment template
copy .env.example .env

# Edit .env with your credentials
# Minimum required:
# - SECRET_KEY (generate new one)
# - EMAIL_HOST_USER (your Gmail)
# - EMAIL_HOST_PASSWORD (Gmail app password)
# - RAZORPAY_KEY_ID (test key)
# - RAZORPAY_KEY_SECRET (test secret)
```

### 3. Database Setup (2 minutes)
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
```

### 4. Run Server (1 minute)
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## For Existing Database

If you have existing database with plain text passwords:

```bash
# Hash existing passwords
python manage.py shell < migrate_passwords.py
```

## Quick Test

1. Register new user: http://127.0.0.1:8000/register/
2. Login: http://127.0.0.1:8000/login/
3. Browse products: http://127.0.0.1:8000/shop/
4. Admin panel: http://127.0.0.1:8000/admin/

## Common Issues

### Issue: Import Error for dotenv
```bash
pip install python-dotenv
```

### Issue: Email not sending
- Enable "Less secure app access" in Gmail (not recommended)
- OR use Gmail App Password (recommended)
- OR use different email provider

### Issue: Razorpay errors
- Check API keys in .env
- Ensure test mode keys start with "rzp_test_"
- Verify internet connection

### Issue: Old passwords not working
- Run migrate_passwords.py script
- OR have users reset password
- OR create new test accounts

## Project Structure

```
EC-Chatbot/
├── Bot/                    # Django project settings
│   ├── settings.py        # Main configuration
│   └── urls.py            # URL routing
├── store/                 # Main application
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── utils.py           # Helper functions
│   ├── templates/         # HTML templates
│   └── static/            # CSS, JS, images
├── photo/                 # Uploaded images
├── .env                   # Environment variables (create this)
├── .env.example           # Template
├── requirements.txt       # Dependencies
├── manage.py              # Django CLI
└── db.sqlite3            # Database (auto-created)
```

## Key Features to Test

- [x] User Registration
- [x] Login/Logout
- [x] Password Reset (OTP via email)
- [x] Product Browsing
- [x] Add to Cart
- [x] Wishlist
- [x] Checkout
- [x] Payment (Razorpay)
- [x] Order History
- [x] Profile Management
- [x] Coupon Codes

## Admin Panel

Access: http://127.0.0.1:8000/admin/

Manage:
- Users
- Products
- Categories
- Orders
- Coupons
- Brands, Colors, Sizes

## API Keys Needed

### Razorpay (Payment Gateway)
1. Sign up: https://razorpay.com/
2. Get test keys from Dashboard
3. Add to .env file

### Gmail (Email Service)
1. Enable 2FA on Gmail
2. Generate App Password
3. Add to .env file

## Development Tips

- Use Django Debug Toolbar for debugging
- Check Django logs for errors
- Use Django shell for testing: `python manage.py shell`
- Run tests: `python manage.py test`

## Next Steps

1. Read SECURITY.md for security features
2. Read CHANGES.md for recent updates
3. Check SETUP.md for detailed setup
4. Review README.md for project overview

## Support

- Email: jaychauhan091202@gmail.com
- Issues: Create GitHub issue
- Documentation: See /docs folder

---

**Happy Coding! 🚀**
