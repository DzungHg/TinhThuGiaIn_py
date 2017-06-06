from TinhToan import giaTriTheoKhuc
class MayDongSach:
    def __init__(self, bHR, thoiGianSanSang, phiNVLChoMotCuon, daySoLuongCB, dayLoiNhuanCB, tocDo):
        self.BHR = bHR
        self.TocDo = tocDo
        self.ThoiGianSanSang = thoiGianSanSang
        self.PhiNguyenLieuChoMotCuon  = phiNVLChoMotCuon
        self.DaySoLuongCB  = daySoLuongCB
        self.DayLoiNhuanCB = dayLoiNhuanCB
#-----
class TinhGiaDongSach:
    def __init__(self, mayDongSach, soCuon, tyLeSales):
        self.SoCuon = soCuon

        self.MayDongSach = mayDongSach
        self.TyLeSales = tyLeSales / 100

    def chiPhi(self ):

        phiSetup = self.MayDongSach.ThoiGianSanSang * self.MayDongSach.BHR #Lấy giờ
        thoiGianChay = self.SoCuon / self.MayDongSach.TocDo
        phiChay = thoiGianChay * self.MayDongSach.BHR
        phi_nguyen_lieu_cho_cuon = self.MayDongSach.PhiNguyenLieuChoMotCuon * self.SoCuon
        ketQua = phiSetup + phiChay + phi_nguyen_lieu_cho_cuon

        return ketQua

    def GiaBanCoBan(self):
        loiNhuan = giaTriTheoKhuc(self.MayDongSach.DaySoLuongCB, self.MayDongSach.DayLoiNhuanCB, self.SoCuon)
        tyLeLoiNhuan = loiNhuan / 100
        return self.chiPhi() +  self.chiPhi() * tyLeLoiNhuan /(1 - tyLeLoiNhuan)

    def GiaSales(self):
        return self.GiaBanCoBan() + self.GiaBanCoBan() * self.TyLeSales / ( 1- self.TyLeSales)

    def GiaTrungBinhCuon(self):
        return  self.GiaSales() / self.SoCuon

