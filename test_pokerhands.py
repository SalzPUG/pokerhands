#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from pokerhands import pokerhands

def test_pokerhands():
    assert_equals(pokerhands(
        ('C2', 'C3', 'C4', 'C5', 'S7'),
        ('S2', 'S3', 'S4', 'S5', 'H8')
    ), -1)
    
def test_ace():
    assert_equals(pokerhands(
        ('C2', 'C3', 'C4', 'C5', 'SA'),
        ('S2', 'S3', 'S4', 'S5', 'HK')
    ), 1)

def test_pair():
    assert_equals(pokerhands(
        ('C2', 'C3', 'C4', 'C5', 'D5'),
        ('S2', 'S3', 'S4', 'S8', 'H8')
    ), -1)
    
def test_three_of_a_kind():
    assert_equals(pokerhands(
        ('C2', 'C3', 'S5', 'C5', 'D5'),
        ('S2', 'S3', 'S4', 'S8', 'H8')
    ), 1)
    
def test_three_of_a_kind2():
    assert_equals(pokerhands(
        ('C2', 'C3', 'S5', 'C5', 'D5'),
        ('S2', 'C4', 'S4', 'S8', 'H8')
    ), 1)

def test_fours():
    assert_equals(pokerhands(
        ('C2', 'H5', 'S5', 'C5', 'D5'),
        ('C4', 'C7', 'S4', 'S8', 'H8')
    ), 1)

def test_fours2():
    assert_equals(pokerhands(
        ('C2', 'H5', 'S5', 'C5', 'D5'),
        ('C4', 'C8', 'S4', 'S8', 'H8')
    ), 1)

def test_full_house():
    assert_equals(pokerhands(
        ('C2', 'H5', 'S5', 'C5', 'D5'),
        ('C4', 'C8', 'S4', 'S8', 'H8')
    ), 1)
    
def test_full_house2():
    assert_equals(pokerhands(
        ('C2', 'H2', 'S5', 'C5', 'D5'),
        ('C4', 'C8', 'S3', 'S8', 'H8')
    ), 1)

