from collections import Counter
from django.test import TestCase
from .models import *
from django.urls import reverse


class ViewsTest(TestCase):
    def setUp(self):
       Game.objects.create(title='gametitle', descr='gamedescr')
       Game.objects.create(title='gametitle1', descr='gamedescr1')
       Game.objects.create(title='gametitle2', descr='gamedescr2')

    def testGamesView(self):
        status = self.client.get(reverse('index')).status_code
        self.assertEqual(status, 200)
        self.assertTemplateUsed('kulichtv/index.html')

    def testCommunitiesView(self):
        status = self.client.get(reverse('index')).status_code
        self.assertEqual(status, 200)
        self.assertTemplateUsed('kulichtv/communities.html')

    def testGameAdd(self):
        gameobj = Game.objects.get(title='gametitle')
        self.assertIsNone(gameobj.pic._file)

    def testGamesCount(self):
        count = Game.objects.all().count()
        self.assertEqual(count, 3)
