from TinhToan import giaTriTheoKhuc

class MayInDigi:

    def __init__(self, click_a4, b_h_r, thoi_gian_san_sang, toc_do):
        self.ClickTrangA4 = click_a4
        self.BHR = b_h_r
        self.TocDo = toc_do
        self.ThoiGianSanSang = thoi_gian_san_sang


class GiaInTheoMayToner:

    def __init__(self, may_in_digi, day_so_luong_cb, day_loi_nhuan_cb, so_trang_a4):
        self.SoTrangA4 = so_trang_a4
        self.MayInDigi = may_in_digi
        self.DaySoLuongCB = day_so_luong_cb
        self.DayLoiNhuanCB = day_loi_nhuan_cb

    def chi_phi(self):

        phiSetup =  self.MayInDigi.ThoiGianSanSang * self.MayInDigi.BHR #Lấy giờ
        thoiGianChay = self.SoTrangA4 / self.MayInDigi.TocDo
        phiChay = thoiGianChay * self.MayInDigi.BHR
        ketQua = phiSetup + phiChay + self.MayInDigi.ClickTrangA4;

        return ketQua

    def gia_ban_co_ban(self):
        ty_le_loi_nhuan_theo_khuc = giaTriTheoKhuc(self.DaySoLuongCB, self.DayLoiNhuanCB, self.SoTrangA4)
        ty_le_loi_nhuan_co_ban = ty_le_loi_nhuan_theo_khuc / 100
        if ty_le_loi_nhuan_co_ban < 1:
            return self.chi_phi()/(1 - ty_le_loi_nhuan_co_ban)
        else:
            return - 1

    def gia_sales_them(self, ty_le_sales):

        ty_le_sales_pct = ty_le_sales / 100

        if ty_le_sales_pct < 1:
            return self.gia_ban_co_ban() / (1 - ty_le_sales_pct)
        else:
            return - 1

    def gia_TB_trang_cb(self):

        return self.gia_ban_co_ban() / self.SoTrangA4

    def gia_TB_trang_sales(self):

        return self.gia_sales_them() / self.SoTrangA4

