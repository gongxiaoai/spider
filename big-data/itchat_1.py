import itchat
import WordCloud
itchat.login()
#爬取自己好友相关信息是个好友列表， 返回一个json文件
friends = itchat.get_friends(update=True)[0:]
for i in friends:
    #获取个性签名
    signatrue=i["signatrue"]
print(signatrue)
#初始化计数器
male = female = other = 0
#friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other +=1
#计算朋友总数
total = len(friends[1:])
print("男性好友： %.2f%%" % (int(male)) + "\n" +
"女性好友： %.2f%%" % (int(female)) + "\n" +
"不明性别好友： %.2f%%" % (int(other))+"\n")
#打印出自己的好友性别比例
print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" +
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +

"不明性别好友： %.2f%%" % (float(other) / total * 100))





# import requests
# import itchat
#
# KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
#
# def get_response(msg):
#     apiUrl = 'http://www.tuling123.com/openapi/api'
#     data = {
#         'key'    : KEY,
#         'info'   : msg,
#         'userid' : 'wechat-robot',
#     }
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         return r.get('text')
#     except:
#         return
#
# @itchat.msg_register(itchat.content.TEXT)
# def tuling_reply(msg):
#     defaultReply = 'I received: ' + msg['Text']
#     reply = get_response(msg['Text'])
#     return reply or defaultReply
#
# itchat.auto_login(hotReload=True)
# itchat.run()