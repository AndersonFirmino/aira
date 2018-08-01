#!/usr/bin/env python3
# coding: utf-8

from .base import BaseTest

class TestFn(BaseTest):

    def test_empty_args(self):
        '''
        fn1 = fn() do
            return 1
        end

        a = fn1()
        '''
        assert self.vm.frame.hash['a'] == 1

    def test_1_arg(self):
        '''
        fn1 = fn(v) do
            return v + 1
        end

        a = fn1(10)
        '''
        assert self.vm.frame.hash['a'] == 11

    def test_2_args(self):
        '''
        fn1 = fn(a, b) do
            return a + b
        end

        a = fn1(2, 3)
        '''
        assert self.vm.frame.hash['a'] == 5

    def test_3_args(self):
        '''
        fn1 = fn(a, b, c) do
            return a + b + c
        end

        a = fn1(2, 3, 4)
        '''
        assert self.vm.frame.hash['a'] == 9
