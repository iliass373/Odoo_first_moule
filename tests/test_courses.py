from odoo.tests.common import TransactionCase
# from odoo.tests.common import Form, SavepointCase
import datetime


class ClassTestCourses(TransactionCase):

    def test_creation_information(self):
        course = self.Course.create({
            'name': 'Course test',
            'description': 'test course',
        })
        self.assertEqual(course.name, 'Course 1')
        self.assertEqual(course.description, 'testcourse')

    def test_domain(self):
        domain_test = self.env['openacademy.course'].create({
            'name': 'Name Course',
            'date_start': '2021-02-01',
            'date_end': '2021-02-05',
        })
        domain = domain_test.get_domain('my_field')
        self.assertEqual(domain, [('date_start', '>=', datetime.date(2020, 2, 1)),
                                  ('date_end', '<=', datetime.date(2020, 2, 5))])
