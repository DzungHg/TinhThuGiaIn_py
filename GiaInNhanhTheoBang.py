from TinhToan import giaInNhanhTheoBang
#dữ liệu để tính giá in nhanh
#/dữ liệu giá bảng 1
level_steps = [1, 11, 51, 101]
level_prices = [20000, 7000, 4000, 3000]
#bảng VIP
'''Mục tiêu làm sao 400trang giá còn 2000 đồng'''
level_steps02 = [1, 11, 51, 101]
level_prices02 = [20000, 7000, 4000, 1000]
#tính thử theo bảng 1
so_trang = input("Nhập số rang A4: ")

print(giaInNhanhTheoBang(level_steps02, level_prices02, int(so_trang)))