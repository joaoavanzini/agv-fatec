int eixo_XA = A0;
int eixo_YA = A1; //PINO REFERENTE A LIGAÇÃO DO EIXO Y
int botaoA = 2; //PINO REFERENTE A LIGAÇÃO NO PINO KEY (EIXO Z)

int eixo_XB = A2;
int eixo_YB = A3; //PINO REFERENTE A LIGAÇÃO DO EIXO Y
int botaoB = 3; //PINO REFERENTE A LIGAÇÃO NO PINO KEY (EIXO Z)

void setup(){
  pinMode (botaoA, INPUT_PULLUP); //DEFINE A PORTA COMO ENTRADA / "_PULLUP" É PARA ATIVAR O RESISTOR INTERNO
  pinMode (botaoB, INPUT_PULLUP);
  Serial.begin (9600); //INICIALIZA O MONITOR SERIAL
}
void loop(){
 
    if((analogRead(eixo_XA)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
        Serial.println("1-A"); //IMPRIME O TEXTO NO MONITOR SERIAL
    }else{
          if((analogRead(eixo_XA)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
              Serial.println("2-A"); //IMPRIME O TEXTO NO MONITOR SERIAL
          }else{
                if((analogRead(eixo_YA)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                  Serial.println("3-A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                }else{
                      if((analogRead(eixo_YA)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                          Serial.println("4-A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                      }else{
                            if(digitalRead(botaoA) == LOW){ //SE LEITURA FOR IGUAL A HIGH, FAZ
                               Serial.println("5-A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                            }else{
                               if((analogRead(eixo_XB)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                                    Serial.println("1-B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                }else{
                                    if((analogRead(eixo_XB)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                                        Serial.println("2-B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                    }else{
                                            if((analogRead(eixo_YB)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                                            Serial.println("3-B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                            }else{
                                                if((analogRead(eixo_YB)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                                                    Serial.println("4-B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                                }else{
                                                        if(digitalRead(botaoB) == LOW){ //SE LEITURA FOR IGUAL A HIGH, FAZ
                                                        Serial.println("5-B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                                        }  
                                                }
                                            }
                                    }
                                }  
                            }
                      }
                }
          }
    }
}