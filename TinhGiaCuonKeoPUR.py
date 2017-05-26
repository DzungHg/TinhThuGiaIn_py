from TinhToan import giaTriTheoKhuc

from MayDongSach import *
""" Hiện nay đang tính như sau:
dạ 1 - 100  đường= 1.000 đ / đường
101 - 300 đường = 900 đ / đường
301 - 400 đường= 800 đ / đường
ví dụ 1000 tờ cấn 1 đường, em thường tính khoảng 300.000 - 350.000 đ / lô
tính khoảng 500.000 đ / lô

"""
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
dayLoiNhuanCB01 = [35,30,35,40,40,40,45,45,45,45,45,45,45,45,45,45,45,45,45,45]
""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại"""

#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
daySoLuong01 = [1,50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
#daySoLuong02 = [950, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
mayDongSach01 = MayDongSach(300000, 0.3, 1250, daySoLuongCB01, dayLoiNhuanCB01, 80) #tốc độ 5000 tờ giờ
tyLeSales = 0;
giaDongCuon01 = TinhGiaDongSach(mayDongSach01, 0, tyLeSales)#tạm để số cuốn 0 để thêm trong vòng lặp sau
#tính toán 01:

for i in range(0, len(daySoLuong01)):
    giaDongCuon01.SoCuon = daySoLuong01[i]
    loiNhuanTheoSoLuong = giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01, giaDongCuon01.SoCuon)
    #print (round(giaIn01.GiaSales())),
    print('SL: {0},  {1}, {2} LN: {3}'.format(giaDongCuon01.SoCuon, round(giaDongCuon01.GiaSales()), \
                                              round(giaDongCuon01.GiaTrungBinhCuon()), loiNhuanTheoSoLuong))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))