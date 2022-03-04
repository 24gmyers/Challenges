allele_type = 0
parent = 0
square_size = ""
working = False

def start_inputs(parent,working,square_size,allele_type):
    while working == False:
        allele_type = input("What type of gene is this?\n1) mandelian traits\n2) nonmandelian traits\n3) sex-linked traits\n")
        if allele_type == "1" or allele_type == "2" or allele_type == "3":
            working = True
        else:
            working = False
    working = False
    while working == False:
        parent1 = input("How many allele pairs are in the first parents genotype:")
        try:
            parent1 = int(parent)
            square_size = (f"{parent * 2} X {parent * 2}")
            working = True
        except Exception as e:
            working = False
    working = False
    print(f"The Punnet Square will be a: {square_size}")

def main():
    start_inputs(parent,working,square_size,allele_type)

main()
