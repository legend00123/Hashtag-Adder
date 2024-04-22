#Function
def adtag():
    with open("sample.txt", 'r') as file_object:
        data = file_object.read()
        main_object = data.split(',')
        for index, tag in enumerate(main_object):
            main_object[index] = '#' + tag

    with open("sample.txt", 'w') as file_object:
        file_object.write(','.join(main_object))


#Function call
adtag()

