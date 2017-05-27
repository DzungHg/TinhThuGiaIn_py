from TinhToan import giaTriTheoKhuc
class MayCanPhu:
    def __init__(self, bHR, thoiGianSanSang, phiNVLM2, daySoLuongCB, dayLoiNhuanCB, tocDo):
        self.BHR = bHR
        self.TocDo = tocDo #Mét/giờ
        self.ThoiGianSanSang = thoiGianSanSang
        self.PhiNguyenVatLieuM2  = phiNVLM2
        self.DaySoLuongCB  = daySoLuongCB
        self.DayLoiNhuanCB = dayLoiNhuanCB
#-----
class TinhGiaCanPhu:
    def __init__(self, mayCanPhu, soTrang4, tyLeSales):
        self.SoTrangA4 = soTrang4

        self.MayCanPhu = mayCanPhu
        self.TyLeSales = tyLeSales / 100

    def chi_phi(self):

        phi_setup = self.MayCanPhu.ThoiGianSanSang * self.MayCanPhu.BHR #Lấy giờ
        thoi_gian_chay = (self.SoTrangA4 * 0.21)/ self.MayCanPhu.TocDo
        phi_chay = thoi_gian_chay * self.MayCanPhu.BHR;
        ket_qua = phi_setup + phi_chay;

        return ket_qua

    def gia_ban_co_ban(self):
        loi_nhuan = giaTriTheoKhuc(self.MayCanPhu.DaySoLuongCB, self.MayCanPhu.DayLoiNhuanCB, self.SoTrangA4)
        ty_le_loi_nhuan = loi_nhuan / 100
        return self.chi_phi() + self.chi_phi() * ty_le_loi_nhuan / (1 - ty_le_loi_nhuan)

    def gia_sales(self):
        return self.gia_ban_co_ban() + self.gia_ban_co_ban() * self.TyLeSales / (1 - self.TyLeSales)

    def gia_trung_binh_a4(self):
        return self.gia_sales() / self.SoTrangA4

