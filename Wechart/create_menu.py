from werobot import WeRoBot

robot = WeRoBot()
robot.config["token"] = 321324199008051296
robot.config["APP_ID"] = "wx729f5a7844b39b49"
robot.config["APP_SECRET"] = "3bdc893577a6b15c837fb8de305f1a18"

client = robot.client
print client.get_ip_list()

client.create_menu({"button":[{"type":"click","name":"Love Music","key":"music","sub_button":[{"type":"view","name":"QR_Sunqiang","url":"http://images.cnblogs.com/cnblogs_com/jiangqiuju/1133447/o_wx.png"}]},{"type":"view","name":"Joke","url":"http://39.106.189.163/joke/"},{"type":"view","name":"Baidu","url":"http://www.baidu.com/"}]})

print client.get_menu()
