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
    keys = ["space", yes_key_name, no_key_name, quit_code]
    launch_example = True
    trials = 100
    score = 0
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    good_luck = f"Vous êtes prêt ? Appuyez sur la touche {yes_key_name} pour démarrer"
    instructions = ["Dans cette tâche cognitive, choisissez le nombre d'allumettes présentes parmi les deux "
                    "propositions.",
                    "N'appuyez sur les touches que lorsqu'on vous le demande.",
                    f"Placez vos index sur les touches 'a' et 'p'.",
                    ]
    csv_headers = ['no_trial', 'id_candidate', 'left_ans', 'right_ans', 'ans_candidate', 'good_ans', 'correct',
                   'practice', 'group', 'score', 'reaction_time', 'time_stamp']

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        group = 'common'
        waiting_time = .1  # change to 2 seconds
        self.create_visual_image(image=f'img/allum_{no_trial}.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(waiting_time)
        L = [[79, 86], [72, 84], [39, 49], [82, 100], [44, 57], [23, 35], [79, 96], [86, 93], [76, 95], [68, 74],
             [36, 44], [53, 58], [75, 80], [81, 90], [16, 27], [21, 31], [16, 22], [50, 58], [50, 61], [71, 82],
             [77, 97], [84, 92], [81, 97], [90, 108], [28, 38], [17, 24], [40, 49], [65, 74], [47, 60], [61, 74],
             [46, 58], [27, 43], [41, 53], [89, 99], [69, 86], [43, 61], [87, 96], [54, 59], [68, 76], [36, 48],
             [56, 62], [69, 78], [45, 56], [59, 79], [62, 67], [74, 90], [14, 28], [10, 30], [58, 73], [39, 58],
             [75, 95], [71, 91], [11, 26], [80, 93], [53, 62], [87, 96], [76, 91], [58, 66], [75, 94], [67, 75],
             [86, 102], [86, 105], [52, 68], [56, 74], [29, 40], [53, 58], [64, 83], [76, 96], [40, 55], [26, 34],
             [43, 50], [50, 56], [18, 23], [17, 28], [83, 91], [81, 101], [71, 80], [37, 44], [62, 77], [17, 27],
             [88, 101], [63, 75], [66, 75], [43, 60], [16, 25], [42, 49], [80, 94], [66, 77], [13, 26], [38, 46],
             [70, 86], [28, 48], [51, 66], [33, 46], [83, 103], [73, 90], [30, 46], [87, 94], [43, 56], [64, 75],
             [43, 63], [51, 61], [31, 46]]
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
            if not practice:
                self.score += 1
        else:
            correct = False

        self.update_csv(no_trial, self.participant, left_ans, L[no_trial][0],
                        [left_ans if resp == 'a' else L[no_trial][0]][0],
                        [left_ans if good_ans == 'a' else L[no_trial][0]][0], correct,
                        practice, group, self.score, round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        self.create_visual_text("").draw()
        self.win.flip()
        if no_trial == 53 and self.score >= 40:
            waiting_time /= 2
            group = 'pro'

        core.wait(.5)
        if practice:
            return correct

    def example(self, exp_start_timestamp):
        score_example = 0
        example = self.create_visual_text(text='Commençons par un exemple')
        tutoriel_end = self.create_visual_text(text="Le tutoriel est désormais terminé")
        example.draw()
        self.create_visual_text(self.next, pos=(0, -0.4), font_size=0.04).draw()
        self.win.flip()
        self.wait_yes()
        for i in range(3):
            if self.task(i, exp_start_timestamp, time.time(), True):
                score_example += 1
                self.create_visual_text(f"Bravo ! Vous avez {score_example}/{i + 1}").draw()
                self.win.flip()
                core.wait(2)
            else:
                self.create_visual_text(f"Dommage... Vous avez {score_example}/{i + 1}").draw()
                self.win.flip()
                core.wait(2)
        self.create_visual_text("+").draw()
        self.win.flip()
        core.wait(1)
        results = self.create_visual_text(f"Vous avez obtenu {score_example}/3")
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
