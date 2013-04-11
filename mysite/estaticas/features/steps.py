import urllib2
from lxml import html
from nose.tools import assert_equals
from lettuce import world, before, step
from lettuce.django import django_url
from django.test.client import Client

@before.all
def set_client():
    world.browser = Client()

@step(r'I navigate to "(.*)"')
def given_i_navigate_to_group1(step, url):
    url = django_url(url)
    assert_equals(url, 'http://127.0.0.1:8000/pages/hola')

    raw = urllib2.urlopen(url).read()
    world.dom = html.fromstring(raw)

