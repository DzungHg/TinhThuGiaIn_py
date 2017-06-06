from TinhToan import giaTriTheoKhuc

from MayCanPhu import *
""" Hiện nay trên thị trường đang tính như sau:
Màng offset: 200.000đ cho 1 lô gồm 200 tờ khổ máy
Số lượng tờ vượt tính 2200đ/m2


"""
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1, 10, 50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1500,2000,3000]
#dayLoiNhuanCB01 = [30,50,80, 80,80, 80, 79, 78, 77, 76, 75, 74, 72, 70, 70, 70, 70,  70, 70,   70]#chuẩn hiện tại
dayLoiNhuanCB01 = [30,50,80, 80,80, 80, 79, 78, 77, 76, 75, 74, 72, 70, 70, 70, 70,  70, 70,   70]#Thử nghiệm
""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại"""

#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
daySoLuong01 = [1,2, 10, 20, 30, 40,50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000,2000]
#daySoLuong02 = [950, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
may_can_mang = MayCanPhu(110000, 0.3, 1100, daySoLuongCB01, dayLoiNhuanCB01, 423) #tốc độ mét/giờ
ty_le_sales = 0;
gia_can_mang = TinhGiaCanPhu(may_can_mang, 0, ty_le_sales)#tạm để số cuốn 0 để thêm trong vòng lặp sau
#tính toán 01:

for i in range(0, len(daySoLuong01)):
    gia_can_mang.SoTrangA4 = daySoLuong01[i]
    loi_nhuan_theo_so_luong = giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01, gia_can_mang.SoTrangA4)
    #print (round(giaIn01.GiaSales())),
    print('SL: {0},  {1}, {2} LN: {3}'.format(gia_can_mang.SoTrangA4, round(gia_can_mang.gia_sales()), \
                                              round(gia_can_mang.gia_trung_binh_a4()), loi_nhuan_theo_so_luong))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))