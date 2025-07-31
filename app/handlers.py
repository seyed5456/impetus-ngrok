def generate_reply(message):
    if "سلام" in message:
        return "سلامی به ژرفای تاریخ!"
    elif "فلسفه" in message:
        return "افلاطون می‌گه: دانستن، رنج بردنه!"
    elif "طنز" in message:
        return "ما فقط شوخی نمی‌کنیم، حقیقت رو با خنده تلخش می‌گیم."
    else:
        return "اینجا Impetusه، جایی برای معنا. چی می‌خوای بدونی؟"
