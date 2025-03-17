import hashlib
import multiprocessing

def check_candidate(args):
    """
    ฟังก์ชันสำหรับตรวจสอบว่า candidate ที่ส่งเข้ามาตรงกับ target hash หรือไม่
    :param args: tuple ที่ประกอบด้วย (i, target_hash, num_digits)
    :return: candidate (เป็น string) ถ้าตรงกัน มิฉะนั้นจะ return None
    """
    i, target_hash, num_digits = args
    # แปลงตัวเลขให้เป็น string ที่มีจำนวนหลักตามที่กำหนด (เติมเลข 0 ข้างหน้า)
    attempt = str(i).zfill(num_digits)
    # คำนวณ MD5 ของ attempt นั้น
    hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
    
    if hashed_attempt == target_hash:
        return attempt  # พบ candidate ที่ถูกต้อง
    return None

def brute_force_password_parallel(target_hash, num_digits=4):
    """
    ฟังก์ชันสำหรับค้นหาค่า candidate ที่เข้ารหัส MD5 ตรงกับ target_hash โดยใช้ multiprocessing
    :param target_hash: ค่า MD5 ที่ต้องการค้นหา
    :param num_digits: จำนวนหลักของ candidate (default: 4)
    :return: รหัสผ่านที่พบ หรือ None ถ้าไม่พบ
    """
    max_attempts = 10 ** num_digits  # สำหรับ 4 หลัก คือ 0000 ถึง 9999

    # เตรียมข้อมูลสำหรับส่งให้แต่ละ process ในรูปแบบ tuple
    args_list = [(i, target_hash, num_digits) for i in range(max_attempts)]

    # สร้าง Pool ของ process (จำนวน process จะเท่ากับจำนวน CPU cores โดยอัตโนมัติ)
    pool = multiprocessing.Pool()

    found_password = None
    try:
        # ใช้ imap_unordered เพื่อประมวลผล candidate แบบขนาน
        for result in pool.imap_unordered(check_candidate, args_list, chunksize=100):
            if result is not None:
                found_password = result
                # พบ candidate ที่ตรงกันแล้ว ให้ยกเลิก process อื่น ๆ
                pool.terminate()
                break
    finally:
        pool.close()
        pool.join()

    return found_password

if __name__ == "__main__":
    # สมมุติว่าเราต้องการค้นหาค่า MD5 ของ "123456" ซึ่งเป็นตัวเลข 6 หลัก
    # คุณสามารถคำนวณ MD5 ของ "123456" แล้วนำค่ามาใช้ใน target_hash ได้
    target_hash = "e10adc3949ba59abbe56e057f20f883e"  # MD5 ของ "123456"
    password = brute_force_password_parallel(target_hash, num_digits=6)

    if password:
        print(f"✅ Password found: {password}")
    else:
        print("❌ Password not found within the given range.")
