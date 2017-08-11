from TinhToan import giaTriTheoKhuc
class MayInDigi:

    def __init__(self, clickA4, bHR, thoiGianSanSang, daySoLuongCB, dayLoiNhuanCB, tocDo):
        self.ClickTrangA4 = clickA4
        self.BHR = bHR
        self.TocDo = tocDo
        self.ThoiGianSanSang = thoiGianSanSang
        self.DaySoLuongCB  = daySoLuongCB
        self.DayLoiNhuanCB = dayLoiNhuanCB

class GiaInMayDigi:

    def __init__(self, mayInDigi, soTrangA4, tyLeSales):
        self.SoTrangA4 = soTrangA4
        self.MayInDigi = mayInDigi
        self.TyLeSales = tyLeSales/100

    def chi_phi(self):

        phiSetup =  self.MayInDigi.ThoiGianSanSang * self.MayInDigi.BHR #Lấy giờ
        thoiGianChay = self.SoTrangA4 / self.MayInDigi.TocDo
        phiChay = thoiGianChay * self.MayInDigi.BHR;
        ketQua = phiSetup + phiChay + self.MayInDigi.ClickTrangA4;

        return ketQua

    def gia_ban_co_ban(self):
        loiNhuan = giaTriTheoKhuc(self.MayInDigi.DaySoLuongCB, self.MayInDigi.DayLoiNhuanCB, self.SoTrangA4)
        tyLeLoiNhuan = loiNhuan / 100
        if tyLeLoiNhuan > 0:
            return self.chi_phi() + self.chi_phi() * tyLeLoiNhuan / (1 - tyLeLoiNhuan)
        else:
            return self.chi_phi() + self.chi_phi() * 0

    def gia_sales(self):

        if self.TyLeSales > 0:
            return self.gia_ban_co_ban() + self.gia_ban_co_ban() * self.TyLeSales / (1 - self.TyLeSales)
        else:
            return self.gia_ban_co_ban() + self.gia_ban_co_ban() * 0

    def GiaTrangTB(self):

        return self.gia_sales() / self.SoTrangA4

