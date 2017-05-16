from TinhToan import giaTriTheoKhuc
class MayInDigi:
    def __init__(self, clickA4, bHR, thoiGianSanSang, daySoLuongCB, dayLoiNhuanCB, tocDo):
        self.ClickTrangA4 = clickA4
        self.BHR = bHR
        self.TocDo = tocDo
        self.ThoiGianSanSang = thoiGianSanSang
        self.DaySoLuongCB  = daySoLuongCB
        self.DayLoiNhuanCB = dayLoiNhuanCB
#-----
class GiaInMayDigi:
    def __init__(self, mayInDigi, soTrangA4, tyLeSales):
        self.SoTrangA4 = soTrangA4
        self.MayInDigi = mayInDigi
        self.TyLeSales = tyLeSales/100

    def chiPhi(self ):

        phiSetup =  self.MayInDigi.ThoiGianSanSang * self.MayInDigi.BHR #Lấy giờ
        thoiGianChay = self.SoTrangA4 / self.MayInDigi.TocDo
        phiChay = thoiGianChay * self.MayInDigi.BHR;
        ketQua = phiSetup + phiChay + self.MayInDigi.ClickTrangA4;

        return ketQua

    def GiaBanCoBan(self):
        loiNhuan = giaTriTheoKhuc(self.MayInDigi.DaySoLuongCB, self.MayInDigi.DayLoiNhuanCB, self.SoTrangA4)
        tyLeLoiNhuan = loiNhuan / 100
        return self.chiPhi() +  self.chiPhi() * tyLeLoiNhuan /(1 - tyLeLoiNhuan)

    def GiaSales(self):
        return self.GiaBanCoBan() + self.GiaBanCoBan() * self.TyLeSales / ( 1- self.TyLeSales)

    def GiaTrangTB(self):
        return  self.GiaSales() / self.SoTrangA4

