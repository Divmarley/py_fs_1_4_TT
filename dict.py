 
# name = {
#     'firstName' : "ama",
#     'lname' : "kofi",
#     'sname' : "kojo",
# }
 

# # del name['firstName']


# # name.pop('2')
# # name.popitem()
# # name.clear()
# # print(name)

# # pop()
# # clear()
# # popitem()
# # copy()

# # print(name.keys())
# # x = name.values()
# # print(list(x).index("kofi"))

# # name.update({'mname':"qwerty"})
# # print(name)

# # print(len(name))
# x = [1,2,3,4,5]

# print(len(x))


familyTree = {
    'grandmother':{
        'mother':'mum',
        'aunty ama':{
            'child1':'marley',
            'child2':['kofi','kwame'],
        }
    },
   

}

# print(familyTree['grandmother']['aunty ama']['child2'][1])
# print(familyTree['grandmother']['mother'])

# print(fb)


# ans = {
#     'name':{
#         'fn':'kofi',
#         'ls':'sika'
#     }

# }

# print(ans['name']['fn'])


# example ={
#     'name':'kwame',
#     'age':24
# }


personalInfo = {
    'name':'AMA',
    'age':100,
    'sex':'M',
    'address':{
        'location':'osu',
        'street':['labone','kokmlemle','qwerty']
    }
}
# print(personalInfo['name'])
# print(personalInfo['address']['location'])
# print(personalInfo['address']['street'][2])

# check the lenght of the  dict
# print(len(personalInfo))

# print all keys in the dict
# print(personalInfo.keys())

# print all values in the dict
# print(personalInfo.values())

# print datatype of age in the dict
# print(type(personalInfo['age']))


# print( type(personalInfo['age']))
k= str(personalInfo['age'])
print(type(k))