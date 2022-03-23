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
    yes_key_name = "espace"
    yes_key_code = "space"
    quit_code = "q"
    keys = ["a", "p", "space", yes_key_name, quit_code]
    launch_example = False
    trials = 50
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    instructions = ["Dans ce mini-jeu, vous devez deviner le nombre d'allumettes présentes sur l'image !",
                    "S'il-vous-plaît, n'appuyez que lorsqu'on vous le demande ou lors de la tâche",
                    f"Placez vos index sur les touches 'a' et 'p' s'il-vous-plaît",
                    ]
    csv_headers = ['no_trial', 'id_candidate', 'left_ans', 'right_ans', 'ans_candidate', 'good_ans', 'correct',
                   'practice', 'reaction_time', 'time_stamp']

    # Conjunction Search Task

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        self.create_visual_image(image=f'img/allum_{no_trial}.png').draw()
        self.win.flip()
        core.wait(0.7)
        L = [[44, 51], [61, 32], [54, 40], [71, 21], [33, 63], [73, 19], [50, 44], [47, 48], [73, 19], [40, 56], [36, 60], [35, 61], [66, 27], [53, 41], [62, 31], [75, 17], [62, 31], [40, 56], [53, 41], [65, 28], [48, 47], [55, 39], [76, 16], [62, 31], [51, 43], [58, 36], [44, 51], [54, 40], [37, 59], [62, 31], [54, 40], [37, 59], [59, 35], [43, 52], [41, 54], [57, 37], [68, 25], [42, 53], [53, 41], [74, 18], [54, 40], [60, 34], [66, 27], [43, 52], [57, 37], [43, 52], [74, 18], [71, 21], [60, 34], [54, 40]]

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
            resp, rt = self.get_response_with_time(timeout=4)
        except (TypeError, AttributeError):
            resp = ""
            rt = 1

        if resp == good_ans:
            correct = True
        else:
            correct = False

        self.update_csv(no_trial, self.participant, left_ans, L[no_trial][0], [left_ans if resp == 'a' else L[no_trial][0]][0], [left_ans if good_ans == 'a' else L[no_trial][0]][0], correct,
                        practice, round(rt, 2), round(time.time() - exp_start_timestamp, 2))
        self.create_visual_text("").draw()
        self.win.flip()
        rnd_time = randint(8, 14)
        core.wait(rnd_time * 10 ** -3)
        if practice:
            return good_answer

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
