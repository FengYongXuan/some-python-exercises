"""
    练习8
"""


flag = 1

while flag:
    ciphertext = []
    content = ""
    flag = input("\n加密还是解密？加密按'1'，解密按'2'，退出按'0' :")
    try:
        flag = int(flag)
    except ValueError:
        print("请输入整数！")
    else:
        if flag == 1:
            content = input("请输入要加密内容：")
            for char in content:
                ciphertext.append(ord(char))
            print("加密结果：", ciphertext)
        elif flag == 2:
            ciphertext = eval(input("请输入要解密内容："))
            for i in range(len(ciphertext)):
                content += chr(ciphertext[i])
            print("解密结果：", content)
        elif flag != 0:
            print("请输入0或1或2！")
