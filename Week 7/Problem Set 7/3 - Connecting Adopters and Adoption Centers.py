def get_ordered_adoption_center_list(Adopter, Centers):

    return sorted (Centers, key=lambda t: \
           (-Adopter.get_score(t),t.get_name()))

def get_adopters_for_advertisement (Center, Adopters, n):

    return sorted (Adopters, key=lambda t:  \
(-t.get_score(Center),t.get_name()))