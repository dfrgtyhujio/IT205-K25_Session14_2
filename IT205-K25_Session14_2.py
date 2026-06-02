# Biến total_points ở dòng 2 là biến toàn cục (Global) vì nó được khai báo ở ngoài cùng của file code, không nằm trong bất kỳ hàm nào.
# Python coi total_points trong hàm là biến cục bộ vì phép gán (=) bên trong hàm đã kích hoạt cơ chế tự tạo một biến cục bộ mới trùng tên.
# Nếu chỉ đọc (print) giá trị của total_points bên trong hàm mà không thực hiện phép gán đổi giá trị thì chương trình sẽ không bị lỗi.
# Từ khóa 'global' giúp khai báo sử dụng biến toàn cục bên trong hàm, dòng lệnh cụ thể là: global total_points.
# Một hàm tốt nên nhận hai tham số đầu vào và dùng lệnh 'return' để trả về tổng điểm mới sau khi đã cộng dồn.


total_points = 100

def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)
