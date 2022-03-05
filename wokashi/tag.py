from bs4.element import Tag as BSTag


class Tag:
    """
    Tagで囲まれている要素
    """

    def __init__(self, origin_tag: BSTag):
        self.origin_tag = origin_tag

    def get_origin_tag(self) -> BSTag:
        """
        元のbs4.element.Tagを取得
        """
        return self.origin_tag

    def get_text(self) -> str:
        """
        タグに囲まれた文字列を取得
        """
        # Tagオブジェクトの文字列を取るときには、
        # tag.stringではなくtag.get_text()を使う
        # https://maitakeramen.hatenablog.com/entry/2019/09/07/220623
        return self.get_origin_tag().get_text()
