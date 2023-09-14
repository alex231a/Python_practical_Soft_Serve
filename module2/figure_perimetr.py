import math


def figure_perimetr(val):
    val = val.lstrip('#')
    coord_lis = val.split('#')
    lb = []
    rb = []
    lt = []
    rt = []
    for i in coord_lis:
        i_l = i[2:]
        i_list = i_l.split(':')
        if i[:2] == 'LB':
            lb = i_list
        elif i[:2] == 'RB':
            rb = i_list
        elif i[:2] == 'LT':
            lt = i_list
        elif i[:2] == 'RT':
            rt = i_list

    length1 = math.sqrt(((int(lt[0])-int(rt[0]))**2) + ((int(lt[1])-int(rt[1]))**2))
    length2 = math.sqrt(((int(lb[0]) - int(rb[0])) ** 2) + ((int(lb[1]) - int(rb[1])) ** 2))
    length3 = math.sqrt(((int(lt[0]) - int(lb[0])) ** 2) + ((int(lt[1]) - int(lb[1])) ** 2))
    length4 = math.sqrt(((int(rt[0]) - int(rb[0])) ** 2) + ((int(rt[1]) - int(rb[1])) ** 2))
    fig_per = length1 + length2 + length3 + length4
    return round(fig_per, 14)

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))