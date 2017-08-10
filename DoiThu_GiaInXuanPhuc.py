from TinhToan import giaTriTheoKhuc



#print(giaTriTheoKhuc(daySoLuong, dayLoiNhuan, 52))
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
# An nhân đã bao gồm fort 100, 120, 250, c 100 -> 300gsm
daySoTrang01 = [1,4,   11,  101,  201,   501,  1001, 2001]
dayGia01 =     [0,8000,4000,1800, 1600, 1500, 1200,  2000]
dayGiaKM30Pct = [0,5600,2800,1300, 1200, 1100, 900,  700]
""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại"""
#
#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
dayTrang01 = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,999]
dayTrang02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]

tyLeSales = 0;

#tính toán 01:

for i in range(len(dayTrang01)):
    #print (round(giaIn01.GiaSales())),
    soTrangTinh = dayTrang01[i]
    giaTheoSoTrangTinh = giaTriTheoKhuc(daySoTrang01, dayGiaKM30Pct, soTrangTinh)
    tong_gia = giaTheoSoTrangTinh * soTrangTinh
    giaTrungBinhTrang = tong_gia / soTrangTinh
    print('SL: {0}, {1}, {2}'.format(soTrangTinh, round(tong_gia) , \
                                      round(giaTrungBinhTrang)))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))