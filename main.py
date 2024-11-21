""" 
programme de lecture complet et calcul d'un fichier csv contenant des lignes d'entiers.
    Fonction secondaires :
        - read_data(filename)  : retourne le contenu du fichier <filename>
        - get_list_k(data, k)  :
        - get_first(l)         : 
        - get_last(l)          : 
        - get_max(l)           : 
        - get_min(l)           :
        - get_sum(l)           :

    Fonction principale main() qui fait des appels de tests, utilisant les fonctions 
    secondaires ci dessus.
"""
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    retourne le contenu du fichier <filename>
        Args:
            filename (str): nom du fichier à lire

        Returns:
            l (list): le contenu du fichier (1 list d'entiers par ligne)
    """
    with open(filename,mode='r',encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        s = list(r)
        l = [list(map(int, sublist)) for sublist in s]
    return l

def get_list_k(data, k):
    """
    retourne la liste d'indice <k> de la liste de liste <data> 
        Args:
            data (list): la liste de liste d'étude
            k (int): l'indice de la liste à retourner 

        Returns:
            l (list): le contenu du fichier (1 list par ligne)
    """
    l = data[k]
    return l

def get_first(l):
    """
    retourne le premier élément de la liste <l>
        Args:
            l (list): liste à étudier

        Returns:
            int : le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    retourne le dernier élément de la liste <l>
        Args:
            l (list): liste à étudier

        Returns:
            int : le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    retourne la valeur maximum de la liste <l>
        Args:
            l (list): liste à étudier

        Returns:
            int : la valeur maximum de la liste
    """
    return max(l)

def get_min(l):
    """
    retourne la valeur minimum de la liste <l>
        Args:
            l (list): liste à étudier

        Returns:
            int : la valeur minimum de la liste
    """
    return min(l)

def get_sum(l):
    """
    retourne la somme des valeurs de la liste <l>
        Args:
            l (list): liste à étudier

        Returns:
            int : la somme des valeurs de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    fait des appels de tests des fonctions secondaires
    """
    data = read_data(FILENAME)
    print(data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k," : ",get_list_k(data, k))


if __name__ == "__main__":
    main()
