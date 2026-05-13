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


def calculate_yuce(relations):
    sheng_ke_dict = {
        "水": {"生": "木", "克": "火", "被生": "金", "被克": "土", "本我": "水"},
        "火": {"生": "土", "克": "金", "被生": "木", "被克": "水", "本我": "火"},
        "木": {"生": "火", "克": "土", "被生": "水", "被克": "金", "本我": "木"},
        "金": {"生": "水", "克": "木", "被生": "土", "被克": "火", "本我": "金"},
        "土": {"生": "金", "克": "水", "被生": "火", "被克": "木", "本我": "土"}
    }
    possible_values = set()
    for upper_value, relation in relations:
        upper_wuxing = get_wuxing(upper_value)
        if upper_wuxing and relation in sheng_ke_dict[upper_wuxing]:
            related_wuxing = sheng_ke_dict[upper_wuxing][relation]
            # 获取该五行对应的数字
            possible_values.update({k for k, v in wuxing_dict.items() if v == related_wuxing})
    return possible_values


def predict_values(df, df2):
    predictions = []

    # 检查 df2 是否为空


    valuess = {col: df2.at[len(df2) - 1, col] % 10 for col in ['一', '二', '三', '四', '五', '六','七', '特']}
    valuess['gongliweihao'] = df2.at[len(df2) - 1, '日期'].day % 10
    solar_date = df2.at[len(df2) - 1, '日期']
    lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
    valuess['nongliweihao'] = lunar_date.lunar_day % 10
    relationss = [
        (valuess['七'], "克"),
            (valuess['nongliweihao'], "被生"),
            (valuess['六'], "被生"),
            (valuess['nongliweihao'], "生"),
            (valuess['一'], "本我"),
            (valuess['gongliweihao'], "生"),
            (valuess['七'], "生"),
            (valuess['nongliweihao'], "克"),
            (valuess['特'], "克"),
            (valuess['四'], "被克")
    ]
    prediction2 = [calculate_yuce([relation]) for relation in relationss]

    for index in range(1, len(df)):
        # 获取输入值
        values = {col: df.at[index - 1, col] % 10 for col in ['一', '二', '三', '四', '五', '六','七', '特']}
        values['gongliweihao'] = df.at[index - 1, '日期'].day % 10

        # 获取农历日期的个位数
        solar_date = df.at[index - 1, '日期']
        lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
        values['nongliweihao'] = lunar_date.lunar_day % 10
        print(values)

        # 预测关系
        relations = [
            (values['七'], "克"),
            (values['nongliweihao'], "被生"),
            (values['六'], "被生"),
            (values['nongliweihao'], "生"),
            (values['一'], "本我"),
            (values['gongliweihao'], "生"),
            (values['七'], "生"),
            (values['nongliweihao'], "克"),
            (values['特'], "克"),
            (values['四'], "被克")
        ]

        # 计算预测值
        prediction = [calculate_yuce([relation]) for relation in relations]
        predictions.append(prediction)


    return predictions,prediction2


def predict_values2(df):
    predictions = []
    for index in range(1, len(df)):
        # 获取输入值
        values = {col: df.at[index-1, col] % 10 for col in ['一', '二', '三', '四', '五', '六','七', '特']}
        values['gongliweihao'] = df.at[index-1, '日期'].day % 10

        # 获取农历日期的个位数
        solar_date = df.at[index-1, '日期']
        lunar_date = ZhDate.from_datetime(solar_date)  # 转换为农历
        values['nongliweihao'] = lunar_date.lunar_day % 10
        print(values)
        # 预测关系
        relations = [
            (values['七'], "克"),
            (values['nongliweihao'], "被生"),
            (values['六'], "被生"),
            (values['nongliweihao'], "生"),
            (values['一'], "本我"),
            (values['gongliweihao'], "生"),
            (values['七'], "生"),
            (values['nongliweihao'], "克"),
            (values['特'], "克"),
            (values['四'], "被克")

        ]

        # 计算预测值
        prediction = [calculate_yuce([relation]) for relation in relations]
        predictions.append(prediction)

    return predictions
file_path = '福建体彩31选7-2016-2024年数据汇总.xlsx'
xls = pd.ExcelFile(file_path)
sheet_names = sorted(xls.sheet_names, key=lambda x: int(x.replace("年","")))
# 创建一个新的 Excel 写入器
with pd.ExcelWriter('福建体彩31选7-新尾号处理结果特号.xlsx') as writer:
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
            for i in range(10):  # 对于七个预测值
                # 确保 predictions 的长度匹配 df 的行数
                df[f'特{i + 1}'] =[prediction2[i]] +[pred[i] for pred in predictions]  # 将所有的预测值包括最后一天

            # 将结果保存到新的工作表
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            predictions = predict_values2(df)
            # 将预测值添加到新的列
            for i in range(10):  # 对于七个预测值
                # 确保 predictions 的长度匹配 df 的行数
                df[f'特{i + 1}'] = [None] + [pred[i] for pred in predictions]  # 将所有的预测值包括最后一天

            # 将结果保存到新的工作表
            df.to_excel(writer, sheet_name=sheet_name, index=False)