unconfirned_user=["alice","brian","candas"]
confirmed_users=[]

while unconfirned_user:
    current_user=unconfirned_user.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)