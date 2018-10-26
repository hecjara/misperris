<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/estilos.css?v=<?php echo(rand()); ?>">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js"></script>
    <script src="js/landing.js"></script>
    <title>Mis perris</title>
</head>
<body>
    <!--este es un comentario-->
   <header>
       <img class="logo" src="img/logo.png" alt="logo">
       <ul class="navegacion">
            <li><a href="index.php">Inicio</a></li>
            <li><a href="#">Quienes Somos</a></li>
            <li><a href="#">Servicios</a></li>
            <li><a href="#">Contáctanos</a></li>
            <li><a href="galeria.php">Galeria</a></li>            
            <li><a href="registro.php">Registro</a></li>
       </ul>
    </header>
    <div class="landing">
        <div class="slider">
            <div>
                <img title="Apolo viaja feliz con sus nuevos dueños" class="imagen_landing" src="img/adoptados/Apolo.jpg" alt="Apolo">   
            </div>
            <div>
                <img title="Duque disfruta de la hermosa vista que da la montaña" class="imagen_landing" src="img/adoptados/Duque.jpg" alt="Duque">   
            </div>
            <div>
                <img title="Tom se toma un merecido descanzo despues de estar jugando con Sofia" class="imagen_landing" src="img/adoptados/Tom.jpg" alt="Tom">   
            </div>     
        </div>
       
        <div class="landing_inferior">
            <h1 class="color_blanco centrar_texto">+56 9 98765431</h1>
            <h1 class="color_blanco centrar_texto">Rescate y adopción de perros callejeros</h1>
            <ul class="social">            
                    <li><img src="img/socialfacebook.png" alt="facebook"></li>
                    <li><img src="img/socialplus.png" alt="plus"></li>
                    <li><img src="img/social-inst.png" alt="instagram"></li>
                    <li><img src="img/correo.png" alt="mail"></li>
            </ul>
        </div>
    </div>

    <div class="contenido">
        <div class="lateral">
            <h3 align="right">RESCATE</h3>
            <h6 align="right">ETAPA UNO</h6>
            <br>
            <hr class="lineaIzq">
            <br>
            <p align="right">Rescatamos perros en situación de peligro y/o abandono. Los rehabilitamos y
                los preparamos para buscarles un nuevo hogar.
            </p>
            <br>
            <img class="rescate" src="img/rescate.jpg" alt="rescate">           
        </div>
        <div class="principal">
            <img class="crowfunding" src="img/crowfunding.jpg "alt="comida">
            <h3>CROWFUNDING</h3>
            <H4>FINANCIAMIENTO</H4>
            <br>
            <hr class="lineaDer">
            <br>
            <p>Sigue nuestras redes sociales para informarte 
                acerca de las diversas campañas y actividades que realizaremos
                para obtener financiamiento para seguir ayudando
            </p>
            <br>

                <button class="button2">CAMPAÑAS</button>
        </div>
    </div>
    <br><br><br>
         

    <footer>
        <h3>Desarrollo Web y Mobile</h3>
        
    </footer>
 
</body>
</html>