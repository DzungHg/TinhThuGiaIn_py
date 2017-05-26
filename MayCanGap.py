from TinhToan import giaTriTheoKhuc
class MayCanGap:
    def __init__(self, bHR, thoiGianSanSang, tGSSThemMotDuongCan, daySoLuongCB, dayLoiNhuanCB, tocDo):
        self.BHR = bHR
        self.TocDo = tocDo
        self.ThoiGianSanSang = thoiGianSanSang
        self.TGSS_ThemMotDuongCan  = tGSSThemMotDuongCan
        self.DaySoLuongCB  = daySoLuongCB
        self.DayLoiNhuanCB = dayLoiNhuanCB
#-----
class GiaMayCanGap:
    def __init__(self, mayCanGap, soCon, soDuong, tyLeSales):
        self.SoCon = soCon
        self.SoDuongCan = soDuong
        self.MayCanGap = mayCanGap
        self.TyLeSales = tyLeSales / 100

    def chiPhi(self ):
        thGianSanSang = self.MayCanGap.ThoiGianSanSang + (self.SoDuongCan - 1) * \
                        self.MayCanGap.TGSS_ThemMotDuongCan
        phiSetup = thGianSanSang * self.MayCanGap.BHR #Lấy giờ
        thoiGianChay = self.SoCon / self.MayCanGap.TocDo
        phiChay = thoiGianChay * self.MayCanGap.BHR;
        ketQua = phiSetup + phiChay;

        return ketQua

    def GiaBanCoBan(self):
        loiNhuan = giaTriTheoKhuc(self.MayCanGap.DaySoLuongCB, self.MayCanGap.DayLoiNhuanCB, self.SoCon)
        tyLeLoiNhuan = loiNhuan / 100
        return self.chiPhi() +  self.chiPhi() * tyLeLoiNhuan /(1 - tyLeLoiNhuan)

    def GiaSales(self):
        return self.GiaBanCoBan() + self.GiaBanCoBan() * self.TyLeSales / ( 1- self.TyLeSales)

    def GiaTrangTB(self):
        return  self.GiaSales() / self.SoCon

