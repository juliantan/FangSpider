#_*_coding:utf8_*_

import pymongo
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

client = pymongo.MongoClient('192.168.1.69',27017)
fangdb = client['fangdb']
newfanginfo = fangdb['newfanginfo(20170915_2)']
df = pd.DataFrame(list(newfanginfo.find()))

df1 = df.loc[:,['EstateArea','RefPrice','AvePrice','HuXing']]
df1est = df1['EstateArea']
df1ref = df1['RefPrice'].replace('/','0').astype('float')
df1ave = df1['AvePrice'].replace('/','0').astype('float')
df1hx = df1['HuXing'].replace('/','0').astype('int')
df1ave = df1ref*10000/df1hx
print df1ave
dic = {'EstateArea':df1est,'RefPrice':df1ref,'AvePrice':df1ave,'HuXing':df1hx}
newdf = pd.DataFrame(dic) #均价由总价/建面的结果
# newdf.to_excel('newdf.xls')
# print newdf

EstateAreas = [u'北京',u'上海',u'广州',u'深圳',u'杭州',u'天津',u'东莞',u'佛山',u'中山',u'惠州']
means = []
for EstateArea in EstateAreas:
    ave = newdf[newdf['EstateArea'].isin([EstateArea])]['AvePrice']
    ave = ave.order(na_last=True, ascending=True, kind='mergesort') #按升序排列
    ave = pd.Series(list(ave),index=list(np.arange(len(ave))))
    print ave
    means.append(ave.mean())    
#     print '\n\n\n'
    print u'{0}楼盘最低价:{1}元\n\t最高价:{2}元'.format(EstateArea,ave.min(),ave.max())

dfresult = pd.DataFrame(means,index=list(EstateAreas))

index = np.arange(dfresult[0].size)
plt.bar(index,dfresult[0],0.75,color='G')
plt.xticks(index+0.37,dfresult.index)
plt.title(u'楼盘均价')
plt.xlabel(u"地区")
plt.ylabel(u"均价")
plt.show()






