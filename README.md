# Aplicación Patrón Adapter

La idea principal del proyecto es realizar un programa que mueva su personaje a la derecha y a la izquierda, para posteriormente adaptar el muñeco de un compañero a nuestro programa creando el adaptador sin tener la necesidad de realizar ningun cambio al programa original.

## Adapter
Permiten que cooperen clases que de otra manera no podrían por tener interfaces incompatibles y convierte la interfaz de una clase en otra distinta que es la que esperan los clientes. Permiten que cooperen clases que de otra manera no podrían por tener interfaces incompatibles.

## ¿Como se implemento? :question:

La implementación del patrón se dio haciendo una adaptación de un personaje externo a los creados en el juego inicialmente, adaptando la logica del personaje a la nuestra para que funcione correctamente en nuestro juego. La clase adaptada es la clase Character que hace referencia al jugador externo adaptandolo en la clase Jugador_adapter y se llama a su respectivo constructor dependiendo del personaje que se prefiera. 

## Datos de la ejecución del Programa :mag_right:

### Cambiar de personaje :two_men_holding_hands:
Para elegir si se quiere un personaje clasico del programa o si se quiere el nuevo personaje, al ejecutar el programa se preguntara al cliente que dependiendo del personaje ingrese una letra, para el personaje nuevo sera n y para el personaje clasico sera c. 

Personaje clasico 
![personajeclasico](https://github.com/valentinatobo/Movimiento_Sprite/blob/master/imagenes/logos/personajeclasico.PNG)

Personaje Nuevo
![personaje nuevo](https://github.com/valentinatobo/Movimiento_Sprite/blob/master/imagenes/logos/nuevopersonaje.PNG)



## Autores

* **Diana Valentina Uscategui Tobo - 20172020063
* **Edwin Andres Salinas Chaparro - 20172020087
