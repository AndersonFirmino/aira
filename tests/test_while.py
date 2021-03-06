#!/usr/bin/env python3
# coding: utf-8

from .base import BaseTest

class TestWhile(BaseTest):

    def test_base(self):
        '''
        a = 0
        sum = 0

        while a < 5 do
            a += 1
            sum += 1
        end
        '''
        assert self.vm.frame.hash['sum'] == 5

    def test_break(self):
        '''
        a = 0
        sum = 0

        while a < 5 do
            a += 1
            sum += 1
            break
        end
        '''
        assert self.vm.frame.hash['sum'] == 1

    def test_if_break(self):
        '''
        a = 0
        sum = 0

        while a < 5 do
            a += 1
            sum += 1

            if a == 2 do
                break
            end
        end
        '''
        assert self.vm.frame.hash['sum'] == 2

    def test_continue(self):
        '''
        a = 0
        sum = 0

        while a < 5 do
            a += 1
            continue
            sum += 1
        end
        '''
        assert self.vm.frame.hash['sum'] == 0

    def test_if_continue(self):
        '''
        a = 0
        sum = 0

        while a < 5 do
            a += 1

            if a > 2 do
                continue
            end

            sum += 1
        end
        '''
        assert self.vm.frame.hash['sum'] == 2
