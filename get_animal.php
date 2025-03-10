<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adoção de Animais</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>🐶 Adote um Amigo! 🐱</h1>
    <nav>
        <?php $pagina_atual = basename($_SERVER['PHP_SELF']); ?>
        <?php if ($pagina_atual != 'index.php'): ?><a href='index.php'>Página Inicial</a><?php endif; ?>
        <?php if ($pagina_atual != 'cadastro_adotante.php'): ?><a href='cadastro_adotante.php'>Cadastrar Adotante</a><?php endif; ?>
        <?php if ($pagina_atual != 'login.php'): ?><a href='login.php'>Login</a><?php endif; ?>
    </nav>
    <div class="banner-container">
        <img src="img/banner1.jpg" alt="Cachorros felizes">
<img src="img/banner2.jpg" alt="Gatinhos fofos">
<img src="img/banner3.jpg" alt="Adote um pet hoje!">
    </div>
    
    <section>
        <h2>🐾 Nossos Amiguinhos Esperando por Você! 🐾</h2>
        <div class="animal-list">
            <?php include 'conexao.php'; ?>
            <?php
            $result = $conn->query("SELECT * FROM animais");
            while ($row = $result->fetch_assoc()) {
                $foto = !empty($row['foto']) ? $row['foto'] : 'img/default_pet.png';
                echo "<div class='animal-card' onclick='showAnimalDetails({$row['id']})'>";
                echo "<div class='animal-photo-frame'>";
                echo "<img src='$foto' alt='Foto de {$row['nome']}' class='animal-img'>";
                echo "</div>";
                echo "<h3>{$row['nome']} ({$row['especie']})</h3>";
                echo "<p>Idade: {$row['idade']}</p>";
                echo "</div>";
            }
            ?>
        </div>
    </section>
    
    <div id="animal-modal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <div id="animal-details"></div>
        </div>
    </div>
    
    <button onclick="window.history.back()" class="back-button">⬅ Voltar</button>
    
    <script>
        function showAnimalDetails(id) {
            fetch('get_animal.php?id=' + id)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('animal-details').innerHTML = data;
                    document.getElementById('animal-modal').style.display = 'block';
                });
        }

        function closeModal() {
            document.getElementById('animal-modal').style.display = 'none';
        }
    </script>
</body>
</html>
