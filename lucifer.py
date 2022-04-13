import random
import time
from random import randint, choice
from list_ans import L
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
    group = "common"
    next = f"Pour passer à l'instruction suivante, appuyez sur la touche {yes_key_name}"
    good_luck = f"Vous êtes prêt ? Appuyez sur la touche {yes_key_name} pour démarrer"
    instructions = [
        f"Dans cette expérience : \n\n - appuyez sur la touche '{yes_key_name}' pour selectionner la réponse "
        f"de droite. \n\n - appuyez sur la touche '{no_key_name}' pour selectionner la réponse de "
        f"gauche.",
        "N'appuyez sur les touches que lorsqu'on vous le demande.",
        "Placez vos index sur les touches 'a' " "et 'p'.",
    ]
    csv_headers = [
        "no_trial",
        "id_candidate",
        "left_ans",
        "right_ans",
        "ans_candidate",
        "good_ans",
        "correct",
        "practice",
        "group",
        "score",
        "reaction_time",
        "time_stamp",
    ]

    def task(self, no_trial, exp_start_timestamp, trial_start_timestamp, practice=False):
        waiting_time = 2
        self.create_visual_image(image=f"img/allum_{no_trial}.png", size=(width, height)).draw()
        self.win.flip()
        core.wait(waiting_time)

        seed = random.randint(0, 1)
        left_ans = L[no_trial][seed]
        self.create_visual_text(text=f"Combien d'allumettes avez-vous vu ? ( {L[no_trial].pop(seed)} / {L[no_trial][0]})").draw()
        self.win.flip()
        if seed:
            good_ans = "p"
        else:
            good_ans = "a"
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

        self.update_csv(
            no_trial,
            self.participant,
            left_ans,
            L[no_trial][0],
            [left_ans if resp == "a" else L[no_trial][0]][0],
            [left_ans if good_ans == "a" else L[no_trial][0]][0],
            correct,
            practice,
            self.group,
            self.score,
            round(rt, 2),
            round(time.time() - exp_start_timestamp, 2),
        )
        self.create_visual_text("").draw()
        self.win.flip()
        if no_trial == 53 and self.score >= 40:
            waiting_time /= 2
            self.group = "pro"

        core.wait(0.5)
        if practice:
            return correct

    def example(self, exp_start_timestamp):
        score_example = 0
        example = self.create_visual_text(text="Commençons par un petit entraînement")
        tutoriel_end = self.create_visual_text(
            text="L'entraînement est désormais terminé"
        )
        example.draw()
        self.create_visual_text(self.next, pos=(0, -0.4), font_size=0.04).draw()
        self.win.flip()
        self.wait_yes()
        for i in range(3):
            if self.task(i, exp_start_timestamp, time.time(), True):
                score_example += 1
                self.create_visual_text(
                    f"Bravo ! Vous avez {score_example}/{i + 1}"
                ).draw()
                self.win.flip()
                core.wait(2)
            else:
                self.create_visual_text(
                    f"Dommage... Vous avez {score_example}/{i + 1}"
                ).draw()
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
