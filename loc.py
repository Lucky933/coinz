# Đọc nội dung các file vào list
with open('very_done.txt', 'r') as f:
    very_done_lines = f.read().splitlines()

with open('cookies.txt', 'r') as f:
    cookies_lines = f.read().splitlines()

# Tìm và lưu các hàng không trùng nhau vào một list
unique_lines = [line for line in cookies_lines if line not in very_done_lines]

# Mở file very_fail.txt và ghi các hàng không trùng nhau vào file đó
with open('very_fail.txt', 'w') as f:
    for line in unique_lines:
        f.write(line + '\n')

# Lấy đầy đủ kí tự của các hàng không trùng nhau
full_lines = []
with open('cookies.txt', 'r') as f:
    for line in f:
        if line.strip() in unique_lines:
            full_lines.append(line)

# Ghi lại đầy đủ kí tự vào file very_fail.txt
with open('very_fail.txt', 'w') as f:
    for line in full_lines:
        f.write(line)
