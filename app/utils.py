import re

def clean_text(text):
    # حذف ایموجی‌ها، فاصله‌های اضافی و کاراکترهای خاص
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def contains_keyword(text, keywords):
    return any(kw in text for kw in keywords)
