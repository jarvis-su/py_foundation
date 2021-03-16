import  os

path = os.getcwd()
print(path)

source_path = 'C:\\Users\\Jarvis\\Desktop\\问诊量\\data1'
os.chdir(source_path)
path = os.getcwd()
print(path)
meraged_path = path+'\\meraged'
if os.path.exists(meraged_path):
    print(meraged_path + ' is existed !')
else:
    os.makedirs(path+'\\meraged')
    print('Created the path ' + meraged_path)
total_size = 0
for file_name in os.listdir(source_path):
    total_size = total_size + os.path.getsize(os.path.join(source_path,file_name))
    file_path = os.path.join(source_path,file_name)
    if os.path.isfile(file_path):
        print(file_path)


print(total_size)