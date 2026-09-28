class Validator:
    """Collection of validation utilities"""
    @staticmethod
    def is_email(text):
        """Check if text looks like an email"""
        if not text or '@' not in text:
            return False
        parts = text.split('@')
        return len(parts) == 2 and '.' in parts[1]

    @staticmethod
    def is_phone(text):
        """Check if text is a 10-digit US phone number"""
        digits = ''.join(c for c in text if c.isdigit())
        return len(digits) == 10
    @staticmethod
    def is_strong_password(password):
        """Check password meets strength requirements"""
        if len(password) < 8:
            return False, "Too short (min 8 chars)"
        if not any(c.isupper() for c in password):
            return False, "Need uppercase letter"
        if not any(c.islower() for c in password):
            return False, "Need lowercase letter"
        if not any(c.isdigit() for c in password):
            return False, "Need a number"
        return True, "Strong password!"

# No object needed — call directly on the class
print(Validator.is_email("alice@gmail.com")) # True
print(Validator.is_email("not-an-email")) # False
print(Validator.is_phone("555-123-4567")) # True
valid, msg = Validator.is_strong_password("Abcdefg1")
print(f"{msg}") # Strong password!

class FileHelper:
    @staticmethod
    def get_extension(filename):
        if not filename.split('.')[-1] in filename:
            pass
        return filename.split('.')[-1]
    @staticmethod
    def is_image(filename):
        if not filename.split('.')[-1] in ["jpg", "png", "gif"]:
            return False
        return True
        
print(FileHelper.get_extension("photo.jpg")) # jpg
print(FileHelper.get_extension("data.tar.gz")) # gz
print(FileHelper.is_image("photo.jpg")) # True
print(FileHelper.is_image("report.pdf")) # False