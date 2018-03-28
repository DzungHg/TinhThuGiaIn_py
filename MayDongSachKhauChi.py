from MayCanQuayTay import *
from SapCuonKhauChi import *
from MayKhauChi import *
from MayKeoGayEva import *
from TinhToan import giaTriTheoKhuc

""" Tính khâu chỉ theo 
các bước:
1. Cấn bìa /bỏ vì tính trong giá in bìa và làm bìa rồi
2. Lồng cuốn /gấp luôn 
3. Khâu chỉ
4. Keo gáy

"""

class TinhDongSachKhauChi:
    def __init__(self ):

        self.GiaLamTaySach = TinhSapCuonDeKhauChi()
        self.GiaKhauChi = TinhKhauChi()
        self.GiaKeoGay = TinhKeoGayEva()
    def chi_phi_theo_so_luong(self, so_luong_cuon ): #200 trang /cuốn
        kq = self.GiaLamTaySach.chi_phi_theo_so_luong(so_luong_cuon) \
        + self.GiaKhauChi.chi_phi_theo_so_luong(so_luong_cuon) \
        + self.GiaKeoGay.chi_phi_theo_so_luong(so_luong_cuon)
        return kq

    def gia_ban_theo_day_loi_nhuan(self, day_so_luong, day_loi_nhuan, so_luong, muc_loi_nhuan_them):
        loi_nhuan = giaTriTheoKhuc(day_so_luong, day_loi_nhuan, so_luong)
        ty_le_loi_nhuan = loi_nhuan / 100
        if ty_le_loi_nhuan >= 1: #ngừa chia 0
            ty_le_loi_nhuan = 0.99
        kq1 = self.chi_phi_theo_so_luong(so_luong) /(1 - ty_le_loi_nhuan)
        ty_le_loi_nhuan_them = muc_loi_nhuan_them / 100
        kq2 = kq1 / (1 - ty_le_loi_nhuan_them)
        return kq2

    def gia_ban(self, so_luong, muc_loi_nhuan):
        ty_le_loi_nhuan = muc_loi_nhuan / 100
        kq = self.chi_phi_theo_so_luong(so_luong)  / ( 1- ty_le_loi_nhuan)
        return kq


