// amobin 09/14/2018
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char userInput[100];
	char userRev[100];
	unsigned int count = 0;
	int x = 0;
	int y = 0;

	printf("Please enter some string less than 100: \n");
	scanf("%[^\n]%*c", userInput); // scan char to count for each char


	while(userInput[count] != '\0'){ // for each char until last char
		++count; // increment counter
	}

	printf("Total number of characters: %d\n", count);

	for(x = count - 1; x >= 0; x--){ // start at end until beginning
		userRev[y++] = userInput[x]; // for each backward for each forward
	}

	printf("Reversed string: %s\n", userRev);

	return 0;
}