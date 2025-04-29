import json

class Student:
    def __init__(self, name, mssv, student_class, phone, birthday, current_address):
        self.name = name
        self.mssv = mssv
        self.student_class = student_class
        self.phone = phone
        self.birthday = birthday
        self.current_address = current_address

    def to_dict(self):
        return {
            "Họ tên": self.name,
            "MSSV": self.mssv,
            "Lớp": self.student_class,
            "SĐT": self.phone,
            "Ngày sinh": self.birthday,
            "Địa chỉ hiện tại": self.current_address
        }

class Family(Student):
    def __init__(self, name, mssv, student_class, phone, birthday, current_address,
                 home_address, father_name, mother_name):
        super().__init__(name, mssv, student_class, phone, birthday, current_address)
        self.home_address = home_address
        self.father_name = father_name
        self.mother_name = mother_name

    def to_dict(self):
        return {
            "Thông tin sinh viên": super().to_dict(),
            "Thông tin gia đình": {
                "Địa chỉ gia đình": self.home_address,
                "Họ tên bố": self.father_name,
                "Họ tên mẹ": self.mother_name
            }
        }

class Manager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def add_student(self, student: Family):
        new_id = len(self.data) + 1
        record = {
            "id": new_id,
            **student.to_dict()
        }
        self.data.append(record)
        self.save_data()

    def update_student(self, student_id, updated_data: Family):
        for i, student in enumerate(self.data):
            if student["id"] == student_id:
                self.data[i] = {
                    "id": student_id,
                    **updated_data.to_dict()
                }
                self.save_data()
                return

    def delete_student(self, student_id):
        self.data = [student for student in self.data if student["id"] != student_id]
        self.save_data()

    def show_all(self):
        for student in self.data:
            print(json.dumps(student, ensure_ascii=False, indent=4))

# Menu CLI
if __name__ == "__main__":
    manager = Manager()

    while True:
        print("\n===== MENU =====")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xóa sinh viên")
        print("4. Hiển thị danh sách")
        print("5. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            name = input("Họ tên: ")
            mssv = input("MSSV: ")
            student_class = input("Lớp: ")
            phone = input("SĐT: ")
            birthday = input("Ngày sinh: ")
            current_address = input("Địa chỉ hiện tại: ")
            home_address = input("Địa chỉ gia đình: ")
            father_name = input("Họ tên bố: ")
            mother_name = input("Họ tên mẹ: ")

            sv = Family(name, mssv, student_class, phone, birthday, current_address,
                        home_address, father_name, mother_name)
            manager.add_student(sv)
            print("✅ Đã thêm!")

        elif choice == "2":
            sid = int(input("Nhập ID sinh viên cần cập nhật: "))
            name = input("Họ tên: ")
            mssv = input("MSSV: ")
            student_class = input("Lớp: ")
            phone = input("SĐT: ")
            birthday = input("Ngày sinh: ")
            current_address = input("Địa chỉ hiện tại: ")
            home_address = input("Địa chỉ gia đình: ")
            father_name = input("Họ tên bố: ")
            mother_name = input("Họ tên mẹ: ")

            new_sv = Family(name, mssv, student_class, phone, birthday, current_address,
                            home_address, father_name, mother_name)
            manager.update_student(sid, new_sv)
            print("✅ Đã cập nhật!")

        elif choice == "3":
            sid = int(input("Nhập ID cần xóa: "))
            manager.delete_student(sid)
            print("🗑️ Đã xóa!")

        elif choice == "4":
            manager.show_all()

        elif choice == "5":
            print("Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")