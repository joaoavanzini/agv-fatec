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
        Serial.println("PARA CIMA - A"); //IMPRIME O TEXTO NO MONITOR SERIAL
    }else{
          if((analogRead(eixo_XA)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
              Serial.println("PARA BAIXO - A"); //IMPRIME O TEXTO NO MONITOR SERIAL
          }else{
                if((analogRead(eixo_YA)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                  Serial.println("DIREITA - A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                }else{
                      if((analogRead(eixo_YA)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                          Serial.println("ESQUERDA - A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                      }else{
                            if(digitalRead(botaoA) == LOW){ //SE LEITURA FOR IGUAL A HIGH, FAZ
                               Serial.println("BOTAO PRESSIONADO - A"); //IMPRIME O TEXTO NO MONITOR SERIAL
                            }else{
                               if((analogRead(eixo_XB)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                                    Serial.println("PARA CIMA - B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                }else{
                                    if((analogRead(eixo_XB)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                                        Serial.println("PARA BAIXO - B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                    }else{
                                            if((analogRead(eixo_YB)) == 0){ //SE LEITURA FOR IGUAL A 0, FAZ
                                            Serial.println("DIREITA - B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                            }else{
                                                if((analogRead(eixo_YB)) == 1023){ //SE LEITURA FOR IGUAL A 1023, FAZ
                                                    Serial.println("ESQUERDA - B"); //IMPRIME O TEXTO NO MONITOR SERIAL
                                                }else{
                                                        if(digitalRead(botaoB) == LOW){ //SE LEITURA FOR IGUAL A HIGH, FAZ
                                                        Serial.println("BOTAO PRESSIONADO - B"); //IMPRIME O TEXTO NO MONITOR SERIAL
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