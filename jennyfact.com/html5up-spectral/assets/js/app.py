from random import *


def get_fact():
    """
    From jenny_fun_facts.txt, returns random fun fact from list
    :return: string
    """
    open_file = open('jenny_fun_facts.txt', "r")
    lines = open_file.readlines()
    num_of_lines = len(lines)
    random_index = randint(0, num_of_lines)
    count = 0
    fun_fact = "fun_fact is initiated"
    for line in lines:
        if count == random_index:
            fun_fact = line
        count = count + 1
    open_file.close()
    return fun_fact

#
# urls = ('/', 'index')
# render = web.template.render('/')
# app = web.application(urls, globals())
# my_form = web.form.Form(
#             web.form.Textbox('', class_='textfield')
#             )
#
#
# class index:
#     def GET(self):
#         form = my_form()
#         return render.tutorial(form, get_fact())
#
#     def POST(self):
#         form = my_form()
#         form.validates()
#         s = form.value['textfield']
#         return make_text(s)


if __name__ == '__main__':
    get_fact()