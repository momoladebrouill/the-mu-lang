/*
Fichier qui contient toutes les structures utilisées
*/

#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize malloc(sizeof(node))

/* les types:
0: string
1: balise  
2: number
3: identifier
*/

typedef struct token {
  int type;
  char value[100]; // Les valeurs des tokens sont ainsi limités à 100 caractères
  struct token * next;
}token;


typedef struct node{
    int type;
    char content[100];
    struct node * child;
    struct node * bro;
}node;

typedef struct bloc{
    node * node;
    struct bloc * prev;
}bloc;
