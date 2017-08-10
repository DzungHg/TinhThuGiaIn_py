from TinhToan import giaTriTheoKhuc

from MayInNhanh import *
# Tính thử về lợi nhuận
daySoLuong = [1,50,100,150,200]
dayLoiNhuan = [50,60,70,80,90]

#print(giaTriTheoKhuc(daySoLuong, dayLoiNhuan, 52))
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
dayLoiNhuanCB01 = [30,65,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68]

#2). Dãy lợi nhuận cần cạnh tranh tối đa
day_so_luong_canh_tranh = [1,50,  100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
day_loi_nhuan_canh_tranh = [50,50,50  ,50,50, 50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
'''Cạnh tranh nên xem sao'''
#2). Dữ liệu cơ bản cho 1000 trang đến 10000 trang (tối đa công suất 1 máy trong ngày)
#daySoLuongCB02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
#dayLoiNhuanCB02 = [68,63,  62,  61,  60,  68,  69,  67,  66,  65,  64,  63,  62,  61,  60,  58,  56,  54,  52,  50]
'''Mức này đang lãi như Kprint'''
##tinh thử ngày 10/08/2017
"""Tính hình thị trường có thể giảm"""
daySoLuongCB02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
dayLoiNhuanCB02 = [68,65,  63,  61,  60,  59,  58,  57,  56,  55,  54,  53,  52,  51,  50,  49,  48,  47,  46,  45]

#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
dayTrang01 = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,999]
dayTrang02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
mayin01 = MayInDigi(450, 760000, 0.08, day_so_luong_canh_tranh, day_so_luong_canh_tranh, 1200 ) #tốc độ 1200 a4/giờ
ty_le_sales_khach_cuoi = 0 #điều chỉnh thử theo An nhân
giaIn01 = GiaInMayDigi(mayin01, 0, ty_le_sales_khach_cuoi)
#tính toán 01:

for i in range(0,len(dayTrang02)):
    giaIn01.SoTrangA4 = dayTrang01[i]
    #print (round(giaIn01.GiaSales())),
   # print('SL: {0},  {1}, {2} LN: {3}'.format(giaIn01.SoTrangA4, round(giaIn01.GiaSales()),\
    #      round(giaIn01.GiaTrangTB()), giaTriTheoKhuc(daySoLuongCB02, dayLoiNhuanCB02,giaIn01.SoTrangA4)))

    print('SL: {0},  {1}, {2} LN: {3}'.format(giaIn01.SoTrangA4, round(giaIn01.GiaSales()), \
                                              round(giaIn01.GiaTrangTB()),
                                              giaTriTheoKhuc(day_so_luong_canh_tranh, day_loi_nhuan_canh_tranh, \
                                              giaIn01.SoTrangA4)))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))