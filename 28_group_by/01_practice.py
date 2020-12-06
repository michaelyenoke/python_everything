# group by 按照年分加總 - 劃出柱狀圖  不要看sum看mean ! 拿掉

for key in data:
    clean_group_by_sum[key].plot(kind='bar')
    plt.show()
    

# group by 按照年分加總 - 劃出折線圖
for key in data:
    #clean_group_mean_year[key].plot(kind='bar')
    plt.plot(clean_group_by_sum[key])
    #plt.ylim(1, 3000)
    #plt.xlim(1,3000)
    plt.show()
    
    
# group by 按照年分加總  -  不要看sum看mean ! 拿掉
clean_group_by_sum = clean.groupby(['year']).sum()
clean_group_by_sum.reset_index(inplace=True)
#print(clean_group_by_sum)
clean_group_by_sum.head(10)


# group by 按照 年,月 做加總   不要看sum看mean ! 拿掉
clean_group_by_sum_y_m = clean.groupby(['year','month']).sum()
clean_group_by_sum_y_m.reset_index(inplace=True)
print(clean_group_by_sum_y_m)
#clean_group_by_sum_y_m.head()


# group by year -  算出 mean

clean_group_mean_year = clean.groupby(['year']).mean()
clean_group_mean_year.reset_index(inplace=True)
#print(clean_group_mean_year)
clean_group_mean_year.head(10)
#clean_group_mean.to_csv(path_or_buf='C:/Users/MichaelCHEN/Desktop/csvfile7')


# 計算出 mean , 然後 group by year, month

clean_group_mean_year_month = clean.groupby(['year','month']).mean()
clean_group_mean_year_month.reset_index(inplace=True)
#print(clean_group_mean_year_month)
clean_group_mean_year_month.head(20)


"""
分析筆記 圖形分析:大部分的詞到2020會下降,因為2020年到目前為止才3個月,自然會下降,所以單看年度的話 ,只能看出哪些是今年快速成長的項目,所以diff的計算著重在2020那些是從默默無聞到爆紅,所以問題 在於比去年相對成長多少,可以稱為爆紅?
第一種思考方式:比去年成長-適合比較不同年同月份,有些今年的爆紅字則是會比去年帶來明顯的增長, 可用在新爆紅字
第二種思考方式:組成一籃子熱門關鍵字,接近這個關鍵字的值的詞也可以被視為熱門關鍵字,譬如說'登山車' 雖然比去年下降很多,但是搜尋熱度比近期的'陳時中','梨泰院'都還高
建立不同類別的的一籃子指數來比較不同類別之間的消長:
第一種思考方式 : 總體面的大類別 - 以不同產業為類別觀察彼此間的消長與關聯
第二種思考方式:微觀面的小類別-以運動為範圍,將相關聯運動歸為一類(這當然建立在背後的tag上)
分析筆記_平均數比總數更適合用來觀察趨勢!
分析筆記_針對月份做比較,可以看出每年每個月份的趨勢,比用sum來的有用
"""


