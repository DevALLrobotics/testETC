import hashlib
import itertools
import multiprocessing

def candidate_generator(charset, length):
    """
    สร้าง generator สำหรับ candidate จาก charset โดยให้ candidate มีความยาวเท่ากับ length
    """
    return (''.join(candidate) for candidate in itertools.product(charset, repeat=length))

def check_candidate(args):
    """
    ตรวจสอบว่า candidate เมื่อเข้ารหัส MD5 ตรงกับ target_hash หรือไม่
    :param args: tuple (candidate, target_hash)
    :return: candidate ถ้าตรงกัน มิฉะนั้นคืนค่า None
    """
    candidate, target_hash = args
    hashed_candidate = hashlib.md5(candidate.encode()).hexdigest()
    if hashed_candidate == target_hash:
        return candidate
    return None

def brute_force_alphanumeric(target_hash, charset, length):
    """
    ค้นหา candidate ที่ MD5 ตรงกับ target_hash โดยใช้ multiprocessing พร้อมแสดงผลความคืบหน้า
    :param target_hash: ค่า MD5 ที่ต้องการหา
    :param charset: ชุดอักขระที่ใช้สร้าง candidate
    :param length: ความยาวของ candidate
    :return: candidate ที่พบหรือ None
    """
    pool = multiprocessing.Pool()
    found_password = None
    processed_count = 0
    try:
        candidate_iter = candidate_generator(charset, length)
        # จับคู่ candidate กับ target_hash ใน tuple
        candidate_args = ((candidate, target_hash) for candidate in candidate_iter)
        
        # ใช้ imap_unordered เพื่อประมวลผล candidate แบบขนาน
        for result in pool.imap_unordered(check_candidate, candidate_args, chunksize=1000):
            processed_count += 1            
            print(f"Processed {processed_count} candidates...")
            if result is not None:
                found_password = result
                pool.terminate()  # ยกเลิก process อื่น ๆ เมื่อพบ candidate ที่ตรงกัน
                break
    finally:
        pool.close()
        pool.join()
    return found_password

if __name__ == "__main__":
    
    target_hash = "db2351a4c8edc8f24400bdc1a52cd442"  # ตรวจสอบให้แน่ใจว่าค่านี้ถูกต้องสำหรับ "Ab1!"
    
    # กำหนด charset ที่มีทั้งตัวเลข, ตัวอักษรพิมพ์เล็ก, พิมพ์ใหญ่ และสัญลักษณ์พิเศษ
    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    length = 4  # เพิ่มความยาว candidate เป็น 4 ตัว
    
    print("กำลังค้นหา candidate ที่มีความยาว 4 ตัวอักษรจาก charset ที่ซับซ้อน...")
    password = brute_force_alphanumeric(target_hash, charset, length)
    
    if password:
        print(f"✅ Password found: {password}")
    else:
        print("❌ Password not found within the given range.")


