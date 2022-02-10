import csv
import statistics as st 

with open("numbers.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)

newdata = []
for i in range(len(filedata)):
    n_num = filedata[i][1]
    newdata.append(n_num)

newdata1 = [int(float (n) ) for n in newdata]

mean = st.mean(newdata1)
median = st.median(newdata1)
mode = st.mode(newdata1)
print(mean)
print(median)
print(mode)

sd = st.stdev(newdata1)
print(sd)