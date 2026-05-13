import pandas as pd
from zhdate import ZhDate

wuxing_dict = {
    1: "水", 6: "水",
    2: "火", 7: "火",
    3: "木", 8: "木",
    4: "金", 9: "金",
    5: "土", 0: "土"
}
def get_wuxing(value):
    wuxing_dict = {
        1: "水", 6: "水",
        2: "火", 7: "火",
        3: "木", 8: "木",
        4: "金", 9: "金",
        5: "土", 0: "土"
    }
    return wuxing_dict.get(value)


def calculate_yuce(relations_sublist):
    sheng_ke_dict = {
        "水": {"生": "木", "克": "火", "被生": "金", "被克": "土", "本我": "水"},
        "火": {"生": "土", "克": "金", "被生": "木", "被克": "水", "本我": "火"},
        "木": {"生": "火", "克": "土", "被生": "水", "被克": "金", "本我": "木"},
        "金": {"生": "水", "克": "木", "被生": "土", "被克": "火", "本我": "金"},
        "土": {"生": "金", "克": "水", "被生": "火", "被克": "木", "本我": "土"}
    }
    result_list = []

    for upper_value, relation in relations_sublist:
        possible_values = set()
        upper_wuxing = get_wuxing(upper_value)

        if upper_wuxing and relation in sheng_ke_dict[upper_wuxing]:
            related_wuxing = sheng_ke_dict[upper_wuxing][relation]
            possible_values.update({k for k, v in wuxing_dict.items() if v == related_wuxing})

        result_list.append(list(possible_values))

    return result_list


def predict_values(df, df2):
    predictions = []

    # 检查 df2 是否为空


    valuess = {col: df2.at[len(df2) - 1, col] % 10 for col in ['一', '二', '三', '四', '五', '六', '特']}
    valuess['gongliweihao'] = df2.at[len(df2) - 1, '日期'].day % 10
    solar_date = df2.at[len(df2) - 1, '日期']
    lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
    valuess['nongliweihao'] = lunar_date.lunar_day % 10
    # 修改后的各个列表
    shang1yuce_relations = [(valuess['五'], "被生"), (valuess['特'], "生"), (valuess['二'], "本我")]
    shang2yuce_relations = [(valuess['特'], "克"), (valuess['五'], "被生"), (valuess['nongliweihao'], "克")]
    shang3yuce_relations = [(valuess['五'], "克"), (valuess['六'], "被克"), (valuess['五'], "被生")]
    shang4yuce_relations = [(valuess['一'], "生"), (valuess['gongliweihao'], "被生"), (valuess['特'], "被克")]
    shang5yuce_relations = [(valuess['nongliweihao'], "本我"), (valuess['一'], "被克"), (valuess['四'], "被生")]
    shang6yuce_relations = [(valuess['一'], "克"), (valuess['nongliweihao'], "被生"), (valuess['六'], "被克")]
    shangteyuce_relations = [(valuess['四'], "生"), (valuess['六'], "本我"), (valuess['一'], "被生")]
    relationss = [
        shang1yuce_relations,
        shang2yuce_relations,
        shang3yuce_relations,
        shang4yuce_relations,
        shang5yuce_relations,
        shang6yuce_relations,
        shangteyuce_relations
    ]
    prediction2 = [calculate_yuce(relation) for relation in relationss]

    for index in range(1, len(df)):
        # 获取输入值
        values = {col: df.at[index - 1, col] % 10 for col in ['一', '二', '三', '四', '五', '六', '特']}
        values['gongliweihao'] = df.at[index - 1, '日期'].day % 10

        # 获取农历日期的个位数
        solar_date = df.at[index - 1, '日期']
        lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
        values['nongliweihao'] = lunar_date.lunar_day % 10
        print(values)

        shang1yuce_relations = [(values['五'], "被生"), (values['特'], "生"), (values['二'], "本我")]
        shang2yuce_relations = [(values['特'], "克"), (values['五'], "被生"), (values['nongliweihao'], "克")]
        shang3yuce_relations = [(values['五'], "克"), (values['六'], "被克"), (values['五'], "被生")]
        shang4yuce_relations = [(values['一'], "生"), (values['gongliweihao'], "被生"), (values['特'], "被克")]
        shang5yuce_relations = [(values['nongliweihao'], "本我"), (values['一'], "被克"), (values['四'], "被生")]
        shang6yuce_relations = [(values['一'], "克"), (values['nongliweihao'], "被生"), (values['六'], "被克")]
        shangteyuce_relations = [(values['四'], "生"), (values['六'], "本我"), (values['一'], "被生")]

        # 汇总成一个列表
        relations = [
            shang1yuce_relations,
            shang2yuce_relations,
            shang3yuce_relations,
            shang4yuce_relations,
            shang5yuce_relations,
            shang6yuce_relations,
            shangteyuce_relations
        ]
        # 计算预测值
        prediction = [calculate_yuce(relation) for relation in relations]
        predictions.append(prediction)


    return predictions,prediction2


def predict_values2(df):
    predictions = []
    for index in range(1, len(df)):
        # 获取输入值
        values = {col: df.at[index-1, col] % 10 for col in ['一', '二', '三', '四', '五', '六', '特']}
        values['gongliweihao'] = df.at[index-1, '日期'].day % 10

        # 获取农历日期的个位数
        solar_date = df.at[index-1, '日期']
        lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
        values['nongliweihao'] = lunar_date.lunar_day % 10
        print(values)
        # 预测关系
        shang1yuce_relations = [(values['五'], "被生"), (values['特'], "生"), (values['二'], "本我")]
        shang2yuce_relations = [(values['特'], "克"), (values['五'], "被生"), (values['nongliweihao'], "克")]
        shang3yuce_relations = [(values['五'], "克"), (values['六'], "被克"), (values['五'], "被生")]
        shang4yuce_relations = [(values['一'], "生"), (values['gongliweihao'], "被生"), (values['特'], "被克")]
        shang5yuce_relations = [(values['nongliweihao'], "本我"), (values['一'], "被克"), (values['四'], "被生")]
        shang6yuce_relations = [(values['一'], "克"), (values['nongliweihao'], "被生"), (values['六'], "被克")]
        shangteyuce_relations = [(values['四'], "生"), (values['六'], "本我"), (values['一'], "被生")]

        # 汇总成一个列表
        relations = [
            shang1yuce_relations,
            shang2yuce_relations,
            shang3yuce_relations,
            shang4yuce_relations,
            shang5yuce_relations,
            shang6yuce_relations,
            shangteyuce_relations
        ]

        # 计算预测值
        prediction = [calculate_yuce(relation) for relation in relations]
        predictions.append(prediction)

    return predictions
file_path = '香港2010-2024年原始数据.xlsx'
xls = pd.ExcelFile(file_path)
sheet_names = sorted(xls.sheet_names, key=lambda x: int(x.replace("年","")))
# 创建一个新的 Excel 写入器
with pd.ExcelWriter('香港新尾号处理结果二阶段-低-2010-2024.xlsx') as writer:
    # 遍历所有工作表
    for sheet_name in sheet_names:
        print(sheet_name)
        indexx=sheet_names.index(sheet_name)
        if indexx!=0:
            df2=pd.read_excel(xls,sheet_name=sheet_names[indexx-1])
            print(f"df2的值:{df2}")
            df = pd.read_excel(xls, sheet_name=sheet_name)
            predictions = predict_values(df,df2)[0]
            prediction2=predict_values(df,df2)[1]
            # 将预测值添加到新的列
            for i in range(7):  # 对于七个预测值
                # 确保 predictions 的长度匹配 df 的行数
                df[f'{i + 1}号'] =[prediction2[i]] +[pred[i] for pred in predictions]  # 将所有的预测值包括最后一天

            # 将结果保存到新的工作表
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            predictions = predict_values2(df)
            # 将预测值添加到新的列
            for i in range(7):  # 对于七个预测值
                # 确保 predictions 的长度匹配 df 的行数
                df[f'{i + 1}号'] = [None] + [pred[i] for pred in predictions]  # 将所有的预测值包括最后一天

            # 将结果保存到新的工作表
            df.to_excel(writer, sheet_name=sheet_name, index=False)