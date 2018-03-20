from MayBeTruyenThong import *
from TinhToan import giaTriTheoKhuc


""" 
Thị trường lên khuôn: 

"""
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1, 10, 50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1500,2000,3000]
#dayLoiNhuanCB01 = [30,50,80, 80,80, 80, 79, 78, 77, 76, 75, 74, 72, 70, 70, 70, 70,  70, 70,   70]#chuẩn hiện tại
#điều chỉnh lại:
dayLoiNhuanCB01 = [30,60,60, 60,60, 60, 60, 60, 60, 60, 60, 50, 50, 50, 50, 50, 45,  45, 45,   45]
""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại"""

#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
daySoLuong01 = [1,2, 10, 20, 30, 40,50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000,2000]
#daySoLuong02 = [950, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]

gia_be = TinhGiaBeTruyenThong()
muc_loi_nhuan_them = 0;
#tính toán 01:

for i in range(0, len(daySoLuong01)):
    so_luong = daySoLuong01[i]
    loi_nhuan_theo_so_luong = giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01, so_luong)
    #print (round(giaIn01.GiaSales())),
    gia_ban_theo_day_loi_nhuan = gia_be.gia_ban_theo_day_loi_nhuan(dayLoiNhuanCB01,\
                                            dayLoiNhuanCB01,so_luong, muc_loi_nhuan_them)
    gia_trung_binh_sp = gia_ban_theo_day_loi_nhuan / so_luong
    print('SL: {0},  {1}, {2} LN: {3}'.format(so_luong, round(gia_ban_theo_day_loi_nhuan), \
        round(gia_trung_binh_sp), loi_nhuan_theo_so_luong + muc_loi_nhuan_them))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))