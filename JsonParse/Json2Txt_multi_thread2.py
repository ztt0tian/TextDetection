import json
import threading
import time


def conversion(oldPoint):
    # print(type(oldPoint))
    target_str = ""
    for i in range(len(oldPoint)):
        target_str += str(oldPoint[len(oldPoint) - i - 1]) + ","
    #     print("正序号：%s   值：%s" % (i + 1, oldPoint[i]))
    # for i in range(len(oldPoint)):
    #     print("倒序号：%s   值：%s" % (i + 1, oldPoint[len(oldPoint)-i-1]))
    return target_str.replace('[', '').replace(']', '')


fileDir = 'E:/train_full_labels6/'


def write2Txt(filename, content):
    with open(fileDir + filename + '.txt', 'w+', encoding='utf8') as f:
        f.write(content)


import datetime
starttime = datetime.datetime.now()
with open("train_full_labels.json", 'r') as load_f:
    load_dict = json.load(load_f)
items1 = load_dict.items()
for key, value in items1:
    # print(str(key) + '=' + str(value))
    fileName = str(key)
    conent = ""
    # thread_num=1
    # if thread_num%1000==0:
    #     time.sleep(1)#每建立一千个线程等待1秒//OSError: [Errno 24] Too many open files
    for item in value:
        _2_text = item['transcription']  # 文本内容
        _2_point = item['points']  # 点List
        conent += conversion(_2_point) + _2_text + "\n"
    t = threading.Thread(target=write2Txt, args=(fileName, conent,))
    t.setDaemon(True)
    t.start()
    # thread_num=thread_num+1
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)

