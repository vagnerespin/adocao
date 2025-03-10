<?php include 'conexao.php'; ?>

<form method="post" action="" enctype="multipart/form-data">
    Nome: <input type="text" name="nome" required><br>
    Espécie: <input type="text" name="especie" required><br>
    Idade: <input type="text" name="idade" required><br>
    Comportamento: <textarea name="comportamento" required></textarea><br>
    Foto: <input type="file" name="foto" required><br>
    <input type="submit" name="cadastrar" value="Cadastrar">
</form>

<?php
if (isset($_POST['cadastrar'])) {
    $foto = "uploads/" . basename($_FILES["foto"]["name"]);
    move_uploaded_file($_FILES["foto"]["tmp_name"], $foto);

    $sql = "INSERT INTO animais (nome, especie, idade, comportamento, foto)
            VALUES ('{$_POST['nome']}', '{$_POST['especie']}', '{$_POST['idade']}', '{$_POST['comportamento']}', '$foto')";
    
    if ($conn->query($sql) === TRUE) {
        echo "Animal cadastrado com sucesso!";
    } else {
        echo "Erro: " . $conn->error;
    }
}
?>
