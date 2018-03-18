from MayMoc import MayThanhPham
from TinhToan import giaTriTheoKhuc

#-----
class TinhGiaBeTuDong:
    def __init__(self ):
        self.MayBe = MayThanhPham(660000, 0.5, 2000, 0) #tốc độ 2000, khấu hao 5 năm tấm bỏ vô /giờ, có bù hao rồi
        self.ChiBe = 20000 #chỉ bế cho 1 bài

    def chi_phi_theo_so_luong(self, so_luong ):
        return self.ChiBe + self.MayBe.tong_chi_phi_chay_may(so_luong)

    def gia_ban_theo_day_loi_nhuan(self, day_so_luong, day_loi_nhuan, so_luong, muc_loi_nhuan_them):
        loi_nhuan = giaTriTheoKhuc(day_so_luong, day_loi_nhuan, so_luong)
        ty_le_loi_nhuan = loi_nhuan / 100
        if ty_le_loi_nhuan >= 1: #ngừa chia 0
            ty_le_loi_nhuan = 0.99
        kq1 = self.chi_phi_theo_so_luong(so_luong) + \
               self.chi_phi_theo_so_luong(so_luong) * ty_le_loi_nhuan /(1 - ty_le_loi_nhuan)
        ty_le_loi_nhuan_them = muc_loi_nhuan_them / 100
        kq2 = kq1 + kq1 * ty_le_loi_nhuan_them / (1 - ty_le_loi_nhuan_them)
        return kq2

    def gia_ban(self, so_luong, muc_loi_nhuan):
        ty_le_loi_nhuan = muc_loi_nhuan / 100
        kq = self.chi_phi_theo_so_luong(so_luong) + \
             self.chi_phi_theo_so_luong(so_luong) + ty_le_loi_nhuan / ( 1- ty_le_loi_nhuan)
        return kq


