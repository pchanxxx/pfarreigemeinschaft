from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent

from sa.overview.content.overview import IOverview
from sa.overview.content.ovcontent import IOvContent

class View(grok.View):
    grok.context(IOverview)
    grok.require('zope2.View')
    grok.name('view')
    
    def has_ovcontent(self):
        return len(self.contained_ovcontent()) > 0
    
    def contained_ovcontent(self):
        """ Return a list of contained content in order to construct. """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IOvContent.__identifier__,
                          path='/'.join(context.getPhysicalPath()),
                          review_state='published',
                          sort_on='getObjPositionInParent')
        return results
