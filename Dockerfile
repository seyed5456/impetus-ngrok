# از یک ایمیج پایه پایتون استفاده می‌کنیم
FROM python:3.10-slim-buster

# پوشه کاری رو در داکر مشخص می‌کنیم
WORKDIR /app

# فایل requirements.txt رو به پوشه کاری کپی می‌کنیم
COPY requirements.txt .

# کتابخانه‌های پایتون رو نصب می‌کنیم
RUN pip install --no-cache-dir -r requirements.txt

# تمام فایل‌های پروژه رو به پوشه کاری کپی می‌کنیم
COPY . .

# پورتی که برنامه روی اون اجرا میشه رو مشخص می‌کنیم
EXPOSE 5000

# دستور اجرای برنامه رو مشخص می‌کنیم
# از gunicorn برای اجرای Flask استفاده می‌کنیم، چون برای محیط‌های production مناسب‌تره
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
