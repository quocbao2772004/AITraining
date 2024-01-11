Thư viện NumPy là một thư viện quan trọng trong ngôn ngữ lập trình Python, 
được sử dụng để làm việc với mảng và ma trận, cùng với một loạt các chức năng
toán học hiệu quả. Dưới đây là một số câu lệnh phổ biến và ví dụ minh họa khi 
sử dụng NumPy.
Cài đặt thư viện Numpy
 - Mở Command Prompt và gõ lệnh: pip install numpy
Các thao tác với Numpy
1. Khai báo thư viện
import numpy as np
2. Khởi tạo mảng: np.array()
a) Khởi tạo mảng một chiều
#Khởi tạo mảng một chiều với kiểu dữ liệu các phần tử là Integer
arr = np.array([1,3,4,5,6], dtype = int)

#Khởi tạo mảng một chiều với kiểu dữ liệu mặc định
arr = np.array([1,3,4,5,6])

print(arr)
OUTPUT:
[1 3 4 5 6]
b) Khởi tạo mảng hai chiều
arr1 = np.array([(4,5,6), (1,2,3)], dtype = int)

print(arr1)
OUTPUT:
[[4 5 6]
 [1 2 3]]
c) Khởi tạo mảng ba chiều
arr2 = np.array(([(2,4,0,6), (4,7,5,6)],
                 [(0,3,2,1), (9,4,5,6)],
                 [(5,8,6,4), (1,4,6,8)]), dtype = int)

print(arr2)
OUTPUT:
[[[2 4 0 6]
  [4 7 5 6]]
 [[0 3 2 1]
  [9 4 5 6]]
 [[5 8 6 4]
  [1 4 6 8]]]
d) Khởi tạo với các hàm có sẵn
np.zeros((3,4), dtype = int): Tạo mảng hai chiều các phần tử 0 với kích thước 3x4.
np.ones((2,3,4), dtype = int): Tạo mảng 3 chiều các phần tử 1 với kích thước 2x3x4.
np.arange(4): Tạo mảng với các phần tử từ 0 đến 3, bước nhảy đơn vị.
np.arange(1,7,2): Tạo mảng với các phần tử từ 1 - 6 với bước nhảy là 2.
np.linspace(1,10,5): Tạo mảng từ 1 đến 10, có 5 phần tử, các phần tử cách đều nhau.
np.full((2,3),5): Tạo mảng 2 chiều các phần tử 5 với kích thước 2x3.
np.eye(4, dtype=int): Tạo ma trận đơn vị với kích thước là 4x4.
np.random.random((2,3)): Tạo ma trận các phần tử ngẫu nhiên với kích thước 2x3.
3. Thao tác với mảng
dtype: Kiểu dữ liệu của phần tử trong mảng.
shape: Kích thước của mảng.
size: Số phần tử trong mảng.
ndim: Số chiều của mảng.
arr2 = np.array(([(2,4,0,6), (4,7,5,6)],
                 [(0,3,2,1), (9,4,5,6)],
                 [(5,8,6,4), (1,4,6,8)]), dtype = int)
print("Kiểu dữ liệu của phần tử trong mảng:", arr2.dtype)
print("Kích thước của mảng:", arr2.shape)
print("Số phần tử trong mảng:", arr2.size)
print("Số chiều của mảng:", arr2.ndim)
Output:
Kiểu dữ liệu của phần tử trong mảng: int32
Kích thước của mảng: (3, 2, 4)
Số phần tử trong mảng: 24
Số chiều của mảng: 3
Truy cập phần tử trong mảng
Các phần tử trong mảng được đánh số từ 0 trở đi
arr[i]: Truy cập tới phần tử thứ i của mảng 1 chiều.
arr[i,j]: Truy cập tới phần tử hàng i, cột j của mảng 2 chiều.
arr[n,i,j]: Truy cập tới phần tử chiều n, hàng i, cột j của mảng 3 chiều.
arr[a:b]: Truy cập tới các phần tử từ a đến b-1 trong mảng 1 chiều.
arr[:,:]: Truy cập tới tất cả các phần tử trong mảng 2 chiều.
Truy cập một dòng cụ thể:
import numpy as np
# Tạo một mảng 2 chiều 3x3
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Truy cập dòng thứ 1
row_1 = arr_2d[1, :]
print(row_1)
Kết quả:
[4 5 6]
Truy cập một cột cụ thể:
# Truy cập cột thứ 2
col_2 = arr_2d[:, 2]
print(col_2)
Kết quả:
[3 6 9]
Truy cập một phần của mảng:
# Truy cập một phần gồm các hàng từ 0 đến 1 và cột từ 1 đến 2
sub_arr = arr_2d[0:2, 1:3]
print(sub_arr)
Kết quả:
[[2 3]
 [5 6]]

Đọc mảng từ file .txt

diem_2a = np.loadtxt('Diem_2A.txt', dtype = int,delimiter=',') 
print("File dữ liệu điểm lớp 2A:\n", diem_2a)
Output

Một số toán tử phổ biến trong NumPy:
Toán tử số học:
+ (cộng)
- (trừ)
* (nhân)
/ (chia)
** (mũ)
Toán tử so sánh:
< (nhỏ hơn)
> (lớn hơn)
<= (nhỏ hơn hoặc bằng)
>= (lớn hơn hoặc bằng)
== (bằng)
!= (khác nhau)
Toán tử logic:
& (and)
| (or)
~ (not)
Toán tử khác:
np.sum() (tổng các phần tử)
np.mean() (trung bình các phần tử)
np.median()  (Trả về giá trị trung vị của mảng arr)
np.max() và np.min() (giá trị lớn nhất và nhỏ nhất)
np.argmax() và np.argmin() (vị trí của giá trị lớn nhất và nhỏ nhất)
np.sort() (sắp xếp mảng)
np.dot() (tích vô hướng hoặc nhân ma trận)
np.rank() (hạng của ma trận)
np.transpose() hoặc .T (chuyển vị ma trận)
np.reshape() (thay đổi dạng ma trận)

Tham số "axis": Tham số axis trong NumPy thường được sử dụng để xác định 
chiều (dimension) trên đó một phép toán được thực hiện. 
Với mảng 2 chiều, axis=0 sẽ áp dụng phép toán theo chiều dọc (theo cột), 
trong khi axis=1 sẽ áp dụng phép toán theo chiều ngang (theo hàng).
import numpy as np

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Tổng theo các cột (axis=0)
sum_col = np.sum(arr_2d, axis=0)
print("Tổng theo cột:")
print(sum_col)

# Tổng theo các hàng (axis=1)
sum_row = np.sum(arr_2d, axis=1)
print("\nTổng theo hàng:")
print(sum_row)

Output:
Tổng theo cột:
[12 15 18]

Tổng theo hàng:
[ 6 15 24]

Link tham khảo: https://numpy.org/devdocs/user/quickstart.html
