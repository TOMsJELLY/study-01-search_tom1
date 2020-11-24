#１．入力したワードで、キャラクターリスト(source)を検索して結果をPrint文で表示してみましょう
#２．１に追加して結果が存在した場合と、しなかった場合で表示する文言が変わるようにしてみましょう
#３．２に追加して結果が存在しなかった場合に、リストに追加できるようにしてみましょう
#４．３に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
#５．４に追加してキャラクターリストをCSVに書き込めるようにしてみましょう


### キャラクターソース作成
def create_source():
    source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
    
    with open("character_source.csv", "wb") as list:
        for e in source:
            list.write((e + "\n").encode('utf-8'))



### 検索ツール
def search():

    with open("character_source.csv", "rb") as list:
        source = list.read().decode('utf-8').strip().split("\n")
    
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は見つかりません".format(word))
        source.append(word)
        with open("character_source.csv", "wb") as list:
            for e in source:
                list.write((e + "\n").encode('utf-8'))
        print("{}を新しく検索ソースに追加しました".format(word))
        


if __name__ == "__main__":
    create_source()
    search()
