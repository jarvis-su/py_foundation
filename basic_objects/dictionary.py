
def basic_dictionary():
    d = {'food':'Spam','quantity':4, 'color':'pink'}
    print(d['food'])
    d['quantity']+=1
    print(d['quantity'])
########################################
    d1 = {}
    d1['name'] = 'Bob'
    d1['job'] = 'dev'
    d1['age'] = 40
    print(d1)
#######################################
    d2 = {'name':{'first':'Bob','last':'Smith'},'job':['dev','mgr'],'age':40.5}
    print(d2['name'])
    print(d2['job'])

    print('sex' in d2)
    if  not 'sex' in d2:
        print('sex is missing')


if __name__ == "__main__":
    basic_dictionary()
    print("hello")