# ชุดข้อสอบ Python พื้นฐานด้วย `pytest`

English version: [README.md](README.md)

โฟลเดอร์นี้เป็นชุดข้อสอบ Python พื้นฐานจำนวน 7 ข้อ

ไฟล์ในโฟลเดอร์:
- `student.py`: ไฟล์สรุปโครงสร้าง
- `students/`: ไฟล์ template ของนักเรียน แยกตามข้อ
- `solution.py`: ไฟล์สรุปเฉลย
- `solutions/`: ไฟล์เฉลยแยกตามข้อ
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

กติกา:
- ให้แก้เฉพาะไฟล์คำตอบของข้อที่กำลังทำ
- ไม่ต้องแก้ไฟล์ในโฟลเดอร์ `tests/`
- ข้อ 5 ถ้า dictionary ว่าง ให้ `raise ValueError`

วิธีใช้งาน:
1. ติดตั้ง `pytest`
2. เขียนคำตอบลงในไฟล์ template ใต้โฟลเดอร์ `students/`
3. รันเทสต์เพื่อตรวจคำตอบ

คำสั่งรันทุกข้อ:
```bash
python3 -m pip install pytest
python3 -m pytest TestPythonCamp/tests -q
```

คำสั่งรันแยกเป็นรายข้อ:
```bash
python3 -m pytest TestPythonCamp/tests/test_question_1.py -q
python3 -m pytest TestPythonCamp/tests/test_question_2.py -q
python3 -m pytest TestPythonCamp/tests/test_question_3.py -q
python3 -m pytest TestPythonCamp/tests/test_question_4.py -q
python3 -m pytest TestPythonCamp/tests/test_question_5.py -q
python3 -m pytest TestPythonCamp/tests/test_question_6.py -q
python3 -m pytest TestPythonCamp/tests/test_question_7.py -q
```

ไฟล์ที่ต้องแก้ในแต่ละข้อ:
- ข้อ 1: สร้างฟังก์ชัน `add_numbers(a, b)` ใน `students/question_1.py`
- ข้อ 2: สร้างฟังก์ชัน `is_leap_year(year)` ใน `students/question_2.py`
- ข้อ 3: สร้างฟังก์ชัน `sum_even_numbers(numbers)` ใน `students/question_3.py`
- ข้อ 4: สร้างฟังก์ชัน `count_vowels(text)` ใน `students/question_4.py`
- ข้อ 5: สร้างฟังก์ชัน `find_top_student(scores)` ใน `students/question_5.py`
- ข้อ 6: สร้างฟังก์ชัน `get_grade(score)` ใน `students/question_6.py`
- ข้อ 7: สร้างฟังก์ชัน `reverse_text(text)` ใน `students/question_7.py`

ไฟล์เฉลย:
- ข้อ 1: `solutions/question_1.py`
- ข้อ 2: `solutions/question_2.py`
- ข้อ 3: `solutions/question_3.py`
- ข้อ 4: `solutions/question_4.py`
- ข้อ 5: `solutions/question_5.py`
- ข้อ 6: `solutions/question_6.py`
- ข้อ 7: `solutions/question_7.py`
