subj_dict = {}
with open('test_5.txt') as file_dict:
    for line in file_dict:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.strip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-']
        subj_dict.update({lesson_type: sum(lesson_count)})

print(subj_dict)




