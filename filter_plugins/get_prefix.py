#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Cuong Nguyen (cuongnguyen23 at gmail dot com)"


def get_prefix(host, iface):
    ''' Get prefix based on IP of specific interface '''
    bin_str = ''
    netmask = host["ansible_" + iface]["ipv4"]["netmask"]
    for octet in netmask.split('.'):
        bin_str += bin(int(octet))[2:].zfill(8)
    return bin_str.find('0')


def get_ip(host, iface):
    ''' Get desired IP if multiple interfaces.'''
    return host["ansible_" + iface]["ipv4"]["address"]


def get_net(host, iface):
    ''' Return subnet of inteface '''
    return host["ansible_" + iface]["ipv4"]["network"]


class FilterModule(object):
    ''' Custom filter get prefix based on netmask as argument '''

    def filters(self):
        return {
            'get_ip': get_ip,
            'get_prefix': get_prefix,
            'get_net': get_net,
        }
