import random
import time
from random import randint, choice
import os
from psychopy import core, visual
from task_template import TaskTemplate
from screeninfo import get_monitors

screen = get_monitors()[0]

width = screen.width
height = screen.height


class AllumettesTask(TaskTemplate):
    yes_key_name = "p"
    yes_key_code = "p"
    no_key_code = "a"
    no_key_name = "a"
    quit_code = "q"
    keys = ["space", yes_key_name,no_key_name, quit_code]
    launch_example = False
    trials = 50
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    good_luck = f"Vous êtes prêt ? Appuyez sur la touche {yes_key_name} pour démarrer"
    instructions = ["Dans cette tâche cognitive, choisissez le nombre d'allumettes présentes parmi les deux "
                    "propositions.",
                    "N'appuyez sur les touches que lorsqu'on vous le demande.",
                    f"Placez vos index sur les touches 'a' et 'p'.",
                    ]
    csv_headers = ['no_trial', 'id_candidate', 'left_ans', 'right_ans', 'ans_candidate', 'good_ans', 'correct',
                   'practice','group', 'reaction_time', 'time_stamp']

    # Conjunction Search Task

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        group = 'common'
        score = 0
        waiting_time = 2
        self.create_visual_image(image=f'img/allum_{no_trial}.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(waiting_time)
        L = [[52, 64], [71, 78], [15, 21], [23, 38], [71, 81], [63, 72], [33, 47], [53, 65], [31, 47], [29, 41], [10, 16], [35, 46], [59, 73], [86, 97], [89, 107], [58, 64], [36, 45], [23, 41], [79, 96], [79, 91], [62, 77], [11, 19], [37, 49], [32, 49], [90, 105], [37, 55], [41, 49], [19, 36], [45, 55], [49, 57], [19, 24], [76, 83], [46, 54], [78, 96], [80, 88], [74, 81], [62, 81], [52, 67], [10, 16], [27, 33], [34, 52], [52, 59], [52, 70], [54, 72], [67, 87], [33, 49], [26, 31], [33, 34], [33, 53], [33, 52], [14, 25], [27, 37], [20, 36], [17, 31], [24, 39], [26, 36], [10, 27], [16, 33], [18, 35], [22, 28], [30, 36], [18, 25], [18, 34], [15, 30], [9, 27], [16, 24], [30, 39], [15, 25], [8, 23], [12, 19], [27, 36], [28, 34], [7, 14], [27, 43], [10, 22], [36, 16], [40, 27], [44, 31], [40, 19], [40, 18], [56, 19], [20, 25], [24, 14], [48, 25], [32, 26], [20, 21], [28, 23], [44, 29], [36, 28], [52, 18], [12, 12], [52, 22], [24, 11], [48, 18], [28, 14], [28, 23], [20, 24], [12, 19], [52, 25], [24, 24]]
        seed = random.randint(0, 1)
        left_ans = L[no_trial][seed]
        self.create_visual_text(text=f"Combien d'allumettes avez-vous vu ? ( {L[no_trial].pop(seed)} /"
                                     f" {L[no_trial][0]} )").draw()
        self.win.flip()
        if seed:
            good_ans = 'p'
        else:
            good_ans = 'a'
        try:
            resp, rt = self.get_response_with_time()
        except (TypeError, AttributeError):
            resp = ""
            rt = 1

        if resp == good_ans:
            correct = True
            score += 1
        else:
            correct = False

        self.update_csv(no_trial, self.participant, left_ans, L[no_trial][0], [left_ans if resp == 'a' else L[no_trial][0]][0], [left_ans if good_ans == 'a' else L[no_trial][0]][0], correct,
                        practice, group, round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        self.create_visual_text("").draw()
        self.win.flip()
        if no_trial == 50 and score >= 40:
            waiting_time /= 2
            group = 'pro'

        core.wait(.5)
        if practice:
            return correct

    def example(self, exp_start_timestamp):
        score = 0
        example = self.create_visual_text(text='Commençons par un exemple')
        tutoriel_end = self.create_visual_text(text="Le tutoriel est désormais terminé")
        example.draw()
        self.create_visual_text(self.next, pos=(0, -0.4), font_size=0.04).draw()
        self.win.flip()
        self.wait_yes()
        for i in range(3):
            if self.task(i, exp_start_timestamp, time.time(), True):
                score += 1
                self.create_visual_text(f"Bravo ! Vous avez {score}/{i + 1}").draw()
                self.win.flip()
                core.wait(2)
            else:
                self.create_visual_text(f"Dommage... Vous avez {score}/{i + 1}").draw()
                self.win.flip()
                core.wait(2)
        self.create_visual_text("+").draw()
        self.win.flip()
        core.wait(1)
        results = self.create_visual_text(f"Vous avez obtenu {score}/3")
        results.draw()
        self.win.flip()
        core.wait(5)
        tutoriel_end.draw()
        self.win.flip()
        core.wait(5)

    def quit_experiment(self):
        exit()


if not os.path.isdir("csv"):
    os.mkdir("csv")
exp = AllumettesTask("csv")
exp.start()
