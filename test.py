from PIL import Image
import numpy as np

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
        return np.random.choice(
            self.motifs,
            p = [self.transition_matrix[current_motif][next_motif] \
                for next_motif in self.motifs]
        )

    def choose_combination(self, current_motif="cake", length=2):
        combination = []

        while len(combination) < length:
            next_motif = self.get_next_motif(current_motif)
            combination.append(next_motif)
            current_motif = next_motif
        
        return combination

    def create_collage(self, combination):
        background = Image.new("RGBA", (1000,1000), color=(255,255,255))

        for motif in combination:
            #img = Image.open("/Users/tomalley/markov-artwork/images/cake.png")
            img = Image.open("/Users/tomalley/markov-artwork/images/" + motif + ".png")
            img = img.resize((500,500))

            if motif == combination[0]:
                background.paste(img, (0,0))

            if motif == combination[1]:
                background.paste(img, (500,500))

        background.show()


def main():
    collage_maker = MarkovCollager({
        "cake": {"cake": 0.3, "orange": 0.7},
        "orange": {"cake": 0.6, "orange": 0.4}
    })

    new_combination = collage_maker.choose_combination(current_motif="cake", length=2)

    print("Here's the combination:", new_combination)

    collage_maker.create_collage(new_combination)

if __name__ == "__main__":
    main()



# background = Image.new("RGBA", (1000,1000), color=(255,255,255))
# img = Image.open("/Users/tomalley/markov-artwork/images/cake.png")
# img = img.resize((500,500))

# background.paste(img, (0,0))
# background.paste(img, (500,500))

# background.show()