dic = {'Accurate': ['exact', 'precise'], 'exact': ['precise'],
       'astute': ['smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}


words_in_dic_list = []
keys_in_dic_list = []

for key in dic:
    keys_in_dic_list.append(key)
    for word in dic[key]:
        if word not in words_in_dic_list:
            words_in_dic_list.append(word)


key_list = list(dic.keys())
val_list = list(dic.values())


pussy = {"a":["a" , "n" , "k"], "b": "c"}
s = list(pussy)
print(s)


all_lists = []

def boob():
  for word in words_in_dic_list:
    value_list = []
    for i in val_list:
      for j in i:
        if word == j:
          value_list.append(val_list.index(i))
    all_lists.append(value_list)


boob()

new_dic = {}

for value in range(len(all_lists)):
 for x in range(len(all_lists[value])):
  all_lists[value][x]=key_list[x]

for word in words_in_dic_list:
  new_dic[word] = all_lists[words_in_dic_list.index(word)]

print(new_dic)

