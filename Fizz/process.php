<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $cash = file_get_contents("om.txt");
    $M = unserialize($cash);
    unset($cash);
    $cash = file_get_contents("oi.txt");
    $ID = unserialize($cash);
    unset($cash);

    // Получение данных из формы
    $username = htmlspecialchars($_POST['username']);
    $password = intval($_POST['password']);

    $cash = $ID[$username];
    if ($password == $M[$cash])
    {
        echo "username: " . $username . "<br>";
        echo "password: " . $password . "<br>";
    } else {
        header("Location: Login.html");
        exit;
    }
    // Обработка данных (например, вывод на экран)
    


    
    exit();
} else {
    echo "E1";
}

