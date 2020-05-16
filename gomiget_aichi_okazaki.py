#!/usr/bin/env python3

import sys
from gomireader import GomiReader, PatternValuePair

def main(argv):
    # メモ:
    # 市のホームページでは「ビールびん」の分類が「空きびん」と誤記されているので
    # 空きびん・生きびんについては分類ではなく備考により分別するようにした。
    reader = GomiReader()
    reader.municipality_id = "232025"
    reader.municipality_name = "愛知県岡崎市"
    reader.datasource_url = "https://www.city.okazaki.lg.jp/1100/1108/1151/p003039.html"
    reader.target_url_base = "https://www.city.okazaki.lg.jp/1100/1108/1151/"
    reader.target_pages = [ "p003041.html", "p003042.html", "p003043.html", "p003044.html", "p003045.html", "p003046.html", "p003047.html", "p003048.html", "p003049.html", "p003050.html" ]
    reader.datetime_selector = "span.date"
    reader.datetime_pattern = "最終更新日%Y年%m月%d日"
    reader.article_row_selector = "tbody > tr"
    reader.article_column_selector = "td"
    reader.category_to_category_id = {
        PatternValuePair(r"/（?可燃ごみ）?/", "burnable"),
        PatternValuePair("不燃ごみ", "unburnable"),
        PatternValuePair("粗大ごみ", "oversized"),
        PatternValuePair("有害ごみ", "hazardous.harmful"),
        PatternValuePair("発火性危険ごみ", "hazardous.ignitable"),
        PatternValuePair("紙製容器包装", "paperpackaging"),
        PatternValuePair(r"/プラスチック製容器包?装/", "plasticpackaging"),
        PatternValuePair("ペットボトル", "petbottle"),
        PatternValuePair("空き缶", "can"),
        PatternValuePair("処理困難物", "uncollectible.difficult"),
        PatternValuePair("リサイクル料金が必要。製造メーカーの電話受付窓口へ", "uncollectible.makercollection"),
        PatternValuePair(r"/家電4品目\sリサイクル料金が必要/", "legalrecycling")
    }
    reader.note_to_category_id = [
        PatternValuePair("資源回収または拠点回収へ", "localcollection"),
        PatternValuePair(r"/.*回収協力店へ.*/", "pointcollection"),
        PatternValuePair(r"/.*販売店へ.*/", "uncollectible.sellercollection"),
        PatternValuePair(r"/.*自主回収へ.*/", "uncollectible.sellercollection"),
        PatternValuePair(r"/.*青色のコンテナへ/", "can"),
        PatternValuePair(r"/.*茶色のコンテナへ/", "grassbottle"),
        PatternValuePair(r"/.*白色のコンテナへ/", "reusebottle")
    ]
    reader.category_definitions = {
        "burnable": { "name": "可燃ごみ" },
        "unburnable": { "name": "不燃ごみ" },
        "oversized": { "name": "粗大ごみ" },
        "hazardous": { "name": "危険/有害ごみ" },
        "hazardous.ignitable": { "name": "発火性危険ごみ" },
        "hazardous.harmful": { "name": "有害ごみ" },
        "paperpackaging": { "name": "紙製容器包装" },
        "plasticpackaging": { "name": "プラ容器包装" },
        "petbottle": { "name": "ペットボトル" },
        "reusebottle": { "name": "生きびん" },
        "grassbottle": { "name": "空きびん" },
        "can": { "name": "空き缶" },
        "localcollection": { "name": "資源回収/拠点回収" },
        "pointcollection": { "name": "回収ボックス" },
        "legalrecycling": { "name": "家電リサイクル法対象" },
        "uncollectible": { "name": "回収できません" },
        "uncollectible.difficult": { "name": "回収できません(処理困難)" },
        "uncollectible.sellercollection": { "name": "回収できません(販売店回収)" },
        "uncollectible.makercollection": { "name": "回収できません(メーカー回収)" }
    }
    print(reader.to_json())

if __name__ == "__main__":
    main(sys.argv)
