<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>El Tiempo en Fuenlabrada</title>
</head>
<body>
    <?php
    $url = 'https://www.el-tiempo.net/api/json/v2/provincias/28/municipios/28058';


    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);




    $data = json_decode($response, true);




    $nombre_ciudad = $data['municipio']['NOMBRE'] ;
    $temperatura = $data['temperatura_actual'] . 'ºC';
    $estado_cielo = $data['stateSky']['description'];


    echo "<h1>El Tiempo en $nombre_ciudad</h1>";
    echo "<p><strong>Temperatura Actual:</strong> $temperatura</p>";
    echo "<p><strong>Estado del Cielo:</strong> $estado_cielo</p>";
    ?>
</body>
</html>