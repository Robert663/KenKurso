from rest_framework.test import APITestCase
from ..models import Course
from ..serializers import CourseSerializer


class CoursesViewsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Test course",
        cls.description = "Test description",
        cls.duration = 1800


        cls.unique_course = Course.objects.create(
            name=cls.name,
            description=cls.description,
            duration=cls.duration,
        )

        cls.courses = [Course.objects.create(
            name=cls.name,
            description=cls.description,
            duration=cls.duration,
        ) for _ in range(10)]

    def test_list_all_classes(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.courses)+1, len(response.data))
    
        for course in self.courses:
            self.assertIn(
                CourseSerializer(instance=course).data,response.data
            )
    
    def test_list_course_by_id(self):
        course = self.unique_course
        response = self.client.get(f'/api/courses/{course.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.unique_course.id)
        self.assertEqual(
            CourseSerializer(instance=course).data, response.data
        )