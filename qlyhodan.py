import csv
import os


def menu():
    print("1: Mở file danh sách")
    print("2: Nhập thông tin các cửa hộ dân")
    print("3: Tính trợ cấp ")
    print("4: Lưu danh sách")
    print("5: Sắp xếp các hộ dân")
    print("6: Kết thúc chương trình")


path_hien_tai = os.getcwd()
path_csv = os.path.join(path_hien_tai, "files\\ds_ho_dan.csv")

def mo_file():
    with open(path_csv, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        danh_sach_ho_dan = [row for row in reader]
    return danh_sach_ho_dan

def nhap_ho_dan():
    ma_ho = input("nhập vào mã hộ: ")
    ten_chu_ho = input("nhập vào tên chủ hộ: ")
    so_thanh_vien = int(input("nhập vào số thành viên: "))
    muc_thu_nhap = float(input("nhập vào mức thu nhập: "))
    ho_ngheo = input("Hộ nghèo(True/False): ").lower() == "true"
    tro_cap = tinh_tro_cap(ho_ngheo, so_thanh_vien)
    return [ma_ho, ten_chu_ho, so_thanh_vien, muc_thu_nhap, ho_ngheo, tro_cap]

def tinh_tro_cap(ho_ngheo, so_thanh_vien):
    if ho_ngheo:
        if int(so_thanh_vien) >= 5:
            return 1000000
        elif 3 <= int(so_thanh_vien) < 5:
            return 800000
        elif 1 <= int(so_thanh_vien) < 3:
            return 500000
    return 0

def luu_file(danh_sach_can_xu_li):
    with open(path_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(danh_sach_can_xu_li)

def hien_danh_sach(danh_sach_can_xu_li):
    for row in danh_sach_can_xu_li:
        print(row)















def hien_thong_tin_ho_nhap_thap_nhat(danh_sach_can_xu_li):
    if not danh_sach_can_xu_li:
        print("Danh sách rỗng.")
        return

    ho_nhap_thap_nhat = min(danh_sach_can_xu_li, key=lambda x: x[3])  # Sắp xếp theo thu nhập (cột 3)
    
    print("\nThông tin của hộ có thu nhập nhỏ nhất:")
    print("Mã hộ:", ho_nhap_thap_nhat[0])
    print("Tên chủ hộ:", ho_nhap_thap_nhat[1])
    print("Số thành viên:", ho_nhap_thap_nhat[2])
    print("Mức thu nhập:", ho_nhap_thap_nhat[3])
    print("Hộ nghèo:", ho_nhap_thap_nhat[4])
    print("Trợ cấp:", ho_nhap_thap_nhat[5])

def xoa_ho_dan_theo_ten(danh_sach_can_xu_li, ten_chu_ho):
    danh_sach_can_xu_li = [ho for ho in danh_sach_can_xu_li if ho[1] != ten_chu_ho]
    print(f"Hộ dân với tên chủ hộ {ten_chu_ho} đã được xóa khỏi danh sách.")

def thong_ke_muc_thu_nhap(danh_sach_can_xu_li):
    if not danh_sach_can_xu_li:
        print("Danh sách rỗng.")
        return

    muc_thu_nhap = [float(ho[3]) for ho in danh_sach_can_xu_li if ho[3].replace('.', '').isdigit()]  # Tạo danh sách mức thu nhập

    if muc_thu_nhap:
        # Tính tổng, trung bình, lớn nhất và nhỏ nhất
        tong_thu_nhap = sum(muc_thu_nhap)
        trung_binh_thu_nhap = tong_thu_nhap / len(muc_thu_nhap)
        max_thu_nhap = max(muc_thu_nhap)
        min_thu_nhap = min(muc_thu_nhap)

        # Hiển thị kết quả
        print("\nThống kê mức thu nhập:")
        print("Tổng thu nhập:", tong_thu_nhap)
        print("Trung bình thu nhập:", trung_binh_thu_nhap)
        print("Thu nhập lớn nhất:", max_thu_nhap)
        print("Thu nhập nhỏ nhất:", min_thu_nhap)
    else:
        print("Không có dữ liệu mức thu nhập để thống kê.")

def loc_theo_muc_thu_nhap(danh_sach_can_xu_li, gioi_han_thu_nhap):
    ho_khau = [ho for ho in danh_sach_can_xu_li if ho[3] > gioi_han_thu_nhap]

    if ho_khau:
        print(f"\nDanh sách hộ dân có thu nhập lớn hơn {gioi_han_thu_nhap}:")
        for ho in ho_khau:
            print(ho)
    else:
        print(f"Không có hộ dân nào có thu nhập lớn hơn {gioi_han_thu_nhap}.")

def tim_ho_co_tro_cap_cao_nhat(danh_sach_can_xu_li):
    if not danh_sach_can_xu_li:
        print("Danh sách rỗng.")
        return

    ho_tro_cap_cao_nhat = max(danh_sach_can_xu_li, key=lambda x: x[5])  # Sắp xếp theo trợ cấp (cột 5)

    print("\nThông tin của hộ có trợ cấp cao nhất:")
    print("Mã hộ:", ho_tro_cap_cao_nhat[0])
    print("Tên chủ hộ:", ho_tro_cap_cao_nhat[1])
    print("Số thành viên:", ho_tro_cap_cao_nhat[2])
    print("Mức thu nhập:", ho_tro_cap_cao_nhat[3])
    print("Hộ nghèo:", ho_tro_cap_cao_nhat[4])
    print("Trợ cấp:", ho_tro_cap_cao_nhat[5])










danh_sach_ho_dan = []

while True:
    menu()
    lua_chon = int(input("nhập vào chức năng muốn chọn: "))
    if lua_chon == 1:
        danh_sach_ho_dan = mo_file()
        print(danh_sach_ho_dan)
    elif lua_chon == 2:
        thong_tin = nhap_ho_dan()
        danh_sach_ho_dan.append(thong_tin)
    elif lua_chon == 3:
        for row in danh_sach_ho_dan:
            row[5] = tinh_tro_cap(row[4], row[2])
    elif lua_chon == 4:
        luu_file(danh_sach_ho_dan)
    elif lua_chon == 5:
        print("danh sách trước khi sắp xếp: ")
        hien_danh_sach(danh_sach_ho_dan)
        print("\ndanh sách sau khi sắp xếp: ")
        for row in danh_sach_ho_dan: 
            row[2] = int(row[2])
        danh_sach_ho_dan.sort(key=lambda x: x[2], reverse = True)
        hien_danh_sach(danh_sach_ho_dan)




    elif lua_chon == 7:
        hien_thong_tin_ho_nhap_thap_nhat(danh_sach_ho_dan)
    elif lua_chon == 8:
        ten_chu_ho_can_xoa = input("Nhập tên chủ hộ cần xóa: ")
        xoa_ho_dan_theo_ten(danh_sach_ho_dan, ten_chu_ho_can_xoa)
    elif lua_chon == 9:
        thong_ke_muc_thu_nhap(danh_sach_ho_dan)
    elif lua_chon == 10:
        gioi_han_thu_nhap = float(input("Nhập mức thu nhập tối thiểu: "))
        loc_theo_muc_thu_nhap(danh_sach_ho_dan, gioi_han_thu_nhap)
    elif lua_chon == 11:
        tim_ho_co_tro_cap_cao_nhat(danh_sach_ho_dan)
    else:
        break
