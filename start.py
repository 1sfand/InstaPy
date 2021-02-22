from instapy import InstaPy

friends_list = ['enter_here_what_u_want']

accounts = ["usr1", "usr2", "usr3"]
passwords = ["psw1", "psw2", "psw3"]

for account_number in range(len(accounts)):
    #login proccess
    rabota = InstaPy(username=accounts[account_number], password=passwords[account_number], headless_browser=True)
    rabota.login()

    #quotes

    rabota.set_quota_supervisor(enabled=True, peak_comments_daily=1000, peak_comments_hourly=50, peak_likes_hourly=50, )
    rabota.set_relationship_bounds(enabled=True, max_followers=150)

    #whole proccess    

    rabota.like_by_users(friends_list, amount= depends on u)
    
    #if u want u can enable follows and comments by removing '#'    

    #rabota.like_by_tags(['линукс', 'информационнаябезопасность', 'программирование']) 
    #rabota.set_do_follow(True, percentage=100)
    #rabota.set_do_comment(True, percentage=100)
    #rabota.set_comments(["класссс", 'Давно таких публикаций не было!!', 'Годный контент!'])

    rabota.end()
