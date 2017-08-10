from TinhToan import giaTriTheoKhuc



'''Dựa trên giá An Nhân đã trừ giấy'''
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
# An nhân đã bao gồm fort 100, 120, 250, c 100 -> 300gsm
daySoTrang01 =     [1,    6,     16,   80,   120,  560,  1001]
day_gia_gom_giay = [10000, 8000, 5000, 3000, 2500, 2200, 2000]

""" dữ liệu trên đã đúng với giá in nhanh VIP1 hiện tại
 giá in này chưa bao gồm giấy
"""
#
#Dãy trang để tính giá
dayTrang01 = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,999]
dayTrang02 = [950,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]

tyLeSales = 0;

#tính toán 01:

for i in range(len(dayTrang01)):
    #print (round(giaIn01.GiaSales())),
    soTrangTinh = dayTrang01[i]
    giaTheoSoTrangTinh = giaTriTheoKhuc(daySoTrang01, day_gia_gom_giay, soTrangTinh)
    tong_gia = giaTheoSoTrangTinh * soTrangTinh
    giaTrungBinhTrang = tong_gia / soTrangTinh
    #bao gồm giấy
    #print('SL: {0}, {1}, {2}'.format(soTrangTinh, round(tong_gia) , \
     #                                 round(giaTrungBinhTrang)))
    #trừ giấy TB: 350 đồng
    print('SL: {0}, {1}, {2}'.format(soTrangTinh, round(tong_gia), \
                                     round(giaTrungBinhTrang - 350)))


#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))