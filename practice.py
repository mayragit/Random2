fileObj = open('Downloads/PythonForBiology/examples/chromoData.tsv')
values = []
header = fileObj.readline()

for line in fileObj:
   data = line.split()
   chromosome, position, value = data
   position = int(position)
   value = float(value)

   values.append(value)
   print(sum(values)/len(values))

print("add new line")