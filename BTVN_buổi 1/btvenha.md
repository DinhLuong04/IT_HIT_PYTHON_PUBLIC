### Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

Python là ngôn ngữ thông dịch. Điều này có nghĩa là mã nguồn Python được thực thi trực tiếp từng dòng bởi một chương trình thông dịch (interpreter) mà không cần phải biên dịch trước thành mã máy (machine code). Quá trình này khác với các ngôn ngữ biên dịch như C hoặc C++, nơi mã nguồn phải được biên dịch trước thành mã máy trước khi thực thi.

Lý do Python được coi là ngôn ngữ thông dịch bao gồm:
- **Thực thi trực tiếp**: Mã Python được thực thi trực tiếp bởi trình thông dịch mà không cần giai đoạn biên dịch trước.
- **Tính tương tác**: Python hỗ trợ chế độ tương tác (interactive mode) giúp lập trình viên có thể viết và thực thi mã ngay lập tức.
- **Linh hoạt và dễ dàng thử nghiệm**: Việc thực thi mã trực tiếp giúp lập trình viên dễ dàng thử nghiệm và gỡ lỗi mã nguồn.

### Bài 2: Tìm hiểu trước kiến thức buổi 2

#### Các kiểu dữ liệu trong Python
1. **Số (Numbers)**:
   - `int`: Số nguyên (e.g., 1, -3, 42)
   - `float`: Số thực (e.g., 3.14, -0.001, 2.0)
   - `complex`: Số phức (e.g., 1+2j, -3j)
2. **Chuỗi (String)**: Đại diện cho dãy ký tự (e.g., "Hello", 'Python')
3. **Danh sách (List)**: Danh sách các phần tử có thể thay đổi được (e.g., [1, 2, 3], ['apple', 'banana'])
4. **Tuple**: Danh sách các phần tử không thể thay đổi (e.g., (1, 2, 3), ('a', 'b', 'c'))
5. **Từ điển (Dictionary)**: Cặp key-value (e.g., {'name': 'John', 'age': 25})
6. **Set**: Tập hợp các phần tử không trùng lặp (e.g., {1, 2, 3})
7. **Boolean**: Chỉ có hai giá trị là True và False.

#### Các toán tử trong Python
1. **Toán tử số học**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
2. **Toán tử so sánh**: `==`, `!=`, `>`, `<`, `>=`, `<=`
3. **Toán tử logic**: `and`, `or`, `not`
4. **Toán tử gán**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`
5. **Toán tử bit**: `&`, `|`, `^`, `~`, `<<`, `>>`

#### Mệnh đề điều kiện và vòng lặp
1. **Mệnh đề điều kiện (if-elif-else)**:
   ```python
   if điều_kiện:
       thực_thi_khối_lệnh
   elif điều_kiện_khác:
       thực_thi_khối_lệnh_khác
   else:
       thực_thi_khối_lệnh_cuối
   ```
2. **Vòng lặp**:
   - **for**:
     ```python
     for biến in dãy:
         thực_thi_khối_lệnh
     ```
   - **while**:
     ```python
     while điều_kiện:
         thực_thi_khối_lệnh
     ```

#### Kiểu dữ liệu True, False
- **Boolean**: Kiểu dữ liệu chỉ có hai giá trị là `True` và `False`. Trong Python, các giá trị này được sử dụng trong các mệnh đề điều kiện và toán tử logic.
  ```python
  is_active = True
  has_permission = False
  if is_active and has_permission:
      print("Access granted")
  else:
      print("Access denied")
  ```