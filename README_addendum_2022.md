# Nombres narcissiques, complément


- **Date de rendu**: Selon les information de votre professeur.

## Les nombres d'Armstrong
Pour plus d'information, utiliser la page wikipedia en anglais :
[Narcissistic number](https://en.wikipedia.org/wiki/Narcissistic_number)

## Algorithme

Deux exemples de dessin d'algorithme se trouve sur Cyberlearn.
Il est recommander d'utiliser le standard UML (diagramme d'activité) pour le dessin, mais ce n'est pas une obligation. 

Une fois terminé vous devez implémenter cet algorithme sous forme d'une fonction, voir definition ci-dessous :

```c
/**
 * Le nombre passé en argument est-it un nombre narcissique
 * @param[in] number Nombre à analyser
 * @return Vrais(=1) si number est un nombre narcissique, sinon faux(=0)
 */
bool is_armstrong(int number)
{
    //TODO: ...
}
```

## En-tête de programme

Il vous est demandé d'écrire un en-tête de programme expliquant ce que fait le programme.
Inspirez-vous de l'exemple ci-dessous qui contient le MINIMUM requis (au format [Doxygen](https://doxygen.nl/):
 * description du contenu du fichier,
 * votre nom ou adresse email et
 * la date de création

```c
/**
 * @brief  Détermine si un nombre est narcissique ou non.
 * @author prénom.nom@heig-vd.ch
 * @date   October 2021
 * ... autres info utiles
 */
```

## Mode verbeux

Le programme peut être verbeux, c'est à dire afficher des informations sous forme de texte sur la sortie standard en plus de retourner le résultat dans le status de sortie:

```shell
$./armstrong --verbose 153
Le nombre 153 est un nombre d'Armstrong
```

```shell
$./armstrong --verbose 154
Le nombre 154 n'est pas un nombre d'Armstrong
```

## Entrée standard (*stdin*)

Dans le cas ou le premier argument n'est pas un nombre, le programme obtient le nombre d'entrée via `stdin`:

```shell
$ echo 9 | ./armstrong
$ echo $?
0
```
ou
```shell
$ cat 9 | ./armstrong
$ echo $?
0
```

L'entrée standard peut être lue avec la fonction `fscanf`, [cplusplus.com](https://cplusplus.com/reference/cstdio/fscanf/). Essayez par exemple d'exécuter ce programme:

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    // ...

    // Lecture d'une valeur depuis stdin
    int number = 0;
    if (fscanf(stdin, "%d", &number) == 0);
    {
        // Ecriture vers stderr
        fprintf(stderr, "ERREUR de lecture depuis stdin!\n");
        return 2;
    }

    fprintf(stdout, "number: %d\n", number);
    // ...
    return 0;
}
```