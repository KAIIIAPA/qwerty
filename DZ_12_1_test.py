import unittest
from DZ_12_1 import Student


class MyStudentTest(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student(name='Ivan')
        self.student_2 = Student(name='Pavel')

    def test_walk(self):
        for i in range(1, 11):
            self.student_1.walk()
        self.assertEqual(first=self.student_1.distance,
                         second=50,
                         msg=f'Дистанции не равны {self.student_1.distance} != 50')

    def test_run(self):
        for i in range(1, 11):
            self.student_2.run()
        self.assertEqual(first=self.student_2.distance,
                         second=100,
                         msg=f'Дистанции не равны {self.student_2.distance} != 100')

    def test_three(self):
        for i in range(1,11):
            self.student_1.walk()
            self.student_2.run()
        self.assertLess(a=self.student_1.distance,
                        b=self.student_2.distance,
                        msg=f'{self.student_2.name} должен преодолеть дистанцию больше, чем {self.student_1.name})')


if __name__ == '__main__':
    unittest.main()
