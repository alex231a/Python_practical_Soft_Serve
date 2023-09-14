import re


def max_population(data):
    pattern = r"[a-z]{2}[_][a-z]+[,]\d+"
    max_population = 0
    capital = ''
    data = str(data)
    result = re.findall(pattern, data)
    for i in result:
        res_list = i.split(",")
        if int(res_list[1]) > int(max_population):
            max_population = res_list[1]
            capital = res_list[0]
    val_to_return = (capital, int(max_population))
    return val_to_return

data = ["id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"]


print(max_population(data))