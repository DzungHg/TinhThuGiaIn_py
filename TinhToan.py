#hàm tính giá trị theo khúc
def giaTriTheoKhuc(daySoLuongS, dayGiaTriS, soLuong):
# bắt buộc số lượng phải từ 1
    result = 0
    tmpI = 0
    # Trường họp số  lượng >= số     lượng     cuối(lớn     nhất)
    if soLuong >= daySoLuongS[len(daySoLuongS) - 1]:
        tmpI = len(daySoLuongS) - 1
        result = dayGiaTriS[tmpI]
        return result
    # Lặp tiếp chỉ đến phẩn tử kế cuối for (int i = 0; i < daySoLuongS.Length - 1; i++) // chỉ đến kế cuối
    # tiếp tục
    for  i in range(0, len(daySoLuongS) - 1):
        if daySoLuongS[i] <= soLuong & soLuong < daySoLuongS[i + 1]:
            tmpI = i
            break

    result = dayGiaTriS[tmpI]

    return result

#Hàm tính giá in nnhanh theo bảng

def giaInNhanhTheoBang(khoangSoLuongS, khoangGiaS, soTrangA4):
    result = 0
    soTrangGoc = soTrangA4 #/ lưu để tính cuối.
    # tạo bản dãy chứa block trang theo độ dài
    page_blocks = [len(khoangSoLuongS)]
    i = 0
    for i in range(0, len(page_blocks) - 1):
        if soTrangA4 <= khoangSoLuongS[i + 1] - khoangSoLuongS[i]:
            page_blocks[i] = soTrangA4
            soTrangA4 = 0; # ngăn không cho cộng thêm ở cuối break;
        else:
            page_blocks[i] = khoangSoLuongS[i + 1] - khoangSoLuongS[i]
            # page num còn lại
            soTrangA4 -= page_blocks[i]

    if (soTrangA4 > 0):
        page_blocks[i] = soTrangA4
    # tính giá theo các blocks trang đã có

    for i in range(0, len(page_blocks)):
        result += page_blocks[i] * khoangGiaS[i]

    return result


