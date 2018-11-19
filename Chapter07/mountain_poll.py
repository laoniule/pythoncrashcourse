responses={}

polling_active=True

while polling_active:
    name=input("请输入你的姓名： ")
    response=input("你们要去爬哪座山？ ")

    responses[name]=response

    repeat=input("是否需要其他人回答？(Yes/no) ")
    if repeat=="no":
        polling_active=False
print("\n--- 投票结果 ---")
for name,response in responses.items():
    print(name+"要去爬"+response+".")
