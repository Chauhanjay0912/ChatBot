# EC-Chatbot Setup Instructions

## Critical Security Updates Applied

### 1. Environment Variables
- Created `.env.example` template
- Moved sensitive data (API keys, passwords) to environment variables
- Added `.gitignore` to prevent committing sensitive files

### 2. Password Security
- Implemented Django's built-in password hashing
- Updated password field length to 128 characters
- All passwords now stored as hashed values

### 3. Code Improvements
- Added utility functions to reduce code duplication
- Improved error handling with specific exceptions
- Used Django settings for API configuration

## Setup Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create Environment File**
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` with your actual credentials.

3. **Run Migrations** (Important - password field changed)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Server**
   ```bash
   python manage.py runserver
   ```

## Important Notes

- **Existing Users**: Old passwords won't work. Users need to reset passwords using "Forgot Password"
- **Production**: Set DEBUG=False in .env for production
- **API Keys**: Update Razorpay keys in .env file
- **Email**: Configure your Gmail app password in .env

## Security Checklist

✅ Passwords hashed with Django's make_password
✅ API keys moved to environment variables
✅ Sensitive files added to .gitignore
✅ Better error handling implemented
✅ Code duplication reduced with utility functions

## Next Steps (Optional Improvements)

- Add rate limiting for login attempts
- Implement CSRF tokens in forms
- Add logging for security events
- Set up HTTPS for production
- Add input validation and sanitization
