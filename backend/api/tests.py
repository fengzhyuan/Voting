# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Question, Choice
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the Question & Choice model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.question_text = "What's up?"
        self.question = Question(question_text=self.question_text)
        # self.choice1 = Choice(question=self.question, choice_text='Nothing')
        # self.choice2 = Choice(question=self.question.id, choice_text='The sky')
        # self.choice3 = Choice(question=self.question.id, choice_text='Not much')
        
    def test_model_create(self):
        """Test the question/choice model can create a question/choice."""
        oldq = Question.objects.count()
        oldc = Choice.objects.count()
        self.question.save()
        Choice.objects.create(question=self.question, choice_text='Not much')
        Choice.objects.create(question=self.question, choice_text='The sky')
        Choice.objects.create(question=self.question, choice_text='Nothing')
        newq = Question.objects.count()
        newc = Choice.objects.count()
        self.assertNotEqual(oldq, newq)
        self.assertEqual(newq, 1)
        self.assertNotEqual(oldc, newc)
        self.assertEqual(newc, 3)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.question_data = {'question_text': 'How\'s the weather?'}
        self.response = self.client.post(
            reverse('create'),
            self.question_data,
            format="json")

    def test_api_create_question(self):
        """Test the api has question creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_question(self):
        """ Test the aoi can get a given question. """
        question = Question.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': question.id},
            format='json'
        )
        self.assertEqual(response.status_code, status_HTTP_200_OK)
        self.assertContains(resonse, question)
    
    def test_api_update_question(self):
        """ Test the api can update a given question. """
        chg_question = {'question_text': 'Are you hungery?'}
        res = self.client.put(
            reverse('details', kwargs={'pk': question.id}),
            chg_question, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_delete_question(self):
        """ Test the api can delete a question. """
        question = Question.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': question.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
