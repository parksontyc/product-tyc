

# 讓使用者輸入
# 重複輸入、持續輸入==> while True

booking = []
while True:
    name = input('請輸入產品名稱:')
    if name == '':
        print('請輸入產品名稱/q離開')
        name = input('請輸入產品名稱:')
        if name == 'q':
            break
    if name == 'q':
        break
    price = input('請輸入價格:')
    booking.append([name, price])
print(booking)


# 寫入檔案
with open('booking.csv', 'w') as f:
    for line in booking:
        f.write(line)  # TypeError: write() argument must be str, not list