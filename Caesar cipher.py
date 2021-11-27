msg = input("enter your secret message:\n")
shift = -1
while (shift < 1) or (shift > 25):
    try:
        shift = int(input("enter your secret shift: "))
    except:
        print("please enter an integer between 1 and 25")

msg_list = msg.split()
msg_enc =[]
temp_msg = ""
for msg_i in msg_list :
    if not msg_i.isalnum:
        msg_enc.append(msg_i)
        continue
    else:
        temp_msg = ""
        for j in msg_i:
            if not j.isalpha() :
                temp_msg +=(j)
            else :
                if (ord(j) <= ord("Z")) and (ord(j)+shift <= ord("Z")) :
                    temp_msg +=(chr(ord(j)+shift))
                elif (ord(j) <= ord("Z")) and (ord(j)+shift > ord("Z")):
                    temp_msg +=(chr((ord(j)+shift)-26))
                elif (ord(j) >= ord("a")) and (ord(j)+shift <= ord("z")) :
                    temp_msg +=(chr(ord(j)+shift))
                elif (ord(j) >= ord("a")) and (ord(j)+shift > ord("z")) : 
                    temp_msg +=(chr((ord(j)+shift)-26))
        msg_enc.append(temp_msg)

for x in msg_enc :
    print(x,end=" ")

# to_check = input()
# to_check = to_check.replace(" ","")
# to_check = to_check.upper()
# is_pali = True
# if len(to_check) > 1 :
#     for i in range(len(to_check)//2):
#         if to_check[i] != to_check[-(i+1)] :
#             is_pali = False
#             break
# elif len(to_check) == 0 :
#     is_pali = False

# if is_pali :
#     print("It's a palindrome")
# else :
#     print("It's not a palindrome")


# to_check1 = input()
# to_check2 = input()
# to_check1 = to_check1.replace(" ","")
# to_check1 = to_check1.upper()
# to_check2 = to_check2.replace(" ","")
# to_check2 = to_check2.upper()
# is_ana = False
# check_list = []
# for i in to_check1 :
#     check_list.append(i)

# cont = 0
# if len(to_check1) == len(to_check2) :
#     for j in to_check2 :
#         if j in check_list :
#             for k in range(len(check_list)) :
#                 if check_list[k] == j :
#                     del check_list[k:k+1]
#                     break
#         else : break
# if len(check_list) == 0 :
#     is_ana = True
# if is_ana :
#     print("Anagrams")
# else :
#     print("Not anagrams")