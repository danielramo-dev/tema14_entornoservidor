<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noticias RSS</title>
</head>
<body>

<?php
$rss_urls = [
    "El Periódico" => 'https://www.elperiodico.com/es/cds/rss/?id=board.xml',
    "ABC Última Hora" => 'https://www.abc.es/rss/2.0/ultima-hora/'
];

foreach ($rss_urls as $nombre => $url) {
    $feed = simplexml_load_file($url);


    echo "<h1>Noticias de $nombre</h1>";
    echo "<ul>";

    foreach ($feed->channel->item as $item) {
        $title = (string) $item->title;

        echo "<h2>$title</h2>";
    }
    echo "</ul>";
}
?>

</body>
</html>
