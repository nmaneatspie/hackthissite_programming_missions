/*	Program by Norman Thien, Last Updated 25/04/2020

	Program made to complete mission 2 of programming tasks on HackThisSite.com
	This program will look at the provided image file and decode it. This involves
	determining where the white pixels are and to decode the ASCII code based off
	their positions. The offset between a white pixel and the previous white pxiel
	provides the ASCII code. This is in morse-code and will need to be translated
	to readable english characters.
	
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define imgname "download.png"

int main(int argc, char **argv)
{
	char morseToEnglishChar(char *morseInput);
	
	//test morseToEnglishChar
	printf("%c\n", morseToEnglishChar(".-")); //answer should be o
	
	
   return(0);
}

char morseToEnglishChar(char *morseInput)
{

	//hard coded LUT
	struct morseCode 
	{
		char morseString[4];
		short morseNum;
		char morseLetter;
	};
	
	struct morseCode morseLUT[26] = {};
	
	strcpy(morseLUT[0].morseString, ".-");
	strcpy(morseLUT[1].morseString, "-...");
	strcpy(morseLUT[2].morseString, "-.-.");
	strcpy(morseLUT[3].morseString, "-..");
	strcpy(morseLUT[4].morseString, ".");
	strcpy(morseLUT[5].morseString, "..-.");
	strcpy(morseLUT[6].morseString, "--.");
	strcpy(morseLUT[7].morseString, "....");
	strcpy(morseLUT[8].morseString, "..");
	strcpy(morseLUT[9].morseString, ".---");
	strcpy(morseLUT[10].morseString, "-.-");
	strcpy(morseLUT[11].morseString, ".-..");
	strcpy(morseLUT[12].morseString, "--");
	strcpy(morseLUT[13].morseString, "-.");
	strcpy(morseLUT[14].morseString, "---");
	strcpy(morseLUT[15].morseString, ".--.");
	strcpy(morseLUT[16].morseString, "--.-");
	strcpy(morseLUT[17].morseString, ".-.");
	strcpy(morseLUT[18].morseString, "...");
	strcpy(morseLUT[19].morseString, "-");
	strcpy(morseLUT[20].morseString, "..-");
	strcpy(morseLUT[21].morseString, "...-");
	strcpy(morseLUT[22].morseString, ".--");
	strcpy(morseLUT[23].morseString, "-..-");
	strcpy(morseLUT[24].morseString, "-.--");
	strcpy(morseLUT[25].morseString, "--..");

	short i;
	
	for(i = 0; i < 26; ++i)
	{
		morseLUT[i].morseNum = i;
	}
	
	i = 0;
	for(char ch = 'a'; ch <= 'z'; ++ch)
	{
		morseLUT[i].morseLetter = ch;
		++i;
	}	
	
	//compare morseInput to LUT values
	for(i = 0; i < 26; ++i)
	{
		if(!strcmp(morseLUT[i].morseString, morseInput))
		{
			return(morseLUT[i].morseLetter);
		}
	}
	
	return('\0');
	
}