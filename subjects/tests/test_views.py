from rest_framework.test import APITestCase

from ..serializers import SubjectSerializers
from ..models import Subject
class SubjectModelTest(APITestCase):

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
        cls.subject_2 = Subject.objects.create(
            name = cls.name,
            description = cls.description,
            duration = cls.duration,
        )
        cls.subjects = [Subject.objects.create(
            name = cls.name,
            description = cls.description,
            duration = cls.duration,
        ) for _ in range(10)]

    def test_update_subject(self):
        subject = self.subject
        response = self.client.post(f'/api/subjects/{subject.id}',{'name':"Test subject update"}, follow='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_subject(self):
        subject = self.subject_2
        response = self.client.delete(f'/api/subjects/{subject.id}/')
        self.assertEqual(response.status_code, 204)

    def test_list_all_subjects(self):
        response = self.client.get('/api/subjects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.subjects)+2, len(response.data))
    
        for subject in self.subjects:
            self.assertIn(
                SubjectSerializers(instance=subject).data,response.data
            )
    
    def test_list_subject_by_id(self):
        subject = self.subject
        response = self.client.get(f'/api/subjects/{subject.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.subject.id)
        self.assertEqual(
           SubjectSerializers(instance=subject).data, response.data
        )
      

