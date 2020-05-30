# encoding:utf-8
import requests
from requests.exceptions import RequestException
import urllib.parse
import urllib.request
import os
import re


def get_voice(url, name):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    try:
        if response.status_code == 200:
            download_voice(url, name)
        return None
    except RequestException:
        return None


def download_voice(url, name):
    file_path = r'{}.mp3'.format(name)
    if not os.path.exists(file_path):
        print('正在下载:', name, url)
        urllib.request.urlretrieve(url, file_path)
        print('ok!!!!!!!!!')
    else:
        print('下载出错')


def not_empty(s):
    return s and s.strip()


def cut_text(text, length):
    text = re.sub('[\r\n\t]', '', text)
    text_array = list(filter(not_empty, text.split('。')))
    text_i = [0]
    text_len = 0
    list_1 = []
    for i in range(len(text_array)):
        list_1.append(i)
        text_len = text_len + len(text_array[i])
        # print(text_len)
        if text_len > length:
            text_len = 0
            text_len = text_len + len(text_array[i])
            print(text_len)
            text_i.append(i-1)
            list_1.clear()

    if text_i[-1] < (len(text_array) -1):
        text_i.append(len(text_array) -1)

    # print(text_i)
    new_text_i = []
    for i in range(len(text_i) - 1):
        list1 = []
        for a in range(text_i[i] + 1, text_i[i+1] + 1):
            list1.append(a)
        new_text_i.append(list1)
    new_text_i[0].insert(0, 0)
    # print(new_text_i)

    new_text_array = []
    for t in new_text_i:
        x = ''
        for t1 in range(len(t)):
            x += text_array[t[t1]] + '。'
        new_text_array.append(x)

    return new_text_array


def main(appkey, token, voice, speech_rate, format, volume, file_name, text):
    text_array = cut_text(text, 300)
    # print(text_array)
    for text in range(len(text_array)):
        url = 'https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/tts?appkey=' + appkey \
          + '&token=' + token + '&format=' + format + '&voice=' + voice + '&speech_rate=' + str(speech_rate) + '&volume=' + volume + '&text=' + urllib.parse.quote(text_array[text])
        get_voice(url, file_name + str(text))


if __name__ == '__main__':
    voice = 'Aixia'
    appkey = 'VNSQETOK5RRVSeRH'
    token = 'f2852ddf530e4105bd5f784f77aade6d'
    speech_rate = -200
    format = 'mp3'
    volume = 100
    file_name = 'voice'
    text = '''岁月匆匆而过，悄悄回首，我已走进小学生活近六年了，念及往事，不生唏嘘。那人生道路上的无数个第一次就像波涛起伏的海浪，荡漾在我的心头。是那样的亲切而有熟悉，又是那样的美好而和谐。第一次上台表演的经历就一直使我不能忘怀。那是我在五岁第一次上台时，在上台前，我的心忐忑不安，总是无法调整出好的情绪。开始表演了，强烈的镁光灯直射下来，就像一双犀利的眼睛，盯着我喘不过气来。我就更紧张了。当我看到台下这么多人的目光聚集在我的身上，原来就担心的我一下子忘了自己的动作，傻呆呆的站在幕布旁。那一刹那，我听到的音乐就像奔驰的野马，嗡嗡作响；镁光灯则是一把锋利而尖锐的箭，射进了我的内心深处。好在这时，老师在幕布旁不断地鼓励我，小声地说：“你一定能行！”我深深的吸了一口气，很快镇静下来。我微笑着自信地走上了舞台。一上台，我就好像置于一池碧水中，身体变得那样的舒展，跳的每一个动作都是那么娴熟而自然。那音乐如潺潺的溪水，镁光灯也如正午的暖阳。我的舞姿犹如一只傲气的白天鹅在湖面上游动；又像一缕纯洁的阳光，干净而温暖；更像一直蓬勃的向日葵，正努力地向上生长。终于，我在观众们的掌声中退了场。事后，我一直在想：有自信不一定能成功。但是，如果你充满自信，就有成功的希望。自信是飞向蓝天的翅膀，是航行的船桨。在任何时候，自信都会助你一臂之力，助你到达成功的彼岸。让自己成为一个充满自信的人吧！我爱第一次，他教会了我成功的秘笈：充满自信，挑战自信。*'''
    main(voice, appkey, token, speech_rate, file_name, text)