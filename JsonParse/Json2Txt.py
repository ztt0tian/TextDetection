import json


def conversion(oldPoint):
    # print(type(oldPoint))
    target_str = ""
    for i in range(len(oldPoint)):
        target_str += str(oldPoint[len(oldPoint) - i - 1]) + ","
    #     print("正序号：%s   值：%s" % (i + 1, oldPoint[i]))
    # for i in range(len(oldPoint)):
    #     print("倒序号：%s   值：%s" % (i + 1, oldPoint[len(oldPoint)-i-1]))
    return target_str.replace('[', '').replace(']', '')


with open("train_full_labels.json", 'r') as load_f:
    load_dict = json.load(load_f)
# print(load_dict)
items1 = load_dict.items()
fileDir = 'E:/train_full_labels/'
for key, value in items1:
    print(str(key) + '=' + str(value))
    for item in value:
        # print(item)
        with open(fileDir+str(key)+'.txt', 'a+', encoding='utf8') as newf:
            _2_text = item['transcription']  # 文本内容
            _2_point = item['points']  # 点List
            oneLine = conversion(_2_point) + _2_text
            print(oneLine)
            newf.write(oneLine + '\n')  # 加\n换行显示
    # print(_2_text)
    # print(_2_point)
# items2=value.items()
# for key2, value2 in items2:
#     print(key2+"=="+value2)
# point=[[649, 317], [665, 317], [662, 331], [648, 331]]
#
# print(conversion(point))
