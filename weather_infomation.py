def main():
    # 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています

    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},

        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},

        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

# """
# Q1. 全国の平均気温は？
# """
    # 東京合計気温 = リストの1つ目 辞書の3つ目 + リストの2つ目 辞書の3つ目 + リストの3つ目 辞書の3つ目
    # total_temperature_infomation = (weather_information[0]["temperature"]) \
    #                                      + (weather_information[1]["temperature"])\
    #                                      + (weather_information[2]["temperature"])\
    #                                      + (weather_information[3]["temperature"])\
    #                                      + (weather_information[4]["temperature"])\
    #                                      + (weather_information[5]["temperature"])\
    #                                      + (weather_information[6]["temperature"])\
    #                                      + (weather_information[7]["temperature"])
    #
    # ave_temperature = total_temperature_infomation / 8
    #
    # print(ave_temperature)

    # 大阪合計気温 =
    # 福岡合計気温 =
    # 合計 =東京合計気温 + 大阪合計気温 + 福岡合計気温
    # len(全部)=東京 + 大阪 + 福岡
    # 平均値を求める式 = (合計) // len(全部)
    # all_ave_temp = 平均値を求める式
    # print(all_ave_temp)

"""
Q2. 大阪府のすべての駅名を出力してね。
"""
# for 文 で大阪府を探して、 station の要素を取り出す。
#     osaka_station1 = weather_information[3]["station"]
#     osaka_station2 = weather_information[4]["station"]
#     osaka_station3 = weather_information[5]["station"]
#
#     print(f"{osaka_station1},{osaka_station2},{osaka_station3}")
for spot_weather_information in weather_information:  # for in データをさらう
    if spot_weather_information["prefecture"] == "大阪府":
        print(spot_weather_information["station"])
    # if weather_information == "prefecture"
    # if 大阪を見つける
    # print 見つけたときは駅名を出力する
# """
# Q3. 福岡県の平均気温は？
# """
#     for fukuoka_weather_information in weather_information

if __name__ == "__main__":
    main()