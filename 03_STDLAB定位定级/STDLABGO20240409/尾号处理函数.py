def weihaochuli(shang):
    # 五行属性分类
    wuxing_dict = {
        "水": [1, 6],
        "火": [2, 7],
        "木": [3, 8],
        "金": [4, 9],
        "土": [5, 0]
    }

    # 五行生克关系
    sheng_ke_dict = {
        "水": {"生": "木", "克": "火", "被生": "金", "被克": "土", "本我": "水"},
        "火": {"生": "土", "克": "金", "被生": "木", "被克": "水", "本我": "火"},
        "木": {"生": "火", "克": "土", "被生": "水", "被克": "金", "本我": "木"},
        "金": {"生": "水", "克": "木", "被生": "土", "被克": "火", "本我": "金"},
        "土": {"生": "金", "克": "水", "被生": "火", "被克": "木", "本我": "土"}
    }
    liemingduiying={"上一":}
    # 获取五行属性函数
    def get_wuxing(value):
        for wuxing, numbers in wuxing_dict.items():
            if value in numbers:
                return wuxing
        return None

    # 根据规则计算预测值
    def calculate_yuce(relations):
        possible_values = []
        for upper_value, relation in relations:
            upper_wuxing = get_wuxing(upper_value)
            if upper_wuxing and relation in sheng_ke_dict[upper_wuxing]:
                related_wuxing = sheng_ke_dict[upper_wuxing][relation]
                # 获取该五行对应的数字
                possible_values.append(wuxing_dict[related_wuxing])
        return possible_values


