def newsTweet():
    import tweepy
    import json
    import pymongo

    # Twitter API Keys
    from Config import (consumer_key,
                        consumer_secret,
                        access_token,
                        access_token_secret)

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Connecting to news databse

    myclient = pymongo.MongoClient(
        "mongodb+srv://nswehli:900941196@lynews-7ygvg.mongodb.net/LyNews?retryWrites=true&w=majority")
    mydb = myclient["LyNews"]
    mycol = mydb["News"]

    postedTweets = []

    x = mycol.find_one()

    sortedNews = mycol.find().sort("_id", -1).limit(1)

    for x in sortedNews:
        # AlHadeth
        for item in x["AlHadeth"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة ليبيا الحدث : {headline} \n {link}"
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue

        # BBC Arabic
        for item in x["BBCArabic"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"بي بي سي العربية : {headline} \n {link}"
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
                else:
                    print("Already posted")
            except:
                continue

        #  AlJazeera
        for item in x["AlJazeera"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"الجزيرة نت: : {headline} \n {link}"
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # AlMarsad
        for item in x["AlMarsad"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"صحيفة المرصد : {headline} \n {link}"
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # AlRaed
        for item in x["AlRaed"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"شبكة الرائد : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue

        for item in x["Alsaaa24"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"صحيفة الساعة 24 : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # Bawaba Africa
        for item in x["BawabaAfrica"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"بوابة أفريقيا الإخبارية : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # Ein Libya
        for item in x["EinLibya"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"عين ليبيا  : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # France24
        for item in x["France24"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"France24 : {headline} \n #Libya \n {link} \n"
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # Jamahrya
        for item in x["Jamahrya"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة الجماهيرية العظمى : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # Libya218
        for item in x["Libya218"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة 218: {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # Libya24
        for item in x["Libya24News"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة ليبيا 24 : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue
        # libyaAhrar
        for item in x["LibyaAhrar"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة ليبيا الأحرار : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue

        # LyPanoroma
        for item in x["LyPanoroma"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة ليبيا بانوراما : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue

        # LyWatan
        for item in x["LyWatan"]:
            try:
                headline = (item["Headline"])
                link = (item["Link"])
                tweet = f"قناة ليبيا – روحها الوطن: : {headline} \n #Libya \n {link} "
                if tweet not in postedTweets:
                    api.update_status(tweet)
                    postedTweets.append(tweet)
                    print(f" This was tweeted {tweet}")
            except:
                continue

        # RussiaToday
        for x in sortedNews:
            for item in x["RussiaToday"]:
                try:
                    headline = (item["Headline"])
                    link = (item["Link"])
                    tweet = f"روسيا اليوم : {headline} \n #Libya \n {link} "
                    if tweet not in postedTweets:
                        api.update_status(tweet)
                        postedTweets.append(tweet)
                        print(f" This was tweeted {tweet}")
                except:
                    continue

newsTweet()
