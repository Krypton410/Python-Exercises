import random 
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        
        self.location = location


    def get_number_of_species(self, animal):
        
        try:
            return self.species_types[animal]
        except:
            return 0
    
    def get_location(self):
        return tuple(map(float, self.location)) 
    
    def get_species_count(self):
        return self.species_types.copy()
    
    def get_name(self):
        return self.name
    
    def adopt_pet(self, species):
        
        if self.species_types[species] > 0:

            self.species_types[species] -= 1
        
        if self.species_types[species] == 0:
            del self.species_types[species]


class Adopter(object):
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name
    
    def get_desired_species(self):
        return self.desired_species
    
    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species #A list of strings of different species.

    def get_score(self, adoption_center):
        
        count = 0
        for i in self.considered_species:
            count += adoption_center.get_number_of_species(i)

        


        
        if Adopter.get_score(self, adoption_center) + (0.3 * count) > 0:
            return Adopter.get_score(self, adoption_center) + 0.3 * count 
        
        else:
            return 0.0



class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        
        
        count = adoption_center.get_number_of_species(self.feared_species)

        if Adopter.get_score(self, adoption_center) - 0.3 * count > 0:
            return Adopter.get_score(self, adoption_center) - (0.3 * count)
        else:
            return 0.0



class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species #list of strings

    def get_score(self, adoption_center):
        for i in adoption_center.get_species_count().keys():

            if i in self.allergic_species:
                return 0.0
            
        return Adopter.get_score(self, adoption_center)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness #dic - str:float (Species:effectiveness) (0.0-1.0)

    def get_score(self, adoption_center):
        effected = {}
        for i in adoption_center.get_species_count().keys():
            if i in self.medicine_effectiveness:
                effected[i] = self.medicine_effectiveness[i]
        
        if len(effected) > 0:
            lowest = min(effected.values())
        else:
            lowest = 1

        
        return Adopter.get_score(self, adoption_center) * lowest




class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelling. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = tuple(map(float, location))# tuple of floats.

    def get_linear_distance(self, adoption_center):
        
        distance = pow((self.location[0] - adoption_center.get_location()[0])**2 + 
                     (self.location[1] - adoption_center.get_location()[1])**2, 0.5)
        return distance

        

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelling. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = tuple(map(float, location))# tuple of floats.

    def get_linear_distance(self, adoption_center):
        
        distance = pow((self.location[0] - adoption_center.get_location()[0])**2 + 
                     (self.location[1] - adoption_center.get_location()[1])**2, 0.5)
        return distance

        

    def get_score(self, adoption_center):
        
        count = [0, 0]
        
       
        if self.get_linear_distance(adoption_center) < 1:
            for i in adoption_center.get_species_count().keys():
                if i in self.desired_species:
                    count = [i, adoption_center.get_number_of_species(i)]
            
            return count[1]

        
        elif self.get_linear_distance(adoption_center) >= 1 and self.get_linear_distance(adoption_center) < 3:
            for i in adoption_center.get_species_count().keys():
                if i in self.desired_species:
                    count = [i, adoption_center.get_number_of_species(i)]
            
            return count[1] * random.uniform(0.7, 0.9)

        elif self.get_linear_distance(adoption_center) >= 3 and self.get_linear_distance(adoption_center) < 5:
            for i in adoption_center.get_species_count().keys():
                if i in self.desired_species:
                    count = [i, adoption_center.get_number_of_species(i)]
            
            return count[1] * random.uniform(0.5, 0.7)

        elif self.get_linear_distance(adoption_center) >= 5:
            
            for i in adoption_center.get_species_count().keys():
                if i in self.desired_species:
                    count = [i, adoption_center.get_number_of_species(i)]           
            return count[1] * random.uniform(0.1, 0.5)



    

def get_ordered_adoption_center_list(Adopter, Centers):

    return sorted (Centers, key=lambda t: \
           (-Adopter.get_score(t),t.get_name()))

def get_adopters_for_advertisement (Center, Adopters, n):

    return sorted (Adopters, key=lambda t:  \
(-t.get_score(Center),t.get_name()))