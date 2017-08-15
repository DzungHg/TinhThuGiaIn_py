from TinhToan import giaTriTheoKhuc

from MayInNhanh import *
#1 Dãy lợi nhuận cần cạnh tranh 1
day_so_luong_cb1 = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
day_loi_nhuan_cb1 = [62, 62, 62  , 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62]

#2). Dãy lợi nhuận cần cạnh tranh 2
day_so_luong_cb2 = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
day_loi_nhuan_cb2 = [50, 50, 50  , 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

#máy in
may_in_re_co = MayInDigi(450, 760000, 0.08,1200) #tốc độ 1200 a4/giờ

gia_in_may_recoh = GiaInTheoMayToner(may_in_re_co, day_so_luong_cb1, day_loi_nhuan_cb1, 0)

#tính toán theo giá cơ bản xem ra sao theo dãy trang tính:
day_trang_01 = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 999]

for i in range(0,len(day_trang_01)):
    gia_in_may_recoh.SoTrangA4 = day_trang_01[i]
    #print (round(giaIn01.GiaSales())),
   # print('SL: {0},  {1}, {2} LN: {3}'.format(giaIn01.SoTrangA4, round(giaIn01.GiaSales()),\
    #      round(giaIn01.GiaTrangTB()), giaTriTheoKhuc(daySoLuongCB02, dayLoiNhuanCB02,giaIn01.SoTrangA4)))

    print('SL: {0},  {1}, {2} LN: {3}%'.format(gia_in_may_recoh.SoTrangA4, round(gia_in_may_recoh.gia_ban_co_ban()), \
                                              round(gia_in_may_recoh.gia_TB_trang_cb()),
                                              giaTriTheoKhuc(day_so_luong_cb1, day_loi_nhuan_cb1, \
                                                             gia_in_may_recoh.SoTrangA4)))



#print('{0}'.format(giaTriTheoKhuc(daySoLuongCB01, dayLoiNhuanCB01,50)))