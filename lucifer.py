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
                   'practice', 'group', 'reaction_time', 'time_stamp']

    # Conjunction Search Task

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        group = 'common'
        score = 0
        waiting_time = 2
        self.create_visual_image(image=f'img/allum_{no_trial}.png', size=(width, height)).draw()
        self.win.flip()
        core.wait(waiting_time)
        L = [[11, 16], [72, 91], [39, 53], [74, 86], [52, 68], [87, 105], [42, 56], [69, 79], [78, 96], [46, 58], [18, 24], [37, 47], [39, 47], [62, 77], [45, 61], [63, 73], [19, 33], [30, 43], [11, 24], [28, 37], [13, 21], [49, 59], [88, 93], [23, 38], [74, 93], [83, 103], [39, 58], [82, 94], [54, 62], [60, 79], [76, 91], [59, 69], [50, 58], [73, 82], [61, 71], [80, 95], [17, 24], [87, 103], [67, 84], [68, 78], [45, 54], [73, 92], [83, 97], [16, 26], [39, 45], [54, 60], [54, 62], [37, 43], [71, 76], [28, 38], [15, 32], [11, 28], [63, 72], [88, 105], [37, 50], [71, 86], [51, 71], [10, 22], [51, 67], [44, 54], [14, 29], [79, 94], [81, 100], [24, 31], [90, 109], [82, 94], [48, 61], [25, 35], [86, 91], [53, 65], [69, 74], [43, 51], [25, 36], [20, 34], [38, 52], [66, 74], [55, 73], [46, 64], [53, 70], [25, 40], [58, 71], [14, 30], [35, 42], [23, 34], [51, 69], [38, 56], [84, 101], [18, 36], [57, 66], [88, 97], [41, 48], [49, 67], [31, 41], [41, 49], [34, 45], [51, 63], [82, 87], [81, 88], [55, 69], [13, 23]]
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
