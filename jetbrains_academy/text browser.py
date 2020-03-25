import os
import sys
def open_file(dir, file_name, page):
    file = open(f'{dir}/{file_name}.txt', 'w', encoding='utf-8')
    file.write(page)
    file.flush()
    file.close()

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
dirName = sys.argv
# print(dirName[1])
if not os.path.exists(dirName[1]):
    os.mkdir(dirName[1])
    # print("Directory " , dirName[1] ,  " Created ")
enter_url = ''
pages = []

def verify_path():
    teste = ''
    for _, _, arquivo in os.walk(dirName[1]):
        for i in arquivo:
            if i in pages:
                print('esta')
            else:
                pages.append(''.join(i.strip('.txt')))
        # if arquivo not in pages:
        #     pages.append(arquivo)
        return pages
while enter_url != "exit":
    enter_url = input()

    pasta = verify_path()
    if enter_url in pasta:
        # print(verify_path())
        # print('entrou teste aquivo')
        if 'bloomberg' in enter_url:
            print(bloomberg_com)
        elif 'nytimes' in enter_url:
            print(nytimes_com)
    else:
        if '.com' in enter_url or '.org' in enter_url:
            if 'bloomberg' in enter_url:
                open_file(dirName[1], 'bloomberg', bloomberg_com)
                print(bloomberg_com)
            elif 'nytimes' in enter_url:
                open_file(dirName[1], 'nytimes', nytimes_com)
                print(nytimes_com)
            else:
                print('Error: Incorrect URL')
        elif 'exit' in enter_url:
                break
        else:
            print('Error: Incorrect URL')




