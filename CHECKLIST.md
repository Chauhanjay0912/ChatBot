# Verification Checklist

## Before Running the Application

### 1. Environment Setup
- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed: `pip install -r requirements.txt`

### 2. Configuration
- [ ] `.env` file created (copy from `.env.example`)
- [ ] SECRET_KEY configured in .env
- [ ] RAZORPAY_KEY_ID configured in .env
- [ ] RAZORPAY_KEY_SECRET configured in .env
- [ ] EMAIL_HOST_USER configured in .env
- [ ] EMAIL_HOST_PASSWORD configured in .env

### 3. Database
- [ ] Migrations created: `python manage.py makemigrations`
- [ ] Migrations applied: `python manage.py migrate`
- [ ] Superuser created: `python manage.py createsuperuser`
- [ ] (If existing DB) Passwords migrated: `python manage.py shell < migrate_passwords.py`

### 4. Files Verification
Check these files exist:
- [ ] `.env` (your local file, not in Git)
- [ ] `.env.example` (template, in Git)
- [ ] `.gitignore` (protecting sensitive files)
- [ ] `requirements.txt` (dependencies)
- [ ] `store/utils.py` (utility functions)
- [ ] `migrate_passwords.py` (migration script)

## Testing Checklist

### Authentication Tests
- [ ] Register new user
- [ ] Login with new user
- [ ] Logout
- [ ] Forgot password (receive OTP email)
- [ ] Reset password with OTP
- [ ] Login with new password

### E-commerce Tests
- [ ] Browse products
- [ ] Filter by category
- [ ] Filter by brand
- [ ] Filter by price
- [ ] Search products
- [ ] Add to cart
- [ ] Update cart quantity
- [ ] Remove from cart
- [ ] Add to wishlist
- [ ] Remove from wishlist

### Checkout Tests
- [ ] View cart
- [ ] Apply coupon code
- [ ] Enter billing details
- [ ] Razorpay payment page loads
- [ ] Complete test payment
- [ ] Receive order confirmation email
- [ ] View order history

### Profile Tests
- [ ] View profile
- [ ] Update profile information
- [ ] Upload profile image
- [ ] Change password
- [ ] View order history

### Admin Tests
- [ ] Access admin panel: http://127.0.0.1:8000/admin/
- [ ] View users
- [ ] View products
- [ ] View orders
- [ ] Add new product
- [ ] Add new category
- [ ] Add new coupon

## Security Verification

### Password Security
- [ ] New passwords are hashed (check in database)
- [ ] Cannot login with plain text password
- [ ] Password reset works correctly
- [ ] Old password verification works in profile

### Environment Variables
- [ ] No hardcoded API keys in code
- [ ] .env file not committed to Git
- [ ] Settings load from environment correctly

### Error Handling
- [ ] Invalid email shows proper error
- [ ] Invalid password shows proper error
- [ ] Duplicate email registration prevented
- [ ] Invalid OTP shows proper error

## Code Quality Verification

### Check Modified Files
```bash
# View changes in settings.py
git diff Bot/settings.py

# View changes in models.py
git diff store/models.py

# View changes in views.py
git diff store/views.py
```

### Verify Utility Functions
- [ ] `hash_password()` works
- [ ] `verify_password()` works
- [ ] `calculate_cart_total()` works
- [ ] `calculate_order_total()` works

## Documentation Verification

### Files to Review
- [ ] README.md (project overview)
- [ ] SETUP.md (setup instructions)
- [ ] SECURITY.md (security features)
- [ ] QUICKSTART.md (quick start guide)
- [ ] CHANGES.md (detailed changes)
- [ ] SUMMARY.md (executive summary)

## Deployment Checklist (Production)

### Before Deployment
- [ ] DEBUG=False in .env
- [ ] New SECRET_KEY generated
- [ ] Production database configured
- [ ] HTTPS enabled
- [ ] Static files collected: `python manage.py collectstatic`
- [ ] Media files directory configured
- [ ] Backup strategy in place

### Security Settings (Production)
Add to settings.py:
- [ ] SECURE_SSL_REDIRECT = True
- [ ] SESSION_COOKIE_SECURE = True
- [ ] CSRF_COOKIE_SECURE = True
- [ ] SECURE_BROWSER_XSS_FILTER = True
- [ ] SECURE_CONTENT_TYPE_NOSNIFF = True

### Post-Deployment
- [ ] Test all features in production
- [ ] Monitor error logs
- [ ] Test payment gateway
- [ ] Test email delivery
- [ ] Verify SSL certificate
- [ ] Test on mobile devices

## Common Issues & Solutions

### Issue: ModuleNotFoundError: No module named 'dotenv'
**Solution**: `pip install python-dotenv`

### Issue: Email not sending
**Solution**: 
1. Use Gmail App Password (not regular password)
2. Enable 2FA on Gmail account
3. Generate App Password from Google Account settings

### Issue: Razorpay payment fails
**Solution**:
1. Check API keys are correct
2. Ensure using test keys (rzp_test_...)
3. Check internet connection
4. Verify Razorpay account is active

### Issue: Old users cannot login
**Solution**:
1. Run: `python manage.py shell < migrate_passwords.py`
2. OR have users reset password
3. OR create new test accounts

### Issue: Static files not loading
**Solution**:
1. Run: `python manage.py collectstatic`
2. Check STATIC_URL in settings.py
3. Verify static files directory exists

## Performance Checklist

### Database
- [ ] Indexes on frequently queried fields
- [ ] Database connection pooling
- [ ] Query optimization

### Caching
- [ ] Consider Redis for session storage
- [ ] Cache product listings
- [ ] Cache static pages

### Monitoring
- [ ] Error logging configured
- [ ] Performance monitoring
- [ ] Uptime monitoring

## Final Verification

### Run These Commands
```bash
# Check for syntax errors
python manage.py check

# Run migrations
python manage.py migrate

# Create superuser (if not exists)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Access application
# http://127.0.0.1:8000/
```

### Verify URLs Work
- [ ] http://127.0.0.1:8000/ (home)
- [ ] http://127.0.0.1:8000/register/ (register)
- [ ] http://127.0.0.1:8000/login/ (login)
- [ ] http://127.0.0.1:8000/shop/ (shop)
- [ ] http://127.0.0.1:8000/admin/ (admin)

## Sign-Off

- [ ] All critical security issues fixed
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Ready for deployment

---

**Completed By**: _________________
**Date**: _________________
**Notes**: _________________

---

## Quick Commands Reference

```bash
# Setup
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver

# Test
python manage.py test

# Deploy
python manage.py collectstatic
python manage.py check --deploy
```

---

**Status**: ⬜ Not Started | 🟡 In Progress | ✅ Complete
