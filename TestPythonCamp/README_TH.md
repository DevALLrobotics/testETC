# ชุดข้อสอบ Python พื้นฐานด้วย `pytest`

English version: [README.md](README.md)

โฟลเดอร์นี้เป็นชุดข้อสอบ Python พื้นฐานจำนวน 20 ข้อ

ไฟล์ในโฟลเดอร์:
- `student.py`: ไฟล์สรุปโครงสร้าง
- `students/`: ไฟล์ template ของนักเรียน แยกตามข้อ
- `solution.py`: ไฟล์สรุปเฉลย
- `solutions/`: ไฟล์เฉลยแยกตามข้อ
- `check.py`: ไฟล์ตรวจคำตอบแบบอ่านง่าย
- `test.py`: ไฟล์สรุปวิธีรัน
- `tests/`: ไฟล์ `pytest` และไฟล์ช่วยสำหรับเทสต์

รายการข้อสอบ:
1. `add_numbers(a, b)` ให้คืนค่าผลบวกของตัวเลข 2 จำนวน
2. `is_leap_year(year)` ให้ตรวจว่าปีนั้นเป็นปีอธิกสุรทินหรือไม่
3. `sum_even_numbers(numbers)` ให้หาผลรวมของเลขคู่ทั้งหมดในลิสต์
4. `count_vowels(text)` ให้นับจำนวนสระในข้อความ
5. `find_top_student(scores)` ให้คืนชื่อของนักเรียนที่ได้คะแนนสูงสุด
6. `get_grade(score)` ให้คืนเกรดจากคะแนน
7. `reverse_text(text)` ให้คืนข้อความแบบกลับด้าน
8. `count_words(text)` ให้นับจำนวนคำในข้อความ
9. `get_max_number(numbers)` ให้หาค่าสูงสุดในลิสต์
10. `is_palindrome(text)` ให้ตรวจว่าข้อความเป็น palindrome หรือไม่
11. `factorial(n)` ให้หาค่า factorial
12. `average_numbers(numbers)` ให้หาค่าเฉลี่ยของลิสต์ตัวเลข
13. `remove_duplicates(items)` ให้ลบข้อมูลซ้ำโดยคงลำดับเดิม
14. `count_character(text, target)` ให้นับจำนวนตัวอักษรที่ต้องการ
15. `celsius_to_fahrenheit(celsius)` ให้แปลง Celsius เป็น Fahrenheit
16. `filter_positive_numbers(numbers)` ให้เลือกเฉพาะเลขบวก
17. `get_last_element(items)` ให้คืนค่าสุดท้ายของลิสต์
18. `sum_digits(number)` ให้หาผลรวมของเลขแต่ละหลัก
19. `sort_numbers(numbers)` ให้เรียงตัวเลขจากน้อยไปมาก
20. `get_initials(full_name)` ให้คืนอักษรย่อของชื่อ

กติกา:
- ให้แก้เฉพาะไฟล์คำตอบของข้อที่กำลังทำ
- ไม่ต้องแก้ไฟล์ในโฟลเดอร์ `tests/`
- ข้อ 5 ถ้า dictionary ว่าง ให้ `raise ValueError`

วิธีใช้งาน:
1. ติดตั้ง `pytest`
2. เขียนคำตอบลงในไฟล์ template ใต้โฟลเดอร์ `students/`
3. รัน `check.py` เพื่อดูผลแบบอ่านง่าย หรือรัน `pytest`

คำสั่งตรวจแบบอ่านง่าย:
```bash
python3 TestPythonCamp/check.py
python3 TestPythonCamp/check.py 1
python3 TestPythonCamp/check.py 1 2
```

คำสั่งรันทุกข้อ:
```bash
python3 -m pip install pytest
python3 -m pytest TestPythonCamp/tests -q
```

คำสั่งรันแยกเป็นรายข้อ:
```bash
python3 -m pytest TestPythonCamp/tests/test_question_1.py -q
```

ให้เปลี่ยนเลข `1` เป็นหมายเลขข้อที่ต้องการตั้งแต่ `1` ถึง `20`

ไฟล์ที่ต้องแก้ในแต่ละข้อ:
- ข้อ 1: สร้างฟังก์ชัน `add_numbers(a, b)` ใน `students/question_1.py`
- ข้อ 2: สร้างฟังก์ชัน `is_leap_year(year)` ใน `students/question_2.py`
- ข้อ 3: สร้างฟังก์ชัน `sum_even_numbers(numbers)` ใน `students/question_3.py`
- ข้อ 4: สร้างฟังก์ชัน `count_vowels(text)` ใน `students/question_4.py`
- ข้อ 5: สร้างฟังก์ชัน `find_top_student(scores)` ใน `students/question_5.py`
- ข้อ 6: สร้างฟังก์ชัน `get_grade(score)` ใน `students/question_6.py`
- ข้อ 7: สร้างฟังก์ชัน `reverse_text(text)` ใน `students/question_7.py`
- ข้อ 8: สร้างฟังก์ชัน `count_words(text)` ใน `students/question_8.py`
- ข้อ 9: สร้างฟังก์ชัน `get_max_number(numbers)` ใน `students/question_9.py`
- ข้อ 10: สร้างฟังก์ชัน `is_palindrome(text)` ใน `students/question_10.py`
- ข้อ 11: สร้างฟังก์ชัน `factorial(n)` ใน `students/question_11.py`
- ข้อ 12: สร้างฟังก์ชัน `average_numbers(numbers)` ใน `students/question_12.py`
- ข้อ 13: สร้างฟังก์ชัน `remove_duplicates(items)` ใน `students/question_13.py`
- ข้อ 14: สร้างฟังก์ชัน `count_character(text, target)` ใน `students/question_14.py`
- ข้อ 15: สร้างฟังก์ชัน `celsius_to_fahrenheit(celsius)` ใน `students/question_15.py`
- ข้อ 16: สร้างฟังก์ชัน `filter_positive_numbers(numbers)` ใน `students/question_16.py`
- ข้อ 17: สร้างฟังก์ชัน `get_last_element(items)` ใน `students/question_17.py`
- ข้อ 18: สร้างฟังก์ชัน `sum_digits(number)` ใน `students/question_18.py`
- ข้อ 19: สร้างฟังก์ชัน `sort_numbers(numbers)` ใน `students/question_19.py`
- ข้อ 20: สร้างฟังก์ชัน `get_initials(full_name)` ใน `students/question_20.py`

ไฟล์เฉลยจะอยู่ตามรูปแบบ `solutions/question_<number>.py`
