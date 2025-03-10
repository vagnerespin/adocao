// Exibir detalhes do animal no modal
function showAnimalDetails(id) {
    fetch('/animal/' + id)
        .then(response => response.text())
        .then(data => {
            document.getElementById('animal-details').innerHTML = data;
            document.getElementById('animal-modal').style.display = 'flex';
        });
}

// Fechar o modal ao clicar fora dele
window.onclick = function(event) {
    let modal = document.getElementById('animal-modal');
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

// Fechar o modal ao clicar no botão "X"
function closeModal() {
    document.getElementById('animal-modal').style.display = 'none';
}
