from TinhToan import giaTriTheoKhuc

from MayInNhanh import *
# Tính thử về lợi nhuận
daySoLuong = [1,50,100,150,200]
dayLoiNhuan = [50,60,70,80,90]

#print(giaTriTheoKhuc(daySoLuong, dayLoiNhuan, 52))
#1). Dữ liệu cơ bản 01 hớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950]
dayLoiNhuanCB01 = [30,65,68,68,90,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80]

#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
dayTrang01 = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,999]
mayin01 = MayInDigi(450, 760000, 0.08, daySoLuongCB01, dayLoiNhuanCB01, 1200 ) #tốc độ 1200 a4/giờ
tyLeSales = 0;
giaIn01 = GiaInMayDigi(mayin01,0,tyLeSales)
#tính toán 01:

for i in range(0,len(dayTrang01)-1):
    giaIn01.SoTrangA4 = dayTrang01[i]
    #print (round(giaIn01.GiaSales())),
    print('SL: {0},  {1}, {2} LN: {3}'.format(giaIn01.SoTrangA4, round(giaIn01.GiaSales()),\
          round(giaIn01.GiaTrangTB()), giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,giaIn01.SoTrangA4)))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))