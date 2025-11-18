// Funções para gerenciar modais
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
    }
}

// Fechar modal ao clicar fora
window.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('active');
    }
});

// Funções específicas para modal de membros da empresa
function openMemberModal() {
    openModal('memberModal');
}

function closeMemberModal() {
    closeModal('memberModal');
}

// Funções específicas para modal de adicionar membros ao projeto
function openAddMemberModal() {
    openModal('addMemberModal');
}

function closeAddMemberModal() {
    closeModal('addMemberModal');
}

// Confirmação antes de deletar
function confirmDelete(itemName) {
    return confirm(`Tem certeza que deseja excluir "${itemName}"?`);
}
