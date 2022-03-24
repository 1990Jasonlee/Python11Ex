import unittest

from gradebook import Person


class TestGradeBook(unittest.TestCase):
    def test_person_update_first_name(self):
        people = Person('a', 'b', '1/1/1')
        people.update_first_name('adam')
        expected = 'adam'
        self.assertEqual(people.first_name, expected)

    def test_update_last_name(self):
        people = Person('a', 'b', '1/1/1')
        people.update_last_name('boy')
        expected = 'boy'
        self.assertEqual(people.last_name, expected)


if __name__ == '__main__':
    unittest.main()
