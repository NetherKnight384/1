< ?php
$M = [
    0 => "123",
];
$cash = serialize($M);
file_put_contents("om.txt", $cash);
unset($cash);

$Id = [
    "User" => 0,
];
$cash = serialize($Id);
file_put_contents("oi.txt", $cash);
unset($cash);