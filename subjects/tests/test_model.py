from django.test import TestCase

from users.models import User
from ..models import Subject
from teachers.models import Teacher

class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "Test subject",
        cls.description = "Test description",
        cls.duration = "2000"
        cls.subject = Subject.objects.create(
            name = cls.name,
            description = cls.description,
            duration = cls.duration,
        )
      
    def test_description_constraint(self):
        subject = Subject.objects.get(id=1)
        null = subject._meta.get_field('description').null
        self.assertEquals(null,False)

    def test_subject_fields(self):
        self.assertIsNone(self.subject.teacher)
        self.assertEqual(self.subject.name,self.name)
        self.assertEqual(self.subject.description,self.description)
        self.assertEqual(self.subject.duration,self.duration)
        self.assertTrue(self.subject.created_at)
        self.assertTrue(self.subject.updated_at)
    
    