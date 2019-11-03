from itertools import combinations_with_replacement
import random


name_txt = 'players.txt'
surnmane_txt = 'name.txt'

names = []
surnmanes = []
youtube_acc = []


def read_youtube_acc(name_txt):
    f = open(name_txt, 'r', encoding="utf8")
    text = f.read().split('\n')
    f.close()
    d = {}
    for i in range(len(text)):
        text[i] = text[i].split(' ')
    for el in text:
        d[el[0]] = el[1]
    return d


def read_name(name_txt):
    f = open('name.txt', 'r', encoding="utf8")
    text = f.read()
    f.close()
    res = text.split('\n')
    res[0] = res[0].split()
    res[1] = res[1].split()
    return res


def read_nick():
    f = open('nick_created.txt', 'r', encoding="utf8")
    text = f.read()
    return text.split('\n')


accounts = read_nick()


def create_nick():
    accounts = []
    name_and_sur = read_name(surnmane_txt)
    for i in range(700):
        tsur = random.choice(name_and_sur[0])
        tname = random.choice(name_and_sur[1])
        ran_num = random.randint(999, 9999)
        accounts.append(str(tsur) + str(tname) + str(ran_num))
    f = open('nick.txt', 'w+', encoding="utf8")
    for el in accounts:
        f.write("%s\n" % (el))


def brute(players, goal):
    return make_string(list(combinations_with_replacement(players, goal)))


def make_string(posible):
    if not len(posible) == 1:
        res = []
        if len(posible[0]) == 1:
            for el in posible:
                res.append(el[0])
        else:
            for el in posible:
                res.append(el[0] + ',' + el[1])
        return res


def flat(array):
    res = []
    for i in array:
        for j in i:
            res.append(j)
    return res


def brute_p(state, d, accounts_pos, t1_name, t2_name):
    res = []
    if d[state][0] is None:
        for i in d[state][1]:
            res.append(str(t1_name +
                           ' ' +
                           state +
                           ' ' +
                           t2_name +
                           ' (' +
                           i +
                           ')' +
                           '  ' +
                           'https://www.instagram.com/' +
                           accounts[accounts_pos]))
            accounts_pos += 1
    elif d[state][1] is None:
        for i in d[state][0]:
            res.append(str(t1_name +
                           ' ' +
                           state +
                           ' ' +
                           t2_name +
                           ' (' +
                           i +
                           ')' +
                           '  ' +
                           'https://www.instagram.com/' +
                           accounts[accounts_pos]))
            accounts_pos += 1
    else:
        for i in d[state][0]:
            for j in d[state][1]:
                res.append(str(t1_name +
                               ' ' +
                               state +
                               ' ' +
                               t2_name +
                               ' (' +
                               i +
                               '-' +
                               j +
                               ')' +
                               '  ' +
                               'https://www.instagram.com/' +
                               accounts[accounts_pos]))
                accounts_pos += 1
    return res, accounts_pos


def brute_force(t1, t2, t1_name, t2_name):
    all_goals, temp = [], []
    accounts_pos = 0
    d = {}
    for i in range(0, 2):
        for j in range(0, 2):
            if (i == j):
                pass
            else:
                state = str(i) + ':' + str(j)
                t1_goals = brute(t1, i)
                t2_goals = brute(t2, j)
                goals = [t1_goals, t2_goals]
                res = {state: goals}
                d.update(res)
                temp, accounts_pos = brute_p(
                    state, d, accounts_pos, t1_name, t2_name)
                all_goals.append(temp)
    return flat(all_goals)


def read(name_txt):
    f = open(name_txt, 'r', encoding="utf8")
    text = f.read()
    f.close()
    return parse(rep(text.split()))


def rep(text):
    res = []
    for el in text:
        res.append(el.replace(',', ''))
    return res


def parse(text):
    res = {}
    temp = []
    teams = []
    for el in text:
        if ':'in el:
            teams.append(el)
    for el in text:
        if el == teams[0]:
            pass
        elif el == teams[1]:
            res[teams[0].replace(':', '')] = temp
            temp = []
        elif el == text[len(text) - 1]:
            temp.append(el)
            res[teams[1].replace(':', '')] = temp
        else:
            temp.append(el)

    return res


def get_predict():
    players_predict = read('players.txt')
    predicts = brute_force(players_predict[list(players_predict.keys())[0]], players_predict[list(
        players_predict.keys())[1]], list(players_predict.keys())[0], list(players_predict.keys())[1])
    #f = open('log.txt','w+',encoding="utf8")
    # for el in predicts:
    #f.write("%s\n" % (el))
    return predicts
