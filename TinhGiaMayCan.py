from TinhToan import giaTriTheoKhuc

from MayThanhPham import *
""" Hiện nay đang tính như sau:
dạ 1 - 100  đường= 1.000 đ / đường
101 - 300 đường = 900 đ / đường
301 - 400 đường= 800 đ / đường
ví dụ 1000 tờ cấn 1 đường, em thường tính khoảng 300.000 - 350.000 đ / lô
tính khoảng 500.000 đ / lô

"""
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
dayLoiNhuanCB01 = [20,20,20,40,40,40,68,68,68,68,68,68,40,68,68,68,68,68,68,68]
""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại"""
#2). Dữ liệu cơ bản cho 1000 trang đến 10000 trang (tối đa công suất 1 máy trong ngày)
daySoLuongCB02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
dayLoiNhuanCB02 = [68,63,62,61,60,68,69,67,66,65,64,63,62,61,60,58,56,54,52,50]
#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
daySoLuong01 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 999]
daySoLuong02 = [950, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
mayCan01 = MayCanGap(500000, 0.2, daySoLuongCB01, dayLoiNhuanCB01, 5000) #tốc độ 5000 tờ giờ
tyLeSales = 0;
giaCan01 = GiaMayCanGap(mayCan01, 0, tyLeSales)
#tính toán 01:

for i in range(0, len(daySoLuong01)):
    giaCan01.SoCon = daySoLuong01[i]
    loiNhuanTheoSoLuong = giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01, giaCan01.SoCon)
    #print (round(giaIn01.GiaSales())),
    print('SL: {0},  {1}, {2} LN: {3}'.format(giaCan01.SoCon, round(giaCan01.GiaSales()), \
            round(giaCan01.GiaTrangTB()), loiNhuanTheoSoLuong))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))