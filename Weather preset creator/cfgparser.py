#!/usr/bin/python
#-*- coding: utf-8 -*-

#############################
## ACRL partial CFG parser ##
###### For race admins ######
#############################

#You'll need a server_cfg.ini in the root dir
def getcfgDetails():
    details = {}
#    cfg = open('server_cfg.ini','r')
    with open('server_cfg.ini','r') as cfg:
       for line in cfg.readlines():
            details.update({line.split("=")[0].strip():line.split("=")[-1].strip()})
    return details
