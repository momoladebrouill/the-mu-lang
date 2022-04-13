
bloc * empiler(bloc * head, node * new) {
    bloc * n = (bloc*) blocsize;
    n->node = new;
    n->prev = head;
    return n;
}

bloc * depiler(bloc * head){
    return head->prev;
}

node * createNode(token * tok){
	node * c = (node*) nodesize;
	c->type = tok->type;
	strcpy(c->content, tok->value);
	return c;
}

void * addSon(node * mom, node * new){
	if(mom->child == 0){ // si il n'y en avait pas
		mom->child = new;// il devient l'ainé
	}else{
		node *c = mom->child;
		while(c->bro) {// Chercher le tout petit
			c=c->bro;
		}
		c->bro=new;// Devenir plus petit que le petit
	}
}

node * parse(token *  tok){
    bloc * pile = (bloc *) blocsize;
	node * root = createNode(tok);
    pile->node = root;
	tok = tok->next;
	node * currentNode;
    while (tok) {
		currentNode = pile->node;
        if (tok->type == 1) { // si c'est une balise
            if(tok->value[0] == '/') { // si elle se ferme
                pile = depiler(pile);
            }else{ // sinon on en ouvre une autre
				node * new = createNode(tok);
				addSon(currentNode,new);
				pile = empiler(pile, new);
            }
        }else{ // sinon c'est une feuille de l'AST
			node * n = createNode(tok);
            addSon(currentNode,n);
        }
        tok = tok->next;
    }
    return root;
}

void printFamilly(node * root, int niv){
    for (size_t i = 0; i < niv; i++)printf("---|");
    printf("%s\n",root->content ? root->content : "Empty node wth");
    node * curChild = root->child;
    while (curChild){
        printFamilly(curChild,niv+1);
        curChild = curChild->bro;
    }
}
