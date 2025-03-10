<?php
session_start();
include 'conexao.php';

if (isset($_POST['login'])) {
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];

    // Consulta no banco de dados
    $sql = "SELECT * FROM usuarios WHERE usuario='$usuario' AND senha='$senha'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $_SESSION['usuario'] = $usuario;
        header("Location: cadastro_animal.php"); // Redireciona para o cadastro de animais
        exit();
    } else {
        $erro = "Usuário ou senha incorretos!";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <h1>🔐 Login</h1>
    <nav>
        <a href='index.php'>Página Inicial</a>
        <a href='listar_animais.php'>Ver Animais Disponíveis</a>
    </nav>

    <form method="post" action="">
        <label>Usuário:</label>
        <input type="text" name="usuario" required><br>

        <label>Senha:</label>
        <input type="password" name="senha" required><br>

        <input type="submit" name="login" value="Entrar">
    </form>

    <?php if (isset($erro)) { echo "<p style='color: red;'>$erro</p>"; } ?>

</body>
</html>
