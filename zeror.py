#import pandas to load csv
import pandas
#import matplotlib to plot result
import matplotlib.pyplot as plot
#load training data in csv format
train_dataset = pandas.read_csv("zeror_train.csv")
#fetch all values of last column
class_label_data = list(train_dataset.iloc[:,-1])
#fetch unique values from class_label_data
class_label_name = list(set(class_label_data))
#declare a list
class_label_count = []
#loop through class_label_name list and storing it in i
for i in class_label_name:
    #append tuple containg value and count to the list
    class_label_count.append((class_label_data.count(i),i))
#fetch class label with max occurance from tuple
num_max, class_label_max = max(class_label_count)
#load test data in csv format
test_dataset = pandas.read_csv("zeror_test.csv")
#set class_label_max as class label of all instances
output = [class_label_max for i in range(len(test_dataset))]
#count class labels
num_class_labels = len(class_label_name)
#count test data instances
num_test_rows = len(test_dataset)
#plot result
plot.title("Zero-R Predictions")
plot.xlabel("Predicted Classes")
plot.ylabel("Number Of Instances")
#plot a histogram with output and number of bins equal to number of class labels 
plot.hist(output, bins=num_class_labels)
#set x axis start value as 0 and max value as num_class_labels
#set y axis start value as 0 and max value as number of instances (+2 for some padding at top)
plot.axis([0, num_class_labels, 0, num_test_rows+2])
#show graph
plot.show()
