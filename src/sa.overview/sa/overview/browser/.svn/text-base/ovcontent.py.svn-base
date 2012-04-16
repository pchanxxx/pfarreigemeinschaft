
from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from sa.overview.content.ovcontent import IOvContent

class View(grok.View):
    grok.context(IOvContent)
    grok.require('zope2.View')
    grok.name('view')
