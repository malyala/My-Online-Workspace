/* 
 * Fixed size hash map for char[16] keys
 *
 *
 *
 *
 */

typedef Hashmap Hashmap;
typedef enum {False, True} boolean;


//Constructors
Hashmap * hashmap(int size);
boolean Set(Hashmap *map, char[16] key, void *value );

//Accessors
void * Get(Hashmap *map, char[16] key);
long Load(Hashmap *map);

//Desconstructor
void * Delete(Hashmap *map, char[16] key);




