#coding:utf-8
dic ={1:10,3:22,2:21,4:67}
print dic    

out = open('output.txt','w')
print dic[1]
for i in range(len(dic)):
    num = dic[i+1]
    if i == 0 : out.write("%s" %num)
    else: out.write("\n%s" % num)
