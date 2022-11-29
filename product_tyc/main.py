

# 讓使用者輸入
# 重複輸入、持續輸入==> while True

booking = []
while True:
    name = input('請輸入產品名稱:')
    if name in ['Q', 'q']:
        break
    price = input('請輸入價格:')
    p = [name, price]
    booking.append(p)
print(booking)
