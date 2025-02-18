import Foundation

class Student {
    var name: String
    var grade: Int
    
    init(name: String, grade: Int) {
        self.name = name
        self.grade = grade
    }
}

let students = [
    Student(name: "Alice", grade: 90),
    Student(name: "Bob", grade: 72),
    Student(name: "Charlie", grade: 85),
    Student(name: "David", grade: 60)
]

let passedStudents = students.filter { $0.grade >= 70 }
let passedNames = passedStudents.map { $0.name }

print("Students who passed: \(passedNames.joined(separator: ", "))")
