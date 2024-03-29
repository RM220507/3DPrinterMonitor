<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>3D Printer Monitor</title>
    <link rel="stylesheet" href="styles.css?<?php echo time(); ?>">
    <?php 
      $files = scandir("Images");
      $latest = end($files);
    ?>
  </head>
  <body>
    <img id="latest" src="Images/<?php echo $latest; ?>" alt="An Image of the 3D Printer" id="image"/>
    <div id="data-display">
      <h1>3D Printer Monitor</h1>
      <p>Latest: <?php echo pathinfo($latest, PATHINFO_FILENAME); ?></p>
      <a href="gallery.php">Click to see a Gallery of Images</a>
    </div>
  </body>
</html>
