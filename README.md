# Nombres narcissiques

<!-- TOC -->

- [Nombres narcissiques](#nombres-narcissiques)
    - [Les nombres d'Armstrong](#les-nombres-darmstrong)
    - [Objectifs pédagogiques](#objectifs-pédagogiques)
    - [Algorihme](#algorihme)
    - [Programme de test](#programme-de-test)
    - [En-tête de programme](#en-tête-de-programme)
    - [Affichage de la version](#affichage-de-la-version)
    - [Mode verbeux](#mode-verbeux)
    - [Entrée standard (*stdin*)](#entrée-standard-stdin)

<!-- /TOC -->

- **Durée**: 4 périodes + travail à la maison
- **Date de rendu**: Lundi après les vacances, avant minuit.

## Les nombres d'Armstrong

Un nombre Narcissique ou nombre d'Armstrong est un nombre qui est égal à la somme de ses chiffres chacun exprimé à la puissnce du nombre de chiffres que comporte ce nombre.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/5bdd2cd01bccf25cd2e26563fa08e1469fc22c05)

Par exemple:

- 9 est un nombre narcissique car `9 == pow(9, 1)`
- 10 n'est **pas** un nombre narcissique car `10 != pow(1, 2) + pow(0, 2)`
- 153 est un nombre d'armstrong car: `153 = pow(1, 3) + pow(5, 3) + pow(3, 3)`
- 154 n'est **pas** un nombre narcissique car: `154 != pow(1, 3) + pow(5, 3) + pow(4, 3)`

Le programme retourne le résultat sur son status de sortie:

- `0` Si le nombre d'entrée est un nombre narcissique
- `1` Si le nombre n'est pas un nombre narcissique
- `2` En cas d'erreur

```shell
$ ./armstrong 153
$ echo $?
0
```

## Objectifs pédagogiques

Ce travail pratique permet de se familiariser avec les notions suivantes:

- La structure de contrôle `while`
- La capture d'arguments avec `argv`
- La lecture de l'entrée standard `stdin`
- Les options d'appel `--version`, `--verbose`
- La conception d'algorithmes

## Algorihme

Avant de commencer à coder, il vous est demandé d'inclure à votre référentiel un diagramme en flux représentant votre algorithme. Il vous est proposé d'utiliser https://draw.io et d'exporter votre diagramme en un fichier XML que vous appellerez `algorithm.xml` et que vous pouvez inclure à votre référentiel Git avec:

```
git add algorithm.xml
```

Le diagramme en flux se composera:

- De rectangles arrondis pour le début et la fin de l'algorithme;
- De rectangles pour les actions;
- De losanges pour les décisions.

Une fois terminé vous devez implémenter cet algorithme sous forme d'une fonction dont le prototype est:

```c
bool is_armstrong(int number);
```

## Programme de test

Le programme de test utilise Python. Si vous n'avez pas Python installé sur votre WSL vous pouvez utiliser:

```shell
sudo apt install -y python3 python3-blessings
```

Pour tester votre programme:

```shell
make test
```

Ce programme de test est très complet et comporte plus de 60 tests. L'évaluation de votre travail portera en grande partie en la réussite des tests.

## En-tête de programme

Il vous est demandé d'écrire un en-tête de programme expliquant ce que fait le programme. Inspirez-vous de ceci:

```c
/**
 * Check Armstrong number.
 *
 * This program ...
 *
 * Example:
 *
 *     ./armstrong --verbose ...
 */
```

L'en-tête de programme doit être concis. Sa structure est la suivante:

- Première ligne: résumé du programme en une ligne se terminant par un point.
- Explication détaillée du programme.
- Eventuellement un exemple d'utilisation du programme.

## Affichage de la version

Le programme doit afficher son nom et sa version si appelé avec l'option `--version`:

```shell
$./armstrong --version
Version 1.0.0 (c)2019 Nom Prenom <firstname.lastname@heig-vd.ch>
```

La plupart des programmes disposent de cette option. Essayez par exemple: `git --version` ou `gcc --version`. La convention **GNU** pour la [syntaxe des arguments](https://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html) est qu'un argument de programme est considéré comme une option s'il commence par le caractère `-` ([U+002D](https://www.compart.com/en/unicode/U+002D)). Généralement il existe les options courtes (`-v`, `-h`) et les options longues (`--version`) qui commencent par deux tirets.

Le programme de test vérifie la présence du mot `Version` suivi de 3 chiffres séparés par des points e.g `0.1.1`. Il vérifie la présence d'un e-mail exprimé entre `<>`.

## Mode verbeux

Le programme peut être verbeux, c'est à dire afficher des informations sous forme de texte sur la sortie standard en plus de retourner le résultat dans le status de sortie:

```shell
$./armstrong --verbose 153
Le nombre 153 est bien un nombre d'Armstrong
```

Le programme de test vérifie cette fois-ci que le nombre d'entré est répété sur la sortie, ici `153` et que le texte de sortie comporte `est bien un` ou `is an` dans le car ou c'est un nombre narcissique et `n'est pas un` ou `is not` ou `isn't` dans le cas inverse.

## Entrée standard (*stdin*)

Dans le cas ou le premier argument n'est pas un nombre, le programme obtient le nombre d'entrée via `stdin`:

```shell
$ echo 9 | ./armstrong
$ echo $?
0
```

L'entrée standard peut être lue avec la fonction `scanf`. Essayez par exemple d'exécuter ce programme:

```c
int main(void) {
    int number = 0;
    int n = scanf("%d", &number);

    printf("n = %d, number = %d\n", n, number);
}
```
