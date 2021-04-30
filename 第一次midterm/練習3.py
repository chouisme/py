Zodiac_list=["鼠(Rat)","牛(ox)","虎(Tiger)","兔(Rabbit)","龍(Dragon)","蛇(Snake)","馬(Horse)","羊(Sheep)","猴(Monkey)","雞(Rooster)","狗(Dog)","豬(Pig)"]
ad = int(input("請輸入西元年"))
if ad >=2008:
    ad_check =(ad-2008)%12
    print(Zodiac_list[ad_check])
else:
    ad_check =-(2008-ad)%12
    print(Zodiac_list[ad_check])