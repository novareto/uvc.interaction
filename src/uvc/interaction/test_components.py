# -*- coding: utf-8 -*-

import pytest
from .components import Participation, Principal
from .context import Interaction
from zope.security.interfaces import IParticipation
from zope.security.management import getInteraction, endInteraction


def users(participations):
    for participation in participations:
        yield participation.principal


def test_participation():
    principal = Principal('someone')
    participation = Participation(principal)
    assert IParticipation.providedBy(participation)


def test_controler():
    principal = Principal('someone')
    with Interaction(principal) as inter:
        policy = getInteraction()
        assert inter is policy
        assert len(policy.participations) == 1
        assert policy.participations[0].principal == principal


def test_nested_interaction():
    anon = Principal('Anonymous')
    john = Principal('John')
    anke = Principal('Anke')
    paul = Principal('Paul')

    with Interaction(anon):
        policy = getInteraction()
        assert list(users(policy.participations)) == [anon]

        with Interaction(john, replace=False):
            policy = getInteraction()
            assert list(users(policy.participations)) == [anon, john]
            
            with Interaction(anke, replace=False):
                policy = getInteraction()
                assert list(users(policy.participations)) == [anon, john, anke]

                with Interaction(paul):
                    policy = getInteraction()
                    assert list(users(policy.participations)) == [paul]

                policy = getInteraction()
                assert list(users(policy.participations)) == [anon, john, anke]

            policy = getInteraction()
            assert list(users(policy.participations)) == [anon, john]

        policy = getInteraction()
        assert list(users(policy.participations)) == [anon]


def test_aborted_interaction():
    anon = Principal('Anonymous')
    john = Principal('John')
    anke = Principal('Anke')
    paul = Principal('Paul')

    with pytest.raises(RuntimeError) as e:
        with Interaction(anon):
            with Interaction(john, replace=False):
                endInteraction()

    assert e.value.message == (
        'Security context has changed during the `Interaction`')
