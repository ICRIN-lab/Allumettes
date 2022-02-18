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
    yes_key_code = "space"  ## à modifier ? réflechir
    quit_code = "q"
    keys = ["space", yes_key_name, quit_code]  ### à définir
    launch_example = True
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    instructions = [f"Dans ce mini-jeu, appuyez sur la touche {yes_key_name} si la flèche centralee.",
                    "S'il-vous-plaît, n'appuyez que lorsqu'on vous le demande ou lors de la tâche",
                    f"Placez vos index sur les touches 'a' et 'p' s'il-vous-plaît",
                    ]
    csv_headers = ['no_trial', 'id_candidate', 'present', 'ans_candidate', 'good_ans', 'correct',
                   'practice', 'reaction_time', 'time_stamp']

    # Conjunction Search Task

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        nb_allumettes = random.randint(50, 200)
        L_ans = [nb_allumettes, int(nb_allumettes * 2.5 - 23)]

        for i in range(nb_allumettes):
            self.create_visual_image(image='allumette.jpg', pos=(randint(-500, 500), randint(-500, 500)),
                                     ori=randint(0, 360), units='pix').draw()
        self.win.flip()
        core.wait(10)

        self.create_visual_text(text=f"Combien d'allumettes avez-vous vu ? ( {L_ans.pop(random.randint(0, 1))} /"
                                     f" {L_ans[0]} )").draw()
        self.win.flip()
        if L_ans[0] == nb_allumettes:
            good_ans = 'p'
        else:
            good_ans = 'a'
        try:
            resp, rt = self.get_response_with_time(timeout=4)
        except (TypeError, AttributeError):
            resp = ""
            rt = 1
        print("aa")  # test pour voir jusqu'où le programme arrive ?

        if resp == good_ans:
            good_answer = True
        else:
            good_answer = False

        self.update_csv(no_trial, self.participant, resp, good_ans, good_answer,
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
