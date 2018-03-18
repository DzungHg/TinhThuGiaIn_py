
class MayInDigiToner:

    def __init__(self, click_a4, b_h_r, thoi_gian_san_sang, toc_do, \
                 hao_phi_ngvl_khoi_dong, thoi_gian_xu_ly_du_dlbd):
        self.ClickTrangA4 = click_a4
        self.BHR = b_h_r
        self.TocDo = toc_do
        self.ThoiGianSanSang = thoi_gian_san_sang
        self.HaoPhiNguyenVatLieuKhoiDong = hao_phi_ngvl_khoi_dong
        self.ThoiGianXuLyDuLieuBienDoi = thoi_gian_xu_ly_du_dlbd
    def chi_phi_san_sang(self):
        kq = self.ThoiGianSanSang * self.BHR
        return kq
    def chi_phi_du_lieu_bien_doi(self):
        kq = self.ThoiGianXuLyDuLieuBienDoi * self.BHR
        return kq
    def chi_phi_nguyen_vat_lieu_khoi_dong(self):
        kq = self.HaoPhiNguyenVatLieuKhoiDong
        return kq
    def chi_phi_theo_toc_do(self, so_luong):
        thoi_gian_chay = 0
        if (self.TocDo > 0):
            thoi_gian_chay = so_luong / self.TocDo
        kq = thoi_gian_chay * self.BHR
        return kq
    def tong_chi_phi_chay_may(self, so_luong):
        return self.chi_phi_san_sang() + self.chi_phi_du_lieu_bien_doi() \
        + self.chi_phi_nguyen_vat_lieu_khoi_dong() + self.chi_phi_theo_toc_do(so_luong)

class MayThanhPham:
    def __init__(self, b_h_r, thoi_gian_san_sang, toc_do, hao_phi_ngvl_khoi_dong):
        self.BHR = b_h_r
        self.TocDo = toc_do
        self.ThoiGianSanSang = thoi_gian_san_sang
        self.HaoPhiNguyenVatLieuKhoiDong = hao_phi_ngvl_khoi_dong
    def chi_phi_san_sang(self):
        kq = self.ThoiGianSanSang * self.BHR
        return kq
    def chi_phi_nguyen_vat_lieu_khoi_dong(self):
        kq = self.HaoPhiNguyenVatLieuKhoiDong
        return kq
    def chi_phi_theo_toc_do(self, so_luong):
        thoi_gian_chay = 0
        if (self.TocDo > 0):
            thoi_gian_chay = so_luong / self.TocDo
        return thoi_gian_chay * self.BHR
    def tong_chi_phi_chay_may(self, so_luong):
        return self.chi_phi_san_sang() + self.chi_phi_nguyen_vat_lieu_khoi_dong()\
               + self.chi_phi_theo_toc_do(so_luong)