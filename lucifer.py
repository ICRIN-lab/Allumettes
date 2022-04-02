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
                    "propositions",
                    "N'appuyez sur les touches que lorsqu'on vous le demande",
                    f"Placez vos index sur les touches 'a' et 'p'",
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
        L = [[39, 52], [30, 41], [62, 50], [49, 58], [47, 40], [70, 62], [65, 74], [39, 26], [57, 69], [47, 35], [75, 61], [60, 34], [69, 24], [47, 48], [70, 23], [48, 47], [54, 40], [77, 15], [76, 16], [56, 38], [46, 49], [54, 40], [49, 46], [32, 64], [37, 59], [46, 49], [34, 62], [51, 43], [55, 39], [48, 47], [80, 12], [44, 51], [48, 47], [34, 62], [80, 12], [32, 64], [80, 12], [74, 18], [31, 65], [72, 20], [63, 30], [63, 30], [73, 19], [61, 32], [45, 50], [70, 23], [76, 16], [69, 24], [73, 19], [43, 52], [55, 39], [80, 12], [61, 32], [39, 57], [31, 65], [44, 51], [39, 57], [77, 15], [67, 26], [78, 14], [31, 65], [40, 56], [43, 52], [80, 12], [48, 47], [68, 25], [33, 63], [39, 57], [41, 54], [44, 51], [32, 64], [46, 49], [66, 27], [42, 53], [40, 56], [37, 59], [67, 26], [75, 17], [46, 49], [58, 36], [47, 48], [80, 12], [30, 67], [47, 48], [65, 28], [41, 54], [54, 40], [41, 54], [38, 58], [72, 20], [74, 18], [72, 20], [49, 46], [76, 16], [50, 44], [67, 26], [70, 23], [63, 30], [44, 51], [63, 30]]
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
