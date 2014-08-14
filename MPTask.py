# -*- coding: cp932 -*-
import threading
import time

import OpenRTM_aist




##
#����X���b�h�ł̎��s�����N���X
##
class MPComp:
    def __init__(self):
	self.comp = None
	self.I = 0
	self.J = 0
	self.K = 0

##
#����u���b�N�����s����X���b�h�̃N���X
##
class MPTask(OpenRTM_aist.Task):
    def __init__(self, c):
        OpenRTM_aist.Task.__init__(self)
        self.m_ec = c
        self.m_comp = []
    ##
    #�R���|�[�l���g��ǉ�����֐�
    ##
    def addComp(self, c, I, J, K):
        self.mc = MPComp()
        self.mc.comp = c
        self.mc.I = I
        self.mc.J = J
        self.mc.K = K
        self.m_comp.append(self.mc)
    ##
    #�X���b�h���s�֐�
    ##
    def svc(self):
        if len(self.m_ec.rs) > self.m_ec.r_num:
            for i in range(0, len(self.m_comp)):
                self.m_ec.rs[self.m_ec.r_num].rs[self.m_comp[i].I].SR[self.m_comp[i].J][self.m_comp[i].K].s = 1
		self.m_ec.workerComp(self.m_comp[i].comp)
		self.m_ec.rs[self.m_ec.r_num].rs[self.m_comp[i].I].SR[self.m_comp[i].J][self.m_comp[i].K].s = 0

        return 0








