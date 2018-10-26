<?php

//paso 1: recuperar el id que javascript nos mando

$id = $_GET["id"];
$conexion = new mysqli("localhost", "root", "", "misperris");  
$conexion->set_charset("utf8");
$resultado = $conexion->query("select * from comuna where region_id  = $id");

?>

<option value="">Seleccionar</option>
<?php while($fila = $resultado->fetch_assoc()): ?>
<option value="<?php echo $fila["id"];?>">
    <?php echo $fila["nombre"]; ?>
</option>
<?php endwhile; ?>
