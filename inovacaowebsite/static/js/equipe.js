document.addEventListener('DOMContentLoaded', function() {
  // Pegar os containers
  const containers = document.querySelectorAll('.member-container');

  // Evento de clique para cada container
  containers.forEach(container => {
    container.addEventListener('click', function() {
      // Extraindo o conteudo do modal
      const nome = this.querySelector('.member-info h4').textContent;
      const curso = this.querySelector('.member-info span').textContent;
      const funcao = this.querySelector('.member-info p').textContent;
      const descricao = this.querySelector('.member-info .p').textContent;

      // Inserções do titulo e corpo do modal
      const modalLabel = document.getElementById('memberModalLabel');
      modalLabel.textContent = nome;

      const modalBody = document.querySelector('.modal-body');
      modalBody.innerHTML = `
        <p><strong>Curso:</strong> ${curso}</p>
        <p><strong>Função:</strong> ${funcao}</p>
        <p><strong>Descrição:</strong> ${descricao}</p>
      `;

      // Mostra o modal
      const modal = new bootstrap.Modal(document.getElementById('memberModal'));
      modal.show();
    });
  });
});