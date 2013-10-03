# -*- coding: utf-8 -*-
"""A basic zope security components implementation.
It copies what exists in zope.security.testing.
"""
    
from zope.interface import implementer
from zope.security.interfaces import IParticipation, IPrincipal
from zope.security.interfaces import 


@implementer(IParticipation)
class Participation(object):

    def __init__(self, principal):
        self.principal = principal
        self.interaction = None


@implementer(IPrincipal)
class Principal(object):

    def __init__(self, id, title=u'', description=u''):
        self.id = id
        self.title = title
        self.description = description
