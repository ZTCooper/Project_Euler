ls1 = ['','one','two','three','four','five','six','seven','eight','nine','ten']
ls2 = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
ls3 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
ls4 = ['hundred']
sum1 = sum2 = sum3 = sum4 = sum5 = 0
for i in range(1,11):
    sum1 += len(ls1[i])      #1-10
for i in range(9):
    sum2 += len(ls2[i])      #11-19
for i in range(8):
    for j in range(10):
        sum3 += len(ls3[i]) + len(ls1[j])          #20-99
for i in range(1,10):
    sum4 += (len(ls1[i]) + len(ls4[0])) #整百
sum5 = (sum4 + 3*9)*99 + (sum1 + sum2 + sum3)*9  + 11     

print(sum1+sum2+sum3+sum4+sum5)
