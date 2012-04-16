from five import grok
from zope import schema
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity

from sa.overview import _

class IOvContent(form.Schema):
    """
    Description of the Example Type
    """
    
    # -*- Your Zope schema definitions here ... -*-

    form.widget(preview="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    preview = schema.Text(
        title=_(u"Preview List Items"),
        description=_(u"Please enter the items you wish to display as a preview in listings optionally formatted as a list."),
        required=False,
    )


    image = namedfile.NamedImage(
        title=_(u"Image"),
        required=True,
    )

    form.widget(maintext="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    maintext = schema.Text(
        title=_(u"Haupttext"),
        required=False,
    )

