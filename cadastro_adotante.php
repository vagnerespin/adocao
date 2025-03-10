<?php include 'conexao.php'; ?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Adotantes</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <h1>🐾 Cadastro de Adotantes 🐾</h1>
    <nav>
        <a href='index.php'>Página Inicial</a>
        <a href='login.php'>Login</a>
        <a href='listar_animais.php'>Ver Animais Disponíveis</a>
    </nav>

    <form method="post" action="">
        <label>Nome:</label>
        <input type="text" name="nome" required><br>

        <label>Telefone:</label>
        <input type="text" name="telefone" required><br>

        <label>Email:</label>
        <input type="email" name="email" required><br>

        <label>Endereço:</label>
        <textarea name="endereco" required></textarea><br>

        <label>Interesse (Cachorro/Gato/Outro):</label>
        <input type="text" name="interesse"><br>

        <input type="submit" name="cadastrar" value="Cadastrar">
    </form>

    <?php
    if (isset($_POST['cadastrar'])) {
        $sql = "INSERT INTO adotantes (nome, telefone, email, endereco, interesse)
                VALUES ('{$_POST['nome']}', '{$_POST['telefone']}', '{$_POST['email']}', '{$_POST['endereco']}', '{$_POST['interesse']}')";
        
        if ($conn->query($sql) === TRUE) {
            echo "<p style='color: green;'>Adotante cadastrado com sucesso!</p>";
        } else {
            echo "<p style='color: red;'>Erro: " . $conn->error . "</p>";
        }
    }
    ?>

</body>
</html>
