None
meme_dict = {
            "Фул": "просьба показать что-либо до конца или в полной форме",
            "Лол": "Что-то очень смешное",
            "Хайп": "Шумиха, ажиотаж"
            }

word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    # Что делать, если слово нашлось?
    print(meme_dict[world])
else:
    # Что делать, если слово не нашлось?
    print("Минус вайб")
