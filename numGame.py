#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
m=2
y='yes'
n='no'
Rnum=int(random.uniform(100,200))
print Rnum
Putnum=raw_input('please input you nun:')
while int(Putnum)!=Rnum:
    if m<=5:
         print u'输入不正确,您还剩余：',6-m,'次'
         m=m+1
         Putnum=raw_input('please input you nun:')
    else:
        print u'您的次数已经用完'
        print u'输入y继续游戏'
        print u'输入n退出游戏'
        yn=raw_input('please input y or n:')
        if yn==y:
            Nputnum=raw_input('please input you num:')
            if Nputnum!=Rnum:
                 m=2;
            else:
                print u'恭喜'
        elif yn==n:
            break
        else:
            print u'输入不正确，游戏结束'
            break
else:
    print u'恭喜'

    
    

