
<?php
$conexion = new mysqli("localhost", "root", "", "misperris");   //conexion a la base de datos


//con esto nos evitamos problemas con las ñ y las tildes
$conexion->set_charset('utf8');

$resultadoRegiones = $conexion->query("select * from region");

$resultadoComunas = $conexion->query("select * from comuna");

$resTvivienda = $conexion->query("select * from tipovivienda");
$mensaje = "";

/* Aca envio para guardar los registros */




if(!empty($_POST))
{
   /*var_dump($_POST); /* RESIVE LOS DATOS QUE VIENEN EN EL METODO POST DEL FORMULARIO */
    $rut = $_POST['rut'];
    $nombre = $_POST['txtNombreCompleto'];
    $fecNac  = $_POST['dtFechaNac'];
    $telefono =$_POST['txtTelefono'];
    $comuna = $_POST['cboComuna'];
    $mail = $_POST['email'];
    $tipoVi = $_POST['cboTvivienda'];

    $sql = "insert into cliente values('$rut','$nombre','$comuna','$fecNac','$mail','$tipoVi','$telefono')";
    print $sql;
    $rest = $conexion->query($sql);
    
    if(!$rest){
        $mensaje =$rest."Ha ocurrido un error";
    }else{
        $mensaje ="Guardado correctamente";
    }
}

?>



<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"

      content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">

<meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/estilos.css?v=<?php echo(rand()); ?>">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css">



    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/messages_es.min.js"></script>
    <script src="js/combo.js"></script>
    <script src="js/landing.js"></script>
    <script src="js/validar.js"></script>
    <script src="js/jquery.rut.chileno.min.js"></script>
    <link href='https://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
 
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

    <div class="container">  
    <div id="Titutlo" align="center">Formulario de Inscripción </div>    
       
        <form action="registro.php" id="registroFor" method="POST">
            <label for ="">Ingrese Rut: </label>
            <input type="text" name="rut" id="txtRut" placeholder="Ej: 16321764-2"  required  oninput="checkRut(this)" />
            <br>
            <input type="text" name="txtNombreCompleto" id="txtNombreCompleto" placeholder="Nombre Completo" required onkeypress="return soloLetras(event)"/>
            <br>
            <input type="text" name="txtTelefono" id="txtTelefono" placeholder="Telefono" onkeypress="return soloNumeros(event)" required />
            <label for="">Fecha Nacimiento:</label> 
            <input type="date" name="dtFechaNac" id="dtFechaNac"
             placeholder="Fecha Nacimiento"  required
              min="1980-01-01" max="2000-12-31" />
            <br>
     

        
            <label for="">Región: </label>                    
            <select  class="form-control" name="cboRegion" id="cboRegion"  required>
                <option value="">Seleccionar</option>
                <?php while($fila = $resultadoRegiones->fetch_assoc()): ?>
                    <option value="<?php echo $fila["id"];?>">
                        <?php echo $fila["nombre"]; ?>
                    </option>
                <?php endwhile; ?>
            </select>
            <br>    
            <label for="">Comuna: </label>                         
            <select  class="form-control" name="cboComuna" id="cboComuna" disabled="true" required >
                <option value="">Seleccionar</option>
                <?php while($fila = $resultadoComunas->fetch_assoc()): ?>
                    <option value="<?php echo $fila["id"];?>">
                        <?php echo $fila["nombre"]; ?>
                    </option>
                <?php endwhile; ?>
            </select>
            <br>
            <label for="">Mail:</label>
            <input type="email" name="email" id="email" placeholder="drakan.lord@gmail.com" required>

            <label for="">Tipo Vivienda: </label>                         
            <select  class="form-control" name="cboTvivienda" id="cboTvivienda" required>
                <option value="">Seleccionar</option>
                <?php while($fila = $resTvivienda->fetch_assoc()): ?>
                    <option value="<?php echo $fila["id"];?>">
                        <?php echo $fila["nombre"]; ?>
                    </option>
                <?php endwhile; ?>
            </select>
            <br>    
            <input type="submit" class="button" value="Guardar" id="btnGuardar" name="btnGuardar">
        </form>
    </div>
             

    <footer>
        <h3>Desarrollo Web y Mobile</h3>        
    </footer>
    <h3><?php echo $mensaje; ?></h3>
</body>
</html>

<?php $conexion->close(); ?>







