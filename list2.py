marks = [ 30,50,60,70,55,77,11,22,88,99]
average_marks = sum(marks)/len(marks)
count = 0
for mark in marks:
    if mark > average_marks:
        count=count+1
        
print(f"number of students who scored more than average: {count}")


max_count = 0
most_common = marks[0]

for mark in marks:
    if marks.count(mark) > max_count:
        max_count = marks.count(mark)
        most_common = mark

print(f"Most frequent mark: {most_common}, appeared {max_count} times")