/* amobin19
   12/07/2018
   Resources Used: calloc() versus malloc(), GeeksforGeeks
                   Malloc Tutorial, D. Luu
                   The C Programming Language, B.W. Kernighan
                                               D.M. Ritchie 
*/


/*-----------------------------------------------------------------------------------------------------------------------*/
// CODE DOCUMENTATION BELOW
/*-----------------------------------------------------------------------------------------------------------------------*/

/* The code starts with includeing the standard input output library and the standard library.
   Then I define the size of the heap to 2^16 blocks. Then I initialize the pointer to the head of the block.
   Then I include the function prototypes for the malloc (mmaloc) and free (mfree) functions that will be defined later on.

   After I initialize the main block structure which include the qualities of the block such as the 
   integer size of the block, the pointer to the next block, and the integer value that represents a boolean 1 and 0 to 
   represent if the block is free or not (1 being free, 0 being not). 

   Then I define a helper method which would search for a free block with parameters of a pointer to a tail pointer and 
   the size requested. This method basically iterates through the block until a large enough block is found.
   The way this is done is by first initializing a new block structure at the start, 
   this new block structure would be the current block that the pointer begins at. Then as long as the size is not greater
   than the requested size and if it is free and the current pointer is a valid pointer, then the tail which is the running
   end block would be assigned to current. Then the next pointer from current would point to the next value from the current
   block. Then the current block is what would be returned.

   Then the mmaloc method is implemented which is responsible for allocating memory to the requested space. First I 
   initialize a base for the requested amount which I name tail because it is at first the beginning block but 
   eventually it will be the end of the block amount to represent the whole amount requested. Then I initialize that 
   block to be no longer than the heap size which I declared earlier. After that I call the free finder method on the block
   to search for a free block in the amount of available spaces. If no free block is found then NULL is returned. Else if 
   an appropriate amount can be allocated then I flag free in that block to be 0, meaning it is no longer free.

   Then the free method is implemented which is responsible for deallocating memory which has previously been allocated.
   This takes in the parameter of a pointer. If this pointer is not a valid pointer then nothing is returned as this method
   is a void method which will simply flag space as free or not. If an appropriate block pointer is found then it will
   be declared a s new block which would be flagged as free and available to use.

   Then I declare the main function where the tests of the functions will be carried out. I initialize two arrays, an integer 
   array and a char array. Then I request to allocate some memory into both arrays using the mmaloc method. 
   After I attempt to allocate memory, I attempt to free the requested amounts using the mfree method. */


/*-----------------------------------------------------------------------------------------------------------------------*/
// CODE BELOW
/*-----------------------------------------------------------------------------------------------------------------------*/

#include <stdio.h> // include std input/output lib
#include <stdlib.h> // include std lib 

#define HEAP_SIZE 65536 // 2^16 size of heap

void *start = NULL; // single global pointer to start
void * mmaloc(int bytes); // prototype for malloc
void mfree(void *ptr); // prototype for free

// block structure
struct block_struct {
	int size; // size of block
	struct block_struct *next; // pointer to next block
	int free; // if free then 1, else 0
};

// helper method that iterates through blocks
// until large enough block found
struct block_struct * free_finder(struct block_struct **tail, int size){ // pointer to tail pointer to determine current 
	                                                                     // pointer and size to determine if valid size to 
	                                                                     // be requested
	struct block_struct *curr = start; // current block
	while(!(curr->size >= size && curr->free) && curr){ // not greater than requested size and free
		*tail = curr; // pointer to last block points to current
		              // tail is pointer which stores the address of the current pointer
		curr = curr->next; // current points to next block
	}
	return curr; // returns the current
}

// allocates the memory for a requested number of bytes
void * mmaloc(int bytes){ // int parameter to determine requested number of spaces to be used
	struct block_struct *tail; // initialize base
	tail -> size = HEAP_SIZE - sizeof(struct block_struct); // initialize memory block to available size
	tail = free_finder(&tail, bytes); // look for free block
	if(!tail){ // if no free block 
		return NULL; // return NULL
	}
	else{ // if free block found
		tail->free = 0; // block is no longer free
	}
}

// deallocates memory previously allocated 
void mfree(void *free_ptr){ // pointer parameter to determine if valid to be free or not
	if(!free_ptr){ // if not appropriate pointer 
		return; // return nothing because void function
	}
	else { // else if appropriate block pointer found
		struct block_struct *new_block; // new block declared to be freed
		new_block->free = 1; // that block is freed
	}
}

// to test mmaloc and mfree methodds
int main(){
   int *arr1; // new int array declared
   arr1 = (int *) mmaloc(sizeof(int) * 3); // allocate the memory for 3 integer spaces  
   mfree(arr1); // deallocates the integer memory 
   char * arr2; // new char array declared
   arr2 = (char *) mmaloc(sizeof(char) * 5); // allocate the memory for 5 character spaces
   mfree(arr2); // deallocates the character memory  
   return 0; // defalut main return 
}