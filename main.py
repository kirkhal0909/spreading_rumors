import numpy as np

class Spreading_rumors:
    def calculate_spreading(self, probability, count_people, talks, days_calc=20):
        day = 1
        print()
        print("Day - 0; count people who know - {};\nspreading by 1 talk - {:.2f}%;".format(count_people, probability*100))
        print("Talks {}".format(talks))
        while day <= days_calc:
            new_people_who_knows = sum(np.random.binomial(1, probability, count_people*talks))
            count_people += new_people_who_knows
            print("Day - {}; count people who know - {};\tnew people - {}".format(day, count_people, new_people_who_knows))
            day += 1

probability_of_spreading = 0.0001
people_count_who_knows = 1
talks_for_one = 10

sr = Spreading_rumors()
sr.calculate_spreading(probability_of_spreading, people_count_who_knows, talks_for_one, 365*4)