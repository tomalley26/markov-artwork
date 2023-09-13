from PIL import Image
import numpy as np
from random import *

class MarkovCollager:
    def __init__(self, transition_matrix):
        """ Class that creates collages based on probabilities of motifs
        in the transition matrix. 
            Args:
                transition_matrix: dictionary of transition probabilities
        """
        self.transition_matrix = transition_matrix
        self.motifs = list(transition_matrix.keys())

    def get_next_motif(self, current_motif):
        """ Function that chooses the next motif based on the previous one
        using the transition probabilities in the transition matrix.
            Args:
                current_motif: The most recently chosen motif
        """
        return np.random.choice(
            self.motifs,
            p = [self.transition_matrix[current_motif][next_motif] \
                for next_motif in self.motifs]
        )

    def choose_combination(self, current_motif="bowls", length=5):
        """ Function that calls previous function get_next_motif to create
        an array of motif names that will determine the contents of the collage.
            Args:
                current_motif: Currently set to "cake" but can be changed
                length: number of motifs in the collage
        """
        combination = []

        while len(combination) < length:
            next_motif = self.get_next_motif(current_motif)
            combination.append(next_motif)
            current_motif = next_motif
        
        return combination

    def create_collage(self, combination):
        """ Uses the combination of motifs to paste images into the collage 
        and display on screen.
            Args: 
                combination: array of motif names used to create collage
        """
        background = Image.new("RGBA", (1000,2000), color=(255,255,255))

        # coin variable is used to calculate a random location for the last motif
        coin = randint(0,3)
        print(coin)

        for motif in combination:
            img = Image.open("/Users/tomalley/markov-artwork/assets/" + motif + ".png")
            img = img.resize((500,500))

            if motif == combination[0]:
                background.paste(img, (0,0))

            if motif == combination[1]:
                background.paste(img, (500,500))

            if motif == combination[2]:
                background.paste(img, (0,1000))

            if motif == combination[3]:
                background.paste(img, (500,1500))

            if coin == 0 and motif == combination[4]:
                background.paste(img, (500,0))

            if coin == 1 and motif == combination[4]:
                background.paste(img, (0,500))

            if coin == 2 and motif == combination[4]:
                background.paste(img, (500,1000))
            
            if coin == 3 and motif == combination[4]:
                background.paste(img, (0,1500))

            

        background.show()


def main():
    """ Creates an instance of the MarkovCollager class and contains the Markov transition
    matrix for determining which motifs are included in the collage. Calls the necessary
    functions to display the finished collage.
    """
    collage_maker = MarkovCollager({
        "cake": {"cake": 0.03, "orange": 0.07, "bokchoy": 0.2, "rice": 0.1, "salmon": 0.1, "whiterabbit": 0.1, "lindt": 0.08, "kikkoman": 0.04, "bowls": 0.07, "sauce": 0.08, "dumplings": 0.07, "fishhead": 0.06},
        "orange": {"cake": 0.06, "orange": 0.2, "bokchoy": 0.2, "rice": 0.1, "salmon": 0.04, "whiterabbit": 0.02, "lindt": 0.07, "kikkoman": 0.01, "bowls": 0.05, "sauce": 0.05, "dumplings": 0.15, "fishhead": 0.05},
        "bokchoy": {"cake": 0.2, "orange": 0.07, "bokchoy": 0.03, "rice": 0.07, "salmon": 0.03, "whiterabbit": 0.1, "lindt": 0.02, "kikkoman": 0.08, "bowls": 0.2, "sauce": 0.1, "dumplings": 0.05, "fishhead": 0.05},
        "rice": {"cake": 0.1, "orange": 0.07, "bokchoy": 0.03, "rice": 0.2, "salmon": 0.1, "whiterabbit": 0.1, "lindt": 0.02, "kikkoman": 0.1, "bowls": 0.08, "sauce": 0.08, "dumplings": 0.02, "fishhead": 0.1},
        "salmon": {"cake": 0.04, "orange": 0.06, "bokchoy": 0.1, "rice": 0.1, "salmon": 0.1, "whiterabbit": 0.05, "lindt": 0.01, "kikkoman": 0.03, "bowls": 0.07, "sauce": 0.09, "dumplings": 0.05, "fishhead": 0.3},
        "whiterabbit": {"cake": 0.05, "orange": 0.05, "bokchoy": 0.08, "rice": 0.02, "salmon": 0.2, "whiterabbit": 0.2, "lindt": 0.04, "kikkoman": 0.06, "bowls": 0.2, "sauce": 0.02, "dumplings": 0.03, "fishhead": 0.05},
        "lindt": {"cake": 0.1, "orange": 0.2, "bokchoy": 0.05, "rice": 0.05, "salmon": 0.03, "whiterabbit": 0.07, "lindt": 0.2, "kikkoman": 0.08, "bowls": 0.02, "sauce": 0.08, "dumplings": 0.04, "fishhead": 0.08},
        "kikkoman": {"cake": 0.02, "orange": 0.08, "bokchoy": 0.1, "rice": 0.1, "salmon": 0.2, "whiterabbit": 0.1, "lindt": 0.01, "kikkoman": 0.09, "bowls": 0.1, "sauce": 0.05, "dumplings": 0.09, "fishhead": 0.06},
        "bowls": {"cake": 0.03, "orange": 0.07, "bokchoy": 0.1, "rice": 0.2, "salmon": 0.1, "whiterabbit": 0.05, "lindt": 0.03, "kikkoman": 0.07, "bowls": 0.05, "sauce": 0.2, "dumplings": 0.04, "fishhead": 0.06},
        "sauce": {"cake": 0.02, "orange": 0.11, "bokchoy": 0.09, "rice": 0.03, "salmon": 0.08, "whiterabbit": 0.07, "lindt": 0.1, "kikkoman": 0.03, "bowls": 0.07, "sauce": 0.1, "dumplings": 0.2, "fishhead": 0.1},
        "dumplings": {"cake": 0.02, "orange": 0.08, "bokchoy": 0.1, "rice": 0.2, "salmon": 0.02, "whiterabbit": 0.03, "lindt": 0.05, "kikkoman": 0.05, "bowls": 0.1, "sauce": 0.05, "dumplings": 0.2, "fishhead": 0.1},
        "fishhead": {"cake": 0.06, "orange": 0.04, "bokchoy": 0.02, "rice": 0.08, "salmon": 0.1, "whiterabbit": 0.02, "lindt": 0.08, "kikkoman": 0.1, "bowls": 0.2, "sauce": 0.1, "dumplings": 0.1, "fishhead": 0.1}
    })

    new_combination = collage_maker.choose_combination(current_motif="cake", length=5)

    print("Here's the combination:", new_combination)

    collage_maker.create_collage(new_combination)

if __name__ == "__main__":
    main()