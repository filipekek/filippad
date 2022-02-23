import random

def which_door_prize():
    prize_list = [False, False, False]
    pl_index = random.randint(0,2)
    prize_list[pl_index] = True
    return prize_list, pl_index


def which_door_pick(prize_list):
    door_chosen = random.randint(0,2)
    return prize_list[door_chosen], door_chosen

def moderator(prize_list, door_chosen, door_chosen_f_t):
    moderator_choose_list = list()
    for d in range(3):
        if prize_list[d] == True:
            continue
        if d == door_chosen:
            continue
        else:
            moderator_choose_list.append(d)
    return moderator_choose_list

thousand_tries = list()
success1 = list()
success2 = list()

for x in range(100000):
    prize_list, pl_index = which_door_prize()
    door_chosen_f_t, door_chosen = which_door_pick(prize_list)
    thousand_tries.append(door_chosen_f_t)
    moderated_list = moderator(prize_list, door_chosen, door_chosen_f_t)
    moderator_chose = random.choice(moderated_list)
    door_changed = [0, 1, 2]
    door_changed.remove(door_chosen)
    door_changed.remove(moderator_chose)
    door_changed = door_changed[0]
#    print([pl_index, door_chosen] + moderated_list + [door_changed])
    success1.append(door_chosen==pl_index)
    success2.append(door_changed==pl_index)



# print(thousand_tries)
trues_percentage = sum(thousand_tries)/len(thousand_tries)
percentage1 = sum(success1)/len(success1)
percentage2 = sum(success2)/len(success2)
print([percentage1, percentage2])

