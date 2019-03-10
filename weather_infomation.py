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

    # Q1. 全国の平均気温は？

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

    # Q2. 大阪府のすべての駅名を出力してね。

    # Q3. 福岡県の平均気温は？
    # temp6 = weather_information[6]["temperature"]
    # temp7 = weather_information[7]["temperature"]
    # fukuoka_total = temp6 + temp7
    #     print(fukuoka_total / 2)

    fukuoka_total_count = 0

    for weather in weather_information:
        if weather["prefecture"] == "福岡県":
            fukuoka_total_temperautre += weather["temperature"]
            fukuoka_total_count += 1
            print(fukuoka_total_count)

    # fukuoka_total_temperautre = "福岡県"
    # for fukuoka_info in "temperature"


if __name__ == "__main__":
    main()
