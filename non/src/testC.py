class Calculator:
    class Operations:
        def add(self, a, b):
            """บวกเลขสองตัว"""
            return a + b

        def subtract(self, a, b):
            """ลบเลขสองตัว"""
            return a - b

        def multiply(self, a, b):
            """คูณเลขสองตัว"""
            return a * b

        def divide(self, a, b):
            """หารเลขสองตัว ถ้าหารด้วย 0 ให้คืนค่า 'Error'"""
            if b == 0:
                return "Error: Division by zero"
            return a / b

    class AdvancedOperations:
        def power(self, a, b):
            """ยกกำลัง a^b"""
            return a ** b

        def average(self, numbers):
            """หาค่าเฉลี่ยของรายการตัวเลข"""
            if not numbers:
                return "Error: Empty list"
            return sum(numbers) / len(numbers)

    def __init__(self):
        self.basic = self.Operations()
        self.advanced = self.AdvancedOperations()
