import os
from flask import Flask, request, jsonify # برای اینکه بتونیم به عنوان وب‌هوک روبیکا کار کنیم
import logging # برای ثبت اتفاقات ربات

# تنظیم لاگ‌گیری برای نمایش پیام‌ها در کنسول لیارا
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    logging.info("درخواست GET دریافت شد.")
    return "سلام از ربات ایمپتیوس! من آماده‌ام." # یک پیام ساده برای تست که سرور بالاست

@app.route('/webhook', methods=['POST'])
def webhook():
    logging.info("درخواست POST (وب‌هوک) دریافت شد.")
    try:
        data = request.get_json() # دریافت داده‌های JSON از روبیکا
        logging.info(f"داده‌های دریافتی: {data}")

        # اینجا باید منطق پردازش پیام روبیکا و پاسخ‌دهی رو اضافه کنیم
        # فعلاً فقط یک پاسخ ساده برمی‌گردونیم
        return jsonify({"status": "success", "message": "پیام شما دریافت شد!"})

    except Exception as e:
        logging.error(f"خطا در پردازش وب‌هوک: {e}")
        return jsonify({"status": "error", "message": "خطایی رخ داد."}), 500

if name == '__main__':
    # پورت رو از متغیرهای محیطی لیارا می‌گیریم، اگر نبود روی 5000 قرار می‌دیم
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"ربات در حال اجرا روی پورت {port}...")
    app.run(host='0.0.0.0', port=port)
