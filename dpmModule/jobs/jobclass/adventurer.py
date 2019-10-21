from ...kernel import core
from ...kernel.core import VSkillModifier as V
from ...character import characterKernel as ck
# 모험가 공용 5차스킬 통합코드
'''
class MapleHero2:
    #vEhc.getV(var1,var2)
    def __init__(self, vEhc):
        return
    def mapleHero2(var1, var2):
        return core.BuffSkill("메이플월드 여신의 축복")
'''
# 모험가 법사
# 3% 증가로 알고있는데... 확인필요
# TODO : 재사용 대기시간 초기화 미적용으로 변경
class InfinityWrapper(core.BuffSkillWrapper):
    def __init__(self, serverlag = 3):
        skill = core.BuffSkill("인피니티", 960, 40000, cooltime = 180 * 1000, rem = True, red = True)
        super(InfinityWrapper, self).__init__(skill)
        self.passedTime = 0
        self.serverlag = serverlag
        
    def spend_time(self, time):
        if self.onoff:
            self.passedTime += time
        super(InfinityWrapper, self).spend_time(time)
            
    def get_modifier(self):
        if self.onoff:
            return core.CharacterModifier(pdamage_indep = (70 + 4 * (self.passedTime // ((4+self.serverlag)*1000))) )
        else:
            return core.CharacterModifier()
        
    def _use(self, rem = 0, red = 0):
        self.passedTime = 0
        return super(InfinityWrapper, self)._use(rem = rem, red = red)