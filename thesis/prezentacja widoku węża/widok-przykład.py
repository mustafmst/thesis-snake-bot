# wejście do sieci neuronowej
w = [
    # widoczność owocu
    0,      # góra
    0,      # góra-prawo
    0,      # prawo
    0,      # dół-prawo
    1,      # dół
    0,      # dół-lewo
    0,      # lewo
    0,      # góra-lewo
    # widoczność ogona
    1,      # góra
    0,      # góra-prawo
    0,      # prawo
    0,      # dół-prawo
    0,      # dół
    0,      # dół-lewo
    0,      # lewo
    1,      # góra-lewo
    # odległość od ścian
    1/21,   # góra
    1/2,    # góra-prawo
    1/2,    # prawo
    1/2,    # dół-prawo
    1/8,    # dół
    1/8,    # dół-lewo
    1/27,   # lewo
    1/21    # góra-lewo
]