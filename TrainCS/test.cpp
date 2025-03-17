#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <thread>
#include <vector>
#include <atomic>
#include <mutex>
#include <openssl/md5.h>

using namespace std;

// ฟังก์ชันคำนวณ MD5 โดยใช้ OpenSSL
string md5(const string &input) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5(reinterpret_cast<const unsigned char*>(input.c_str()), input.size(), digest);
    
    // แปลงผลลัพธ์เป็น hex string
    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        ss << hex << setw(2) << setfill('0') << static_cast<int>(digest[i]);
    }
    return ss.str();
}

// ฟังก์ชันแปลง index เป็น candidate string ในระบบเลขฐาน (base = ขนาด charset)
string indexToCandidate(unsigned long long index, const string &charset, int length) {
    int base = charset.size();
    string candidate(length, charset[0]);
    for (int pos = length - 1; pos >= 0; pos--) {
        candidate[pos] = charset[index % base];
        index /= base;
    }
    return candidate;
}

// ตัวแปรสำหรับควบคุมการหยุดเมื่อพบ candidate ที่ตรงกัน
atomic<bool> foundFlag(false);
mutex resultMutex;
string foundCandidate;

// Worker function สำหรับแต่ละ thread
void worker(unsigned long long start, unsigned long long end, 
            const string &targetHash, const string &charset, int length) {
    for (unsigned long long i = start; i < end && !foundFlag.load(); i++) {
        string candidate = indexToCandidate(i, charset, length);
        if (md5(candidate) == targetHash) {
            // ค้นพบ candidate ที่ตรงกัน
            lock_guard<mutex> lock(resultMutex);
            foundCandidate = candidate;
            foundFlag.store(true);
            return;
        }
    }
}

int main() {
    // กำหนด target hash (MD5 ของ "Ab1!")
    string targetHash = "e5f6c1977e8c84d9d5e66cfb79c5f144";
    // กำหนด charset: รวมตัวเลข, ตัวอักษรพิมพ์เล็ก-พิมพ์ใหญ่ และสัญลักษณ์พิเศษ
    string charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()";
    int length = 4;  // ความยาว candidate

    // คำนวณจำนวน candidate ทั้งหมด = (size(charset))^length
    unsigned long long total = 1;
    for (int i = 0; i < length; i++) {
        total *= charset.size();
    }

    // กำหนดจำนวน thread จาก hardware_concurrency
    int numThreads = thread::hardware_concurrency();
    if (numThreads == 0) {
        numThreads = 4;  // กำหนดค่าเริ่มต้นหากไม่สามารถตรวจสอบได้
    }
    vector<thread> threads;
    unsigned long long chunk = total / numThreads;

    cout << "Starting brute-force with " << numThreads 
         << " threads, total candidates: " << total << endl;

    // สร้างและเริ่ม thread โดยแบ่งช่วงของ index ที่จะค้นหา
    for (int i = 0; i < numThreads; i++) {
        unsigned long long start = i * chunk;
        unsigned long long end = (i == numThreads - 1) ? total : start + chunk;
        threads.push_back(thread(worker, start, end, targetHash, charset, length));
    }

    // รอให้ thread ทุกตัวทำงานเสร็จ
    for (auto &t : threads) {
        t.join();
    }

    if (foundFlag.load()) {
        cout << "✅ Password found: " << foundCandidate << endl;
    } else {
        cout << "❌ Password not found within the given range." << endl;
    }

    return 0;
}
