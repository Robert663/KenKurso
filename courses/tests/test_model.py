from django.test import TestCase
from ..models import Course

class CoursesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Test course",
        cls.description = "Test description",
        cls.duration = 1000
        cls.course = Course.objects.create(
            name=cls.name,
            description=cls.description,
            duration=cls.duration,
        )
    
    def test_courses_info_fields(self):
        self.assertEqual(self.course.name, self.name)
        self.assertEqual(self.course.description, self.description)
        self.assertEqual(self.course.duration, self.duration)
        self.assertEqual(self.course.inscriptions, 0)
        
    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length, 127)