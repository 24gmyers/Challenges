parent1 = 0
parent2 = 0
square_size = 0
working = False

def start_inputs(parent1,parent2,working,square_size):
    while working == False:
        parent1 = input("How many allele pairs are in the first parents genotype:")
        try:
            parent1 = int(parent1)
            working = True
        except Exception as e:
            working = False
    working = False
    while working == False:
        parent2 = input("How many allele pairs are in the second parents genotype:")
        try:
            parent2 = int(parent2)
            square_size = (f"{parent1 * 2} X {parent2 * 2}")
            working = True
        except Exception as e:
            working = False
    print(f"The Punnet Square will be a: {square_size}")

def main():
    start_inputs(parent1,parent2,working,square_size)

main()
